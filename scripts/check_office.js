/* Does the office page actually work on the phone that reads it?
 *
 * Why this exists (KB-174, KB-175). Every check this company had ran the page as an
 * ordinary web page in one desktop-ish state: load it, screenshot it, move on. The
 * chairman reads it on a phone, from the home screen, with the agent panel open. Two
 * defects in two days survived every check we had, because no check ever ran in the
 * state he uses:
 *
 *   - every product link asked for a new tab, which a standalone home-screen app
 *     silently discards, so all of them were dead for the only person who taps them;
 *   - the agent panel lost its right-hand edge -- tabs, the send button, the end of
 *     every line -- and nothing in the build could have noticed.
 *
 * So this checks the real states, and fails rather than warns:
 *   * four phone widths, narrowest first, plus the panel OPEN on each;
 *   * every view the bottom tab bar can reach;
 *   * the real webfonts, which are wider than the fallbacks, when the network allows;
 *   * no element may extend past the viewport, and the document may not scroll
 *     sideways, except inside something that deliberately scrolls sideways;
 *   * no link may ask for a new tab;
 *   * every product link's printed address must equal its href.
 *
 *     node scripts/check_office.js            # observer/office.html
 *     node scripts/check_office.js --serve    # same, over http, so fonts load
 */

const { chromium } = require("playwright");
const path = require("path");
const http = require("http");
const fs = require("fs");

const REPO = path.dirname(__dirname);
const PAGE = path.join(REPO, "observer", "office.html");
const WIDTHS = [320, 375, 390, 430];
const EXEC = "/opt/pw-browsers/chromium";

const problems = [];
const fail = (m) => problems.push(m);

/* Serve the folder so the Google Fonts <link> resolves; file:// gets fallback
   metrics, which are narrower, which is how a too-wide layout passes locally. */
function serve(dir) {
  return new Promise((resolve) => {
    const srv = http.createServer((req, res) => {
      const f = path.join(dir, decodeURIComponent(req.url.split("?")[0]));
      fs.readFile(f, (e, b) => {
        if (e) { res.writeHead(404); return res.end("no"); }
        res.writeHead(200, { "content-type": f.endsWith(".html") ? "text/html" : "application/octet-stream" });
        res.end(b);
      });
    });
    srv.listen(0, "127.0.0.1", () => resolve({ srv, port: srv.address().port }));
  });
}

/* Anything sticking out past the right edge.
 *
 * The side-scrollers are named explicitly and nothing else counts as one. Reading the
 * computed style instead looked cleverer and was wrong: a box with `overflow-y: auto`
 * gets `overflow-x: auto` computed for free, and this page puts almost all of its
 * content inside `.card .body`, which scrolls vertically -- so a style-based rule
 * quietly excused most of the page and passed a 520px-wide block on a 320px screen.
 * An allowlist cannot drift that way. `.mapwrap` (the floor plan) and the stat strips
 * are the only things here meant to scroll sideways. */
const SIDE_SCROLLERS = ".mapwrap, .stats, .top-in, [data-xscroll]";
const OVERFLOW = `(() => {
  const vw = document.documentElement.clientWidth, bad = [];
  document.querySelectorAll('*').forEach(el => {
    const r = el.getBoundingClientRect();
    if (!r.width || el.hidden) return;
    if (r.right > vw + 1 || r.left < -1) {
      if (el.closest(${JSON.stringify("__SS__")})) return;
      bad.push(el.tagName.toLowerCase() + '.' +
        String(el.className || '').split(' ')[0] + ' [' + Math.round(r.left) + '..' +
        Math.round(r.right) + '] "' + (el.textContent || '').trim().slice(0, 28) + '"');
    }
  });
  return { vw, scrollW: document.documentElement.scrollWidth, bad: bad.slice(0, 6) };
})()`.replace("__SS__", SIDE_SCROLLERS);

async function sweep(pg, width, label) {
  const r = await pg.evaluate(OVERFLOW);
  if (r.scrollW > r.vw + 1)
    fail(`${width}px, ${label}: the page scrolls sideways (${r.scrollW} wide in ${r.vw}). ` +
         `On a phone that widens the layout viewport and every fixed overlay is drawn ` +
         `wider than the screen.`);
  r.bad.forEach((b) => fail(`${width}px, ${label}: ${b} reaches past the right edge.`));
}

