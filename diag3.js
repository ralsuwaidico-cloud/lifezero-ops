const {chromium}=require('playwright');
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',
    args:['--proxy-server='+(process.env.HTTPS_PROXY||'').replace(/^https?:\/\//,''),'--ignore-certificate-errors']});
  const pg=await b.newPage({viewport:{width:390,height:844}});
  const loaded=[];
  pg.on('response',r=>{if(/fonts\.(googleapis|gstatic)/.test(r.url())) loaded.push(r.status()+' '+r.url().slice(0,60));});
  await pg.goto('http://127.0.0.1:8931/office.html',{waitUntil:'networkidle'});
  await pg.waitForTimeout(1500);
  const fonts=await pg.evaluate(()=>document.fonts?[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+' '+f.weight).slice(0,8):[]);
  console.log('font responses:',loaded.length); loaded.slice(0,4).forEach(x=>console.log('  ',x));
  console.log('loaded faces:',JSON.stringify(fonts));
  await pg.evaluate(()=>{const s=document.querySelector('[data-a="ceo"]'); s.dispatchEvent(new MouseEvent('click',{bubbles:true}));});
  await pg.waitForTimeout(600);
  const r=await pg.evaluate(()=>{
    const vw=document.documentElement.clientWidth, bad=[];
    document.querySelectorAll('*').forEach(el=>{
      const b=el.getBoundingClientRect(); if(!b.width) return;
      if(b.right>vw+1||b.left<-1){
        let p=el.parentElement,sc=false;
        while(p){const s=getComputedStyle(p); if(s.overflowX==='auto'||s.overflowX==='scroll'){sc=true;break;} p=p.parentElement;}
        if(!sc) bad.push(el.tagName.toLowerCase()+'.'+(el.className||'').toString().slice(0,30)+' r='+Math.round(b.right)+' w='+Math.round(b.width)+' "'+(el.textContent||'').trim().slice(0,22)+'"');
      }
    });
    return {vw, scrollW:document.documentElement.scrollWidth, n:bad.length, bad:bad.slice(0,14)};
  });
  console.log('clientWidth',r.vw,'scrollWidth',r.scrollW,'offenders',r.n);
  r.bad.forEach(x=>console.log('   ',x));
  await pg.screenshot({path:'real-fonts-panel.png'});
  await b.close();
})();