(async () => {
  if (!fs.existsSync(PAGE)) {
    console.error("FAIL: observer/office.html does not exist. Build it first.");
    process.exit(1);
  }
  const { srv, port } = await serve(path.join(REPO, "observer"));
  const proxy = (process.env.HTTPS_PROXY || "").replace(/^https?:\/\//, "");
  const browser = await chromium.launch({
    executablePath: EXEC,
    args: proxy ? ["--proxy-server=" + proxy, "--ignore-certificate-errors"] : [],
  });
  let fontsLoaded = 0;

  for (const width of WIDTHS) {
    const pg = await browser.newPage({ viewport: { width, height: 844 } });
    const jsErrors = [];
    pg.on("pageerror", (e) => jsErrors.push(String(e.message)));
    await pg.goto(`http://127.0.0.1:${port}/office.html`, { waitUntil: "load" });
    await pg.waitForTimeout(1200);
    fontsLoaded = await pg.evaluate(() =>
      document.fonts ? [...document.fonts].filter((f) => f.status === "loaded").length : 0);

    /* every view the bottom bar can reach */
    const views = await pg.evaluate(() =>
      [...document.querySelectorAll("#tabs button, #sheetlist button")]
        .map((b) => (b.textContent || "").trim()).filter((t) => t && t !== "More"));
    for (const v of views) {
      await pg.evaluate((name) => {
        const b = [...document.querySelectorAll("#tabs button, #sheetlist button")]
          .find((x) => (x.textContent || "").trim() === name);
        if (b) b.click();
      }, v);
      await pg.waitForTimeout(220);
      await sweep(pg, width, `view "${v}"`);
    }

    /* the state the chairman was actually in: an agent panel open */
    await pg.evaluate(() => {
      const b = [...document.querySelectorAll("#tabs button")]
        .find((x) => /Office/.test(x.textContent || ""));
      if (b) b.click();
    });
    await pg.waitForTimeout(220);
    for (const who of ["ceo", "apify"]) {
      await pg.evaluate((id) => {
        const s = document.querySelector(`[data-a="${id}"]`);
        if (s) s.dispatchEvent(new MouseEvent("click", { bubbles: true }));
      }, who);
      await pg.waitForTimeout(300);
      for (const tab of ["Chat", "Status", "Performance"]) {
        await pg.evaluate((t) => {
          const b = [...document.querySelectorAll("#ptabs button")]
            .find((x) => (x.textContent || "").trim() === t);
          if (b) b.click();
        }, tab);
        await pg.waitForTimeout(200);
        await sweep(pg, width, `${who} panel, ${tab} tab`);
      }
      await pg.evaluate(() => document.getElementById("pclose").click());
      await pg.waitForTimeout(250);
    }

    /* links: none may ask for a new tab, and the printed address must be the href */
    const links = await pg.evaluate(() => {
      const out = { targeted: [], mismatched: [], cards: 0 };
      document.querySelectorAll("a[href^='http']").forEach((a) => {
        if (a.getAttribute("target")) out.targeted.push(a.getAttribute("href").slice(0, 60));
      });
      document.querySelectorAll(".pcard").forEach((c) => {
        out.cards++;
        const a = c.querySelector("a.prow"), u = c.querySelector(".paddr .u");
        if (!a || !u || a.getAttribute("href") !== u.textContent.trim())
          out.mismatched.push((a && a.getAttribute("href")) || "(none)");
      });
      return out;
    });
    links.targeted.forEach((h) =>
      fail(`${width}px: ${h} asks for a new tab. A home-screen app drops those silently ` +
           `and the tap does nothing at all (KB-174).`));
    links.mismatched.forEach((h) =>
      fail(`${width}px: product card ${h} prints an address that is not its link.`));
    if (!links.cards) fail(`${width}px: no product cards on the page at all.`);
    jsErrors.forEach((e) => fail(`${width}px: script error -- ${e}`));
    await pg.close();
  }

  await browser.close();
  srv.close();

  if (fontsLoaded < 4)
    console.log(`NOTE: only ${fontsLoaded} webfaces loaded, so widths were measured with ` +
                `fallback fonts, which are narrower than the real ones. Treat a pass as weaker ` +
                `than it looks.`);

  if (problems.length) {
    problems.forEach((p) => console.error("FAIL: " + p));
    console.error(`\nRefusing to sign off the office page: ${problems.length} problem(s). ` +
                  `This runs the states the chairman actually uses, because the checks that ` +
                  `did not (KB-174, KB-175) passed a page whose links were all dead.`);
    process.exit(1);
  }
  console.log(`OK: ${WIDTHS.join(", ")}px -- every view, both panels, all three panel tabs, ` +
              `${fontsLoaded} webfaces loaded. Nothing overflows, no link asks for a new tab, ` +
              `every printed address matches its link.`);
})();
