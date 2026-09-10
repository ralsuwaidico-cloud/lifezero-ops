"""Build script for Reseller Inventory & Profit Tracker 2026.
Run:  python3 build.py   (requires openpyxl only). Then recalculate with LibreOffice/recalc.py."""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule
from openpyxl.utils import get_column_letter
from openpyxl.comments import Comment
from datetime import date

OUT = "/home/claude/products/reseller-tracker/Reseller_Inventory_Profit_Tracker_2026.xlsx"
N = 503          # last data row (rows 4..503 = 500 rows)
FIRST = 4
ACCENT = "1F3A5F"
TINT = "E9EEF5"
TINT2 = "F5F7FA"
BLUE = "0000FF"
FONT = "Arial"

f = lambda **k: Font(name=FONT, **k)
hdr_font = f(bold=True, color="FFFFFF", size=10)
hdr_fill = PatternFill("solid", fgColor=ACCENT)
tint_fill = PatternFill("solid", fgColor=TINT)
tint2_fill = PatternFill("solid", fgColor=TINT2)
thin = Side(style="thin", color="BFC7D1")
border = Border(left=thin, right=thin, top=thin, bottom=thin)
CUR = '$#,##0.00;($#,##0.00);"-"'
PCT = '0.0%'
DATE = 'mm/dd/yyyy'
INT = '#,##0;(#,##0);"-"'

wb = Workbook()

def title(ws, text, sub=None):
    ws["A1"] = text
    ws["A1"].font = f(bold=True, size=16, color=ACCENT)
    if sub:
        ws["A2"] = sub
        ws["A2"].font = f(italic=True, size=9, color="666666")

def header(ws, row, headers, start_col=1):
    for i, h in enumerate(headers):
        c = ws.cell(row=row, column=start_col + i, value=h)
        c.font = hdr_font; c.fill = hdr_fill; c.border = border
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[row].height = 30

def widths(ws, w):
    for i, x in enumerate(w, 1):
        ws.column_dimensions[get_column_letter(i)].width = x

# ---------------------------------------------------------------- START HERE
ws = wb.active; ws.title = "START HERE"
title(ws, "Reseller Inventory & Profit Tracker 2026",
      "For eBay - Poshmark - Mercari - Depop - Whatnot - Facebook Marketplace - Etsy sellers")
rows = [
    ("HOW TO USE", None),
    ("1", "Settings: review platform fee rates (pre-filled approximations - verify against each platform's current fee page) and set your mileage rate, stale-item threshold and year start date."),
    ("2", "Inventory: log every item you buy, one per row. SKU is auto-generated when you enter a purchase date (you can overwrite it with your own code). Set Status to Listed and add the Date Listed when it goes live."),
    ("3", "Sales: when an item sells, enter the Date Sold, SKU, Platform, Sale Price and shipping details. Description, cost, fees, profit, ROI and days-to-sell are calculated for you. Remember to change the item's Status to Sold on the Inventory sheet."),
    ("4", "Expenses: record business costs not tied to one item (supplies, subscriptions, storage, mileage). Enter miles in the Miles column and the deduction is calculated at your Settings rate."),
    ("5", "Dashboard, Death Pile and Tax Summary update automatically. Nothing needs to be typed on those sheets."),
    ("", ""),
    ("LEGEND", None),
    ("BLUE text", "Cells you type into (inputs). Dropdowns are provided where a list is expected."),
    ("BLACK text", "Formulas - do not overwrite. If you accidentally delete one, copy the cell above it and paste down."),
    ("Grey 'helper' columns", "Support the Dashboard and Death Pile lookups. Leave them in place; you may hide them."),
    ("", ""),
    ("SAMPLE DATA", None),
    ("Delete before use", "Inventory, Sales and Expenses contain sample rows (Patagonia fleece, Pyrex, Nike etc.) so you can see how the tracker works. Select those rows and press Delete (clear contents) - do not delete whole rows, because SKUs are numbered by row position and formulas run down to row 503."),
    ("Rows supported", "500 inventory items, 500 sales and 500 expense lines per copy. Start a fresh copy of the file each year (change the Year Start Date in Settings)."),
    ("", ""),
    ("TIPS", None),
    ("Sell-through rate", "Items sold / items sourced this year. Full-time flippers typically aim for 30%+ per quarter."),
    ("Death Pile", "Any Listed item older than the stale threshold (default 60 days) is flagged. Reprice, bundle, or relist it."),
    ("Fee accuracy", "Fees are estimates using the Settings table. Promoted listings, store subscriptions and international fees are not modelled - add them to Other Costs on the Sales row."),
    ("Check the fee rates", "Platforms change their fees without much notice, and a wrong rate quietly distorts every profit and ROI figure in this workbook. The 'Rates last checked' column in Settings tells you which rows have been verified and which have not - the honest answer is that most say 'not re-verified'. Spend five minutes against each platform's current fee page before you trust the numbers, and update Settings; everything else recalculates."),
    ("", ""),
    ("DISCLAIMER", None),
    ("Not tax advice", "This workbook is a bookkeeping aid only. The Tax Summary is an estimate mapped loosely to US Schedule C categories and is not a substitute for advice from a qualified tax professional. Fee rates and the mileage rate are user-editable approximations - verify them for your situation."),
]
r = 4
for a, b in rows:
    if b is None:
        c = ws.cell(row=r, column=1, value=a); c.font = f(bold=True, color="FFFFFF", size=11); c.fill = hdr_fill
        ws.cell(row=r, column=2).fill = hdr_fill
    else:
        ca = ws.cell(row=r, column=1, value=a); ca.font = f(bold=True, size=10, color=ACCENT)
        if a == "BLUE text": ca.font = f(bold=True, size=10, color=BLUE)
        if a == "Grey 'helper' columns": ca.font = f(bold=True, size=10, color="808080")
        cb = ws.cell(row=r, column=2, value=b); cb.font = f(size=10)
        cb.alignment = Alignment(wrap_text=True, vertical="top"); ca.alignment = Alignment(vertical="top")
    r += 1
widths(ws, [24, 110])
ws.sheet_view.showGridLines = False

# ---------------------------------------------------------------- SETTINGS
st = wb.create_sheet("Settings")
title(st, "Settings", "Blue cells are yours to edit. All other sheets read from here.")
header(st, 3, ["Platform", "Fee %", "Fixed Fee / Sale", "Payment Processing %", "Fee on Buyer Shipping? (Y/N)", "Notes - verify against the platform's current fee page", "Rates last checked"])
# Fee structures change without notice and a wrong rate silently corrupts every profit figure,
# so each row records when its rates were last checked rather than implying all are current.
CHECKED = {"Mercari": "2026-09-10"}
platforms = [
    ("eBay", 0.136, 0.40, 0.0, "Y", "Final value fee ~13.6% of total incl. shipping + $0.40 per order (most categories)."),
    ("Poshmark", 0.20, 0.0, 0.0, "N", "20% of sale price at/over the threshold below; flat fee under it. Buyer pays shipping."),
    ("Mercari", 0.10, 0.0, 0.0, "Y", "Flat 10% on item + buyer-paid shipping. The separate 2.9% + $0.50 seller payment-processing fee was removed on 6 Jan 2025; buyers now pay a 3.6% Buyer Protection fee instead."),
    ("Depop", 0.0, 0.45, 0.033, "Y", "US selling fee moved to buyer; ~3.3% + $0.45 payment processing remains."),
    ("Whatnot", 0.08, 0.30, 0.029, "N", "8% commission + 2.9% + $0.30 processing."),
    ("FB Marketplace", 0.10, 0.0, 0.0, "Y", "~10% selling fee on shipped checkout orders; local cash sales = 0%."),
    ("Etsy", 0.065, 0.45, 0.03, "Y", "6.5% transaction + 3% + $0.25 processing + $0.20 listing fee."),
    ("Other", 0.10, 0.0, 0.0, "N", "Generic placeholder - edit for any other marketplace."),
]
for i, p in enumerate(platforms):
    rr = 4 + i
    for j, v in enumerate(p):
        c = st.cell(row=rr, column=1 + j, value=v)
        c.font = f(color=BLUE if j < 5 else "666666", size=10, italic=(j == 5)); c.border = border
    st.cell(row=rr, column=2).number_format = PCT
    st.cell(row=rr, column=3).number_format = CUR
    st.cell(row=rr, column=4).number_format = PCT
    st.cell(row=rr, column=5).alignment = Alignment(horizontal="center")
    checked = CHECKED.get(p[0], "not re-verified")
    c = st.cell(row=rr, column=7, value=checked)
    c.font = f(size=9, italic=True, color="9C0006" if checked == "not re-verified" else "006100")
    c.alignment = Alignment(horizontal="center"); c.border = border
dv_yn = DataValidation(type="list", formula1='"Y,N"', allow_blank=True); st.add_data_validation(dv_yn); dv_yn.add("E4:E11")

header(st, 13, ["General Setting", "Value", "Notes"])
st.merge_cells("C13:F13")
general = [
    ("Currency Symbol", "$", "Used in Dashboard labels. Number formats use $ - change via Format Cells if needed.", None),
    ("Year Start Date", date(2026, 1, 1), "Dashboard months run 12 months from this date.", DATE),
    ("Sales Tax Rate (optional)", 0.0, "Only if you collect tax yourself (e.g. local cash sales). Marketplaces remit tax for you.", PCT),
    ("Mileage Rate (per mile)", 0.70, "IRS standard mileage rate - 2026 default of 70 cents entered; verify the current rate at irs.gov.", '$0.000'),
    ("Default Shipping Cost", 9.00, "Reference figure for quick estimates when pricing.", CUR),
    ("Stale Item Threshold (days)", 60, "Listed items older than this are flagged on the Death Pile.", '0'),
    ("Poshmark Flat-Fee Threshold", 15.00, "Sales below this price pay the flat fee instead of the % fee.", CUR),
    ("Poshmark Flat Fee", 2.95, "Flat fee charged on sales below the threshold.", CUR),
]
for i, (lab, val, note, fmt) in enumerate(general):
    rr = 14 + i
    a = st.cell(row=rr, column=1, value=lab); a.font = f(bold=True, size=10); a.border = border
    b = st.cell(row=rr, column=2, value=val); b.font = f(color=BLUE, size=10); b.border = border
    if fmt: b.number_format = fmt
    c = st.cell(row=rr, column=3, value=note); c.font = f(italic=True, size=10, color="666666")
    st.merge_cells(start_row=rr, start_column=3, end_row=rr, end_column=6)
S_CUR, S_START, S_TAX, S_MILE, S_SHIP, S_STALE, S_PTHR, S_PFLAT = [f"Settings!$B${14+i}" for i in range(8)]

header(st, 3, ["Sources", "Categories", "Statuses", "Expense Categories"], start_col=8)
sources = ["Thrift", "Estate Sale", "Garage Sale", "Auction", "Online", "Wholesale", "Other"]
categories = ["Clothing", "Shoes", "Accessories", "Electronics", "Home", "Toys", "Books & Media", "Collectibles", "Other"]
statuses = ["Sourced", "Listed", "Sold", "Returned", "Donated"]
expcats = ["Supplies", "Shipping Supplies", "Mileage", "Subscriptions", "Storage", "Fees", "Other"]
for col, lst in zip([8, 9, 10, 11], [sources, categories, statuses, expcats]):
    for i, v in enumerate(lst):
        c = st.cell(row=4 + i, column=col, value=v); c.font = f(color=BLUE, size=10); c.border = border
st.cell(row=14, column=8, value="Lists feed the dropdowns on other sheets. Edit names here (keep the Statuses list as-is; formulas depend on it).").font = f(italic=True, size=9, color="666666")
widths(st, [30, 12, 16, 20, 24, 70, 16, 16, 12, 20])
st.sheet_view.showGridLines = False
PLAT_RNG = "Settings!$A$4:$A$11"
SRC_RNG = "Settings!$H$4:$H$10"
CAT_RNG = "Settings!$I$4:$I$12"
STAT_RNG = "Settings!$J$4:$J$8"
EXP_RNG = "Settings!$K$4:$K$10"

# ---------------------------------------------------------------- INVENTORY
inv = wb.create_sheet("Inventory")
title(inv, "Inventory", "One row per item. Blue = type, black = formula. Clear (don't delete) the sample rows before use.")
inv_h = ["SKU", "Date Purchased", "Source", "Brand", "Item Description", "Category", "Size", "Cost of Goods",
         "Extra Costs (cleaning/repair)", "Total Cost", "Status", "Date Listed", "List Price", "Platform Listed",
         "Days in Inventory", "Days Listed", "Stale?", "Stale # (helper)"]
header(inv, 3, inv_h)
inv.cell(row=3, column=18).font = f(bold=True, color="D0D0D0", size=10)
sample_inv = [
    (date(2026,1,12), "Thrift", "Patagonia", "Men's Better Sweater Fleece Full-Zip, Navy", "Clothing", "L", 12.99, 0, "Sold", date(2026,1,15), 79.00, "eBay"),
    (date(2026,1,20), "Estate Sale", "Pyrex", "Vintage Butterfly Gold Mixing Bowl Set (3 pc)", "Home", "", 18.00, 2.50, "Sold", date(2026,1,22), 65.00, "Mercari"),
    (date(2026,2,3), "Thrift", "Nike", "Air Max 90 Sneakers, White/Grey", "Shoes", "10", 22.00, 4.00, "Sold", date(2026,2,5), 68.00, "Poshmark"),
    (date(2026,2,14), "Garage Sale", "Gap Kids", "Denim Trucker Jacket, Medium Wash", "Clothing", "M (8)", 3.00, 0, "Sold", date(2026,2,16), 14.00, "Poshmark"),
    (date(2026,3,2), "Online", "LEGO", "Creator Expert 10265 Ford Mustang (sealed)", "Toys", "", 45.00, 0, "Sold", date(2026,3,4), 95.00, "Whatnot"),
    (date(2026,3,18), "Thrift", "Carhartt", "Detroit Jacket, Duck Canvas, Brown", "Clothing", "XL", 24.99, 6.00, "Listed", date(2026,3,20), 145.00, "eBay"),
    (date(2026,6,5), "Auction", "Sony", "Walkman WM-F41 Cassette Player (tested)", "Electronics", "", 30.00, 0, "Listed", date(2026,8,20), 89.00, "eBay"),
    (date(2026,8,28), "Wholesale", "Lululemon", "Align High-Rise Leggings 25\", Black", "Clothing", "6", 20.00, 0, "Sourced", None, None, ""),
]
for r in range(FIRST, N + 1):
    inv[f"A{r}"] = f'=IF(B{r}="","","SKU-"&TEXT(ROW()-{FIRST-1},"0000"))'
    inv[f"J{r}"] = f'=IF(B{r}="","",N(H{r})+N(I{r}))'
    inv[f"O{r}"] = f'=IF(OR(B{r}="",K{r}="Sold",K{r}="Donated"),"",TODAY()-B{r})'
    inv[f"P{r}"] = f'=IF(OR(L{r}="",K{r}="Sold",K{r}="Donated"),"",TODAY()-L{r})'
    inv[f"Q{r}"] = f'=IF(AND(K{r}="Listed",P{r}<>"",N(P{r})>{S_STALE}),"STALE","")'
    inv[f"R{r}"] = f'=IF(Q{r}="STALE",COUNTIF($Q${FIRST}:Q{r},"STALE"),"")'
    if r - FIRST < len(sample_inv):
        vals = sample_inv[r - FIRST]
        for col, v in zip("BCDEFGHIKLMN", vals):
            if v not in (None, ""): inv[f"{col}{r}"] = v
    for col in "BCDEFGHIKLMN":
        c = inv[f"{col}{r}"]; c.font = f(color=BLUE, size=10); c.border = border
    for col in "AJOPQ":
        c = inv[f"{col}{r}"]; c.font = f(size=10); c.border = border
    inv[f"R{r}"].font = f(size=9, color="A0A0A0")
    inv[f"B{r}"].number_format = DATE; inv[f"L{r}"].number_format = DATE
    for col in "HIJM": inv[f"{col}{r}"].number_format = CUR
    for col in "OP": inv[f"{col}{r}"].number_format = INT
    inv[f"Q{r}"].alignment = Alignment(horizontal="center")
for rng, lst in [(f"C{FIRST}:C{N}", SRC_RNG), (f"F{FIRST}:F{N}", CAT_RNG), (f"K{FIRST}:K{N}", STAT_RNG), (f"N{FIRST}:N{N}", PLAT_RNG)]:
    dv = DataValidation(type="list", formula1=f"={lst}", allow_blank=True); inv.add_data_validation(dv); dv.add(rng)
inv.conditional_formatting.add(f"A{FIRST}:Q{N}", FormulaRule(formula=[f'$Q{FIRST}="STALE"'], fill=PatternFill("solid", fgColor="FDE9D9"), font=Font(name=FONT, color="9C0006")))
inv.conditional_formatting.add(f"K{FIRST}:K{N}", FormulaRule(formula=[f'$K{FIRST}="Sold"'], fill=PatternFill("solid", fgColor="E2F0D9")))
widths(inv, [11, 13, 13, 14, 40, 13, 9, 12, 14, 12, 11, 12, 11, 15, 11, 10, 9, 9])
inv.freeze_panes = "C4"
inv.auto_filter.ref = f"A3:R{N}"
inv["A1"].comment = Comment("SKU is generated from the row number. You may type your own SKU over it, but keep it unique - Sales looks items up by SKU.", "Tracker")

# ---------------------------------------------------------------- SALES
sa = wb.create_sheet("Sales")
title(sa, "Sales", "Enter Date Sold, SKU, Platform, Sale Price and shipping. Everything else is calculated. Fees follow the Settings table.")
sa_h = ["Date Sold", "SKU", "Item Description", "Platform", "Sale Price", "Shipping Charged to Buyer", "Shipping Cost Paid",
        "Platform Fees (est.)", "Sales Tax Collected by Platform (info)", "Other Costs", "Item Total Cost", "Net Profit", "ROI %",
        "Days to Sell", "Category (helper)", "Source (helper)"]
header(sa, 3, sa_h)
sample_sales = [
    (date(2026,1,28), "SKU-0001", "eBay", 79.00, 0, 9.85, 5.53, 0),
    (date(2026,2,10), "SKU-0002", "Mercari", 65.00, 12.99, 14.20, 5.85, 1.50),
    (date(2026,2,21), "SKU-0003", "Poshmark", 68.00, 0, 0, 0, 0),
    (date(2026,3,1), "SKU-0004", "Poshmark", 14.00, 0, 0, 0, 0),
    (date(2026,4,25), "SKU-0005", "Whatnot", 95.00, 8.00, 11.40, 7.60, 0),
]
INV_A = f"Inventory!$A${FIRST}:$A${N}"
def invcol(col): return f"Inventory!${col}${FIRST}:${col}${N}"
for r in range(FIRST, N + 1):
    m = f"MATCH($B{r},{INV_A},0)"
    sa[f"C{r}"] = f'=IF($B{r}="","",IFERROR(INDEX({invcol("E")},{m}),"SKU not found"))'
    pm = f"MATCH($D{r},{PLAT_RNG},0)"
    base = f'(E{r}+IF(INDEX(Settings!$E$4:$E$11,{pm})="Y",N(F{r}),0))'
    sa[f"H{r}"] = (f'=IF(OR(B{r}="",D{r}="",E{r}=""),"",IFERROR(IF(AND(D{r}="Poshmark",E{r}<{S_PTHR}),{S_PFLAT},'
                   f'{base}*(INDEX(Settings!$B$4:$B$11,{pm})+INDEX(Settings!$D$4:$D$11,{pm}))+INDEX(Settings!$C$4:$C$11,{pm})),0))')
    sa[f"K{r}"] = f'=IF($B{r}="","",IFERROR(INDEX({invcol("J")},{m}),0))'
    sa[f"L{r}"] = f'=IF(OR(B{r}="",E{r}=""),"",E{r}+N(F{r})-N(G{r})-N(H{r})-N(J{r})-N(K{r}))'
    sa[f"M{r}"] = f'=IF(OR(L{r}="",N(K{r})=0),"",L{r}/K{r})'
    sa[f"N{r}"] = f'=IF(OR(A{r}="",B{r}=""),"",IFERROR(A{r}-INDEX({invcol("B")},{m}),""))'
    sa[f"O{r}"] = f'=IF($B{r}="","",IFERROR(INDEX({invcol("F")},{m}),""))'
    sa[f"P{r}"] = f'=IF($B{r}="","",IFERROR(INDEX({invcol("C")},{m}),""))'
    if r - FIRST < len(sample_sales):
        for col, v in zip("ABDEFGIJ", sample_sales[r - FIRST]): sa[f"{col}{r}"] = v
    for col in "ABDEFGIJ":
        c = sa[f"{col}{r}"]; c.font = f(color=BLUE, size=10); c.border = border
    for col in "CHKLMN":
        c = sa[f"{col}{r}"]; c.font = f(size=10); c.border = border
    for col in "OP": sa[f"{col}{r}"].font = f(size=9, color="A0A0A0")
    sa[f"A{r}"].number_format = DATE
    for col in "EFGHIJKL": sa[f"{col}{r}"].number_format = CUR
    sa[f"M{r}"].number_format = PCT; sa[f"N{r}"].number_format = INT
dv = DataValidation(type="list", formula1=f"={PLAT_RNG}", allow_blank=True); sa.add_data_validation(dv); dv.add(f"D{FIRST}:D{N}")
sa.conditional_formatting.add(f"L{FIRST}:L{N}", FormulaRule(formula=[f'AND(ISNUMBER($L{FIRST}),$L{FIRST}<0)'], font=Font(name=FONT, color="9C0006", bold=True), fill=PatternFill("solid", fgColor="FDE9D9")))
sa.conditional_formatting.add(f"C{FIRST}:C{N}", FormulaRule(formula=[f'$C{FIRST}="SKU not found"'], font=Font(name=FONT, color="9C0006", bold=True)))
# A platform that is not in the Settings table makes the fee lookup fail, and the IFERROR above
# turns that into a $0 fee - which silently overstates profit and ROI. Flag the cell instead.
sa.conditional_formatting.add(f"D{FIRST}:D{N}", FormulaRule(
    # INDIRECT keeps this working in Google Sheets, which rejects direct cross-sheet
    # references inside a conditional-formatting custom formula.
    formula=[f'AND($D{FIRST}<>"",ISNA(MATCH($D{FIRST},INDIRECT("{PLAT_RNG}"),0)))'],
    font=Font(name=FONT, color="9C0006", bold=True), fill=PatternFill("solid", fgColor="FDE9D9")))
widths(sa, [12, 11, 40, 14, 11, 13, 12, 12, 14, 11, 12, 12, 9, 9, 12, 12])
sa.freeze_panes = "C4"
sa.auto_filter.ref = f"A3:P{N}"
sa["H3"].comment = Comment("Fee = (Sale Price [+ buyer shipping if flagged Y in Settings]) x (Fee % + Processing %) + Fixed Fee. Poshmark sales under the threshold pay the flat fee. Edit rates in Settings.", "Tracker")

# ---------------------------------------------------------------- EXPENSES
ex = wb.create_sheet("Expenses")
title(ex, "Expenses", "Business costs not tied to one item. For mileage, enter Miles and the deduction is calculated from Settings.")
header(ex, 3, ["Date", "Category", "Description", "Amount", "Miles", "Mileage Deduction", "Total Deductible"])
sample_exp = [
    (date(2026,1,5), "Shipping Supplies", "Poly mailers 10x13 (100 pk) + tape", 24.99, None),
    (date(2026,1,15), "Mileage", "Thrift route - 3 stores", None, 32),
    (date(2026,2,1), "Subscriptions", "Crosslisting app - monthly", 19.99, None),
    (date(2026,3,10), "Supplies", "Garment steamer + lint roller", 38.50, None),
]
for r in range(FIRST, N + 1):
    ex[f"F{r}"] = f'=IF(E{r}="","",E{r}*{S_MILE})'
    ex[f"G{r}"] = f'=IF(A{r}="","",N(D{r})+N(F{r}))'
    if r - FIRST < len(sample_exp):
        for col, v in zip("ABCDE", sample_exp[r - FIRST]):
            if v is not None: ex[f"{col}{r}"] = v
    for col in "ABCDE":
        c = ex[f"{col}{r}"]; c.font = f(color=BLUE, size=10); c.border = border
    for col in "FG":
        c = ex[f"{col}{r}"]; c.font = f(size=10); c.border = border
    ex[f"A{r}"].number_format = DATE
    for col in "DFG": ex[f"{col}{r}"].number_format = CUR
    ex[f"E{r}"].number_format = '#,##0.0'
dv = DataValidation(type="list", formula1=f"={EXP_RNG}", allow_blank=True); ex.add_data_validation(dv); dv.add(f"B{FIRST}:B{N}")
widths(ex, [12, 18, 42, 12, 10, 16, 16])
ex.freeze_panes = "A4"
ex.auto_filter.ref = f"A3:G{N}"

# ---------------------------------------------------------------- DASHBOARD
db = wb.create_sheet("Dashboard")
title(db, "Dashboard")
db["A2"] = f'="Tracking year starting "&TEXT({S_START},"mmm d, yyyy")&"  -  updates automatically"'
db["A2"].font = f(italic=True, size=9, color="666666")
db.sheet_view.showGridLines = False

def SR(sheet, col): return f"{sheet}!${col}${FIRST}:${col}${N}"
inv_stat = SR("Inventory", "K"); inv_cost = SR("Inventory", "J")
PT0, CT0, ST0 = 28, 39, 51
tiles = [
    ("A4", f'="Inventory Value at Cost (Unsold, "&{S_CUR}&")"',
     f'=SUMIFS({inv_cost},{inv_stat},"Sourced")+SUMIFS({inv_cost},{inv_stat},"Listed")+SUMIFS({inv_cost},{inv_stat},"Returned")', CUR),
    ("C4", "Sell-Through Rate", f'=IFERROR(COUNTIF({inv_stat},"Sold")/COUNTIF({inv_stat},"?*"),0)', PCT),
    ("E4", f'="Avg Profit per Item ("&{S_CUR}&")"', f'=IFERROR(AVERAGE({SR("Sales","L")}),0)', CUR),
    ("G4", "Avg ROI", f'=IFERROR(AVERAGE({SR("Sales","M")}),0)', PCT),
    ("I4", "Avg Days to Sell", f'=IFERROR(AVERAGE({SR("Sales","N")}),0)', '0.0'),
    ("A7", "Best Platform by Profit", f'=IFERROR(IF(MAX(E{PT0}:E{PT0+7})=0,"-",INDEX(A{PT0}:A{PT0+7},MATCH(MAX(E{PT0}:E{PT0+7}),E{PT0}:E{PT0+7},0))),"-")', None),
    ("C7", "Death Pile Items (stale)", f'=COUNTIF({SR("Inventory","Q")},"STALE")', INT),
    ("E7", f'="Death Pile Cost ("&{S_CUR}&")"', f'=SUMIFS({inv_cost},{SR("Inventory","Q")},"STALE")', CUR),
    ("G7", "Items Sold (year)", f'=D24', INT),
    ("I7", f'="Net Profit (year, "&{S_CUR}&")"', f'=J24', CUR),
]
for anchor, label, formula, fmt in tiles:
    col = anchor[0]; row = int(anchor[1:])
    c2 = get_column_letter(ord(col) - 64 + 1)
    db.merge_cells(f"{col}{row}:{c2}{row}"); db.merge_cells(f"{col}{row+1}:{c2}{row+1}")
    lc = db[f"{col}{row}"]; lc.value = label; lc.font = f(size=9, color="FFFFFF", bold=True); lc.fill = hdr_fill
    lc.alignment = Alignment(horizontal="center", vertical="center")
    vc = db[f"{col}{row+1}"]; vc.value = formula; vc.font = f(size=16, bold=True, color=ACCENT); vc.fill = tint_fill
    vc.alignment = Alignment(horizontal="center", vertical="center")
    if fmt: vc.number_format = fmt
    db.row_dimensions[row + 1].height = 34
    for cc in (col, c2):
        for rr in (row, row + 1): db[f"{cc}{rr}"].border = border

db["A10"] = "Monthly Performance"; db["A10"].font = f(bold=True, size=12, color=ACCENT)
header(db, 11, ["Month", "Items Sourced", "COGS Spent", "Items Sold", "Gross Sales", "Fees", "Shipping Net (charged - paid)",
                "Item Profit", "Overhead Expenses", "Net Profit", "", "Month Start (helper)", "Month End (helper)"])
db["K11"].fill = PatternFill(None); db["K11"].border = Border()
for c in ("L11", "M11"): db[c].font = f(bold=True, color="D0D0D0", size=9)
for i in range(12):
    r = 12 + i
    db[f"L{r}"] = f'=DATE(YEAR({S_START}),MONTH({S_START})+{i},1)'
    db[f"M{r}"] = f'=DATE(YEAR({S_START}),MONTH({S_START})+{i+1},1)'
    lo, hi = f'">="&$L{r}', f'"<"&$M{r}'
    db[f"A{r}"] = f'=TEXT(L{r},"mmm yyyy")'
    db[f"B{r}"] = f'=COUNTIFS({SR("Inventory","B")},{lo},{SR("Inventory","B")},{hi})'
    db[f"C{r}"] = f'=SUMIFS({inv_cost},{SR("Inventory","B")},{lo},{SR("Inventory","B")},{hi})'
    db[f"D{r}"] = f'=COUNTIFS({SR("Sales","A")},{lo},{SR("Sales","A")},{hi})'
    db[f"E{r}"] = f'=SUMIFS({SR("Sales","E")},{SR("Sales","A")},{lo},{SR("Sales","A")},{hi})'
    db[f"F{r}"] = f'=SUMIFS({SR("Sales","H")},{SR("Sales","A")},{lo},{SR("Sales","A")},{hi})'
    db[f"G{r}"] = f'=SUMIFS({SR("Sales","F")},{SR("Sales","A")},{lo},{SR("Sales","A")},{hi})-SUMIFS({SR("Sales","G")},{SR("Sales","A")},{lo},{SR("Sales","A")},{hi})'
    db[f"H{r}"] = f'=SUMIFS({SR("Sales","L")},{SR("Sales","A")},{lo},{SR("Sales","A")},{hi})'
    db[f"I{r}"] = f'=SUMIFS({SR("Expenses","G")},{SR("Expenses","A")},{lo},{SR("Expenses","A")},{hi})'
    # Net Profit = Item Profit (H) - Overhead (I). G is Shipping Net, which is already
    # inside H via Sales!L - subtracting overhead from it reported a loss on a profitable year.
    db[f"J{r}"] = f'=H{r}-I{r}'
    for col in "ABCDEFGHIJ":
        c = db[f"{col}{r}"]; c.font = f(size=10); c.border = border
        if i % 2: c.fill = tint2_fill
    for col in "LM": db[f"{col}{r}"].number_format = DATE; db[f"{col}{r}"].font = f(size=9, color="A0A0A0")
    for col in "BD": db[f"{col}{r}"].number_format = INT
    for col in "CEFGHIJ": db[f"{col}{r}"].number_format = CUR
db["A24"] = "TOTAL"
for col in "BCDEFGHIJ": db[f"{col}24"] = f"=SUM({col}12:{col}23)"
for col in "ABCDEFGHIJ":
    c = db[f"{col}24"]; c.font = f(bold=True, size=10); c.fill = tint_fill; c.border = Border(top=Side(style="medium", color=ACCENT), bottom=thin, left=thin, right=thin)
    if col in "BD": c.number_format = INT
    elif col != "A": c.number_format = CUR
db.conditional_formatting.add("J12:J24", FormulaRule(formula=['AND(ISNUMBER(J12),J12<0)'], font=Font(name=FONT, color="9C0006", bold=True)))

db[f"A{PT0-2}"] = "Performance by Platform"; db[f"A{PT0-2}"].font = f(bold=True, size=12, color=ACCENT)
header(db, PT0 - 1, ["Platform", "Items Sold", "Gross Sales", "Fees", "Net Profit", "Avg Profit / Item", "Avg ROI"])
for i in range(8):
    r = PT0 + i
    db[f"A{r}"] = f"=Settings!A{4+i}"
    db[f"B{r}"] = f'=COUNTIFS({SR("Sales","D")},$A{r},{SR("Sales","E")},"<>")'
    db[f"C{r}"] = f'=SUMIFS({SR("Sales","E")},{SR("Sales","D")},$A{r})'
    db[f"D{r}"] = f'=SUMIFS({SR("Sales","H")},{SR("Sales","D")},$A{r})'
    db[f"E{r}"] = f'=SUMIFS({SR("Sales","L")},{SR("Sales","D")},$A{r})'
    db[f"F{r}"] = f'=IF(B{r}=0,0,E{r}/B{r})'
    db[f"G{r}"] = f'=IFERROR(E{r}/SUMIFS({SR("Sales","K")},{SR("Sales","D")},$A{r}),0)'
    for col in "ABCDEFG":
        c = db[f"{col}{r}"]; c.font = f(size=10); c.border = border
        if i % 2: c.fill = tint2_fill
    db[f"B{r}"].number_format = INT
    for col in "CDEF": db[f"{col}{r}"].number_format = CUR
    db[f"G{r}"].number_format = PCT
db.conditional_formatting.add(f"A{PT0}:G{PT0+7}", FormulaRule(formula=[f'AND(MAX($E${PT0}:$E${PT0+7})>0,$E{PT0}=MAX($E${PT0}:$E${PT0+7}))'], font=Font(name=FONT, bold=True, color=ACCENT), fill=PatternFill("solid", fgColor="E2F0D9")))

db[f"A{CT0-2}"] = "Performance by Category"; db[f"A{CT0-2}"].font = f(bold=True, size=12, color=ACCENT)
header(db, CT0 - 1, ["Category", "Items Sourced", "Items Sold", "Cost Invested (all)", "Unsold at Cost", "Net Profit (sold)", "ROI (sold)"])
for i in range(9):
    r = CT0 + i
    db[f"A{r}"] = f"=Settings!I{4+i}"
    db[f"B{r}"] = f'=COUNTIFS({SR("Inventory","F")},$A{r},{SR("Inventory","B")},"<>")'
    db[f"C{r}"] = f'=COUNTIFS({SR("Sales","O")},$A{r},{SR("Sales","E")},"<>")'
    db[f"D{r}"] = f'=SUMIFS({inv_cost},{SR("Inventory","F")},$A{r})'
    db[f"E{r}"] = f'=D{r}-SUMIFS({inv_cost},{SR("Inventory","F")},$A{r},{inv_stat},"Sold")-SUMIFS({inv_cost},{SR("Inventory","F")},$A{r},{inv_stat},"Donated")'
    db[f"F{r}"] = f'=SUMIFS({SR("Sales","L")},{SR("Sales","O")},$A{r})'
    db[f"G{r}"] = f'=IFERROR(F{r}/SUMIFS({SR("Sales","K")},{SR("Sales","O")},$A{r}),0)'
    for col in "ABCDEFG":
        c = db[f"{col}{r}"]; c.font = f(size=10); c.border = border
        if i % 2: c.fill = tint2_fill
    for col in "BC": db[f"{col}{r}"].number_format = INT
    for col in "DEF": db[f"{col}{r}"].number_format = CUR
    db[f"G{r}"].number_format = PCT

db[f"A{ST0-2}"] = "ROI by Sourcing Channel"; db[f"A{ST0-2}"].font = f(bold=True, size=12, color=ACCENT)
header(db, ST0 - 1, ["Source", "Items Sourced", "Items Sold", "Sell-Through", "Cost of Items Sold", "Net Profit (sold)", "ROI (sold)"])
for i in range(7):
    r = ST0 + i
    db[f"A{r}"] = f"=Settings!H{4+i}"
    db[f"B{r}"] = f'=COUNTIFS({SR("Inventory","C")},$A{r},{SR("Inventory","B")},"<>")'
    db[f"C{r}"] = f'=COUNTIFS({SR("Sales","P")},$A{r},{SR("Sales","E")},"<>")'
    db[f"D{r}"] = f'=IF(B{r}=0,0,C{r}/B{r})'
    db[f"E{r}"] = f'=SUMIFS({SR("Sales","K")},{SR("Sales","P")},$A{r})'
    db[f"F{r}"] = f'=SUMIFS({SR("Sales","L")},{SR("Sales","P")},$A{r})'
    db[f"G{r}"] = f'=IF(E{r}=0,0,F{r}/E{r})'
    for col in "ABCDEFG":
        c = db[f"{col}{r}"]; c.font = f(size=10); c.border = border
        if i % 2: c.fill = tint2_fill
    for col in "BC": db[f"{col}{r}"].number_format = INT
    for col in "DG": db[f"{col}{r}"].number_format = PCT
    for col in "EF": db[f"{col}{r}"].number_format = CUR
widths(db, [17, 13, 14, 13, 14, 15, 17, 14, 15, 14, 3, 13, 13])
db.freeze_panes = "A4"

# ---------------------------------------------------------------- DEATH PILE
dp = wb.create_sheet("Death Pile")
title(dp, "Death Pile - Stale Listings", "Items with Status = Listed that have been live longer than the Settings threshold. Automatic - nothing to type here.")
dp["A4"] = "Stale threshold (days)"; dp["B4"] = f"={S_STALE}"
dp["A5"] = "Stale items"; dp["B5"] = f'=COUNTIF({SR("Inventory","Q")},"STALE")'
dp["A6"] = "Cash tied up (at cost)"; dp["B6"] = f'=SUMIFS({inv_cost},{SR("Inventory","Q")},"STALE")'; dp["B6"].number_format = CUR
dp["A7"] = "Total list value"; dp["B7"] = f'=SUMIFS({SR("Inventory","M")},{SR("Inventory","Q")},"STALE")'; dp["B7"].number_format = CUR
for r in range(4, 8):
    dp[f"A{r}"].font = f(bold=True, size=10); dp[f"B{r}"].font = f(size=10, bold=True, color=ACCENT)
    dp[f"A{r}"].border = border; dp[f"B{r}"].border = border; dp[f"A{r}"].fill = tint_fill
header(dp, 9, ["#", "SKU", "Brand", "Item Description", "Category", "Platform Listed", "Date Listed", "Days Listed", "List Price", "Total Cost", "15% Markdown Price"])
mapping = {"B": "A", "C": "D", "D": "E", "E": "F", "F": "N", "G": "L", "H": "P", "I": "M", "J": "J"}
for i in range(50):
    r = 10 + i
    dp[f"A{r}"] = i + 1
    m = f"MATCH($A{r},{SR('Inventory','R')},0)"
    for col, src in mapping.items():
        dp[f"{col}{r}"] = f'=IF($A{r}>$B$5,"",IFERROR(INDEX({SR("Inventory",src)},{m}),""))'
    dp[f"K{r}"] = f'=IF(I{r}="","",ROUND(I{r}*0.85,2))'
    for col in "ABCDEFGHIJK":
        c = dp[f"{col}{r}"]; c.font = f(size=10); c.border = border
        if i % 2: c.fill = tint2_fill
    dp[f"A{r}"].font = f(size=9, color="A0A0A0")
    dp[f"G{r}"].number_format = DATE; dp[f"H{r}"].number_format = INT
    for col in "IJK": dp[f"{col}{r}"].number_format = CUR
dp["A61"] = "Shows up to 50 stale items. Tip: a 10-15% price drop, a bundle offer, or relisting on a second platform usually clears a death pile fastest."
dp["A61"].font = f(italic=True, size=9, color="666666")
widths(dp, [5, 11, 14, 40, 13, 15, 12, 11, 11, 11, 14])
dp.freeze_panes = "A10"; dp.sheet_view.showGridLines = False

# ---------------------------------------------------------------- TAX SUMMARY
tx = wb.create_sheet("Tax Summary")
title(tx, "Tax Summary (Estimate)", "Totals for the 12 months from the Settings year start, mapped loosely to US Schedule C lines. Rows dated outside that window are excluded. ESTIMATE ONLY - not tax advice. Confirm with a tax professional.")
header(tx, 3, ["Line", "Item", "Amount", "Schedule C mapping (approx.)", "Source"])
# The Dashboard totals only the 12 months from the Settings year start, so the Tax Summary
# must use the same window or the "should equal line 15" cross-check below is a false promise -
# and an annual tax figure that silently includes other years is simply wrong.
YR_LO = f'">="&{S_START}'
YR_HI = f'"<"&EDATE({S_START},12)'
def SY(sheet, col, extra=""):
    """Sum one column of `sheet` over the tracking year only."""
    return f'SUMIFS({SR(sheet, col)}{extra},{SR(sheet, "A")},{YR_LO},{SR(sheet, "A")},{YR_HI})'
def E(cat): return SY("Expenses", "D", f',{SR("Expenses","B")},"{cat}"')
lines = [
    ("INCOME", None, None, None),
    ("1", "Gross sales (item prices)", f'={SY("Sales","E")}', "Line 1 - Gross receipts", "Sales: Sale Price"),
    ("2", "Shipping charged to buyers", f'={SY("Sales","F")}', "Line 1 - Gross receipts", "Sales: Shipping Charged"),
    ("3", "Total gross receipts", "=C5+C6", "Line 1", "Lines 1 + 2"),
    ("4", "Cost of goods sold (sold items only)", f'={SY("Sales","K")}', "Part III / Line 4 - COGS", "Sales: Item Total Cost"),
    ("5", "Gross profit", "=C7-C8", "Line 7", "Line 3 - line 4"),
    ("EXPENSES", None, None, None),
    ("6", "Marketplace & payment fees", f'={SY("Sales","H")}+{E("Fees")}', "Line 10 - Commissions and fees", "Sales: Platform Fees + Expenses: Fees"),
    ("7", "Shipping / postage paid", f'={SY("Sales","G")}', "Line 27a - Other expenses (postage)", "Sales: Shipping Cost Paid"),
    ("8", "Shipping supplies", f'={E("Shipping Supplies")}', "Line 22 - Supplies", "Expenses: Shipping Supplies"),
    ("9", "Supplies", f'={E("Supplies")}', "Line 22 - Supplies", "Expenses: Supplies"),
    ("10", "Subscriptions / software", f'={E("Subscriptions")}', "Line 18 - Office expense", "Expenses: Subscriptions"),
    ("11", "Storage", f'={E("Storage")}', "Line 20b - Rent (other business property)", "Expenses: Storage"),
    ("12", "Vehicle mileage deduction + costs on Mileage rows", f'={SY("Expenses","F")}+{E("Mileage")}', "Line 9 - Car and truck expenses", "Expenses: Miles x rate + Amount on Mileage rows"),
    ("13", "Other item costs & other expenses", f'={SY("Sales","J")}+{E("Other")}', "Line 27a - Other expenses", "Sales: Other Costs + Expenses: Other"),
    ("14", "Total expenses", "=SUM(C11:C18)", "Line 28", "Sum of lines 6-13"),
    ("RESULT", None, None, None),
    ("15", "Estimated net profit (loss)", "=C9-C19", "Line 31 - Net profit or (loss)", "Line 5 - line 14"),
    ("", "Cross-check: Dashboard net profit", "=Dashboard!J24", "Should equal line 15", "Dashboard total row"),
    ("INFO", None, None, None),
    ("", "Sales tax collected & remitted by platforms", f'={SY("Sales","I")}', "Not your income or expense - info only", "Sales: Sales Tax Collected"),
    ("", "Miles driven (tracking year)", f'={SY("Expenses","E")}', "Keep a contemporaneous mileage log", "Expenses: Miles"),
    ("", "Unsold inventory at cost (year end)", "=Dashboard!A5", "Inventory carried forward (Part III)", "Dashboard KPI"),
]
r = 4
for row in lines:
    if row[1] is None:
        for col in range(1, 6):
            c = tx.cell(row=r, column=col); c.fill = tint_fill; c.border = border
        tx.cell(row=r, column=1, value=row[0]).font = f(bold=True, size=10, color=ACCENT)
    else:
        for col, v in enumerate(row, 1):
            c = tx.cell(row=r, column=col, value=v); c.font = f(size=10); c.border = border
        tx.cell(row=r, column=3).number_format = CUR
        if row[0] in ("3", "5", "14", "15"):
            for col in range(1, 6): tx.cell(row=r, column=col).font = f(size=10, bold=True)
        tx.cell(row=r, column=4).font = f(size=10, italic=True, color="666666")
        tx.cell(row=r, column=5).font = f(size=9, color="808080")
    r += 1
tx.conditional_formatting.add("C21", FormulaRule(formula=['AND(ISNUMBER(C21),C21<0)'], font=Font(name=FONT, color="9C0006", bold=True)))
tx[f"A{r+1}"] = ("Disclaimer: This summary is a bookkeeping estimate produced from the data you entered. Fee, mileage and category mappings are "
                 "approximations. It is not tax, legal or accounting advice. Consult a qualified professional before filing.")
tx[f"A{r+1}"].font = f(italic=True, size=9, color="9C0006")
tx.merge_cells(start_row=r+1, start_column=1, end_row=r+1, end_column=5)
tx[f"A{r+1}"].alignment = Alignment(wrap_text=True, vertical="top"); tx.row_dimensions[r+1].height = 30
widths(tx, [8, 42, 16, 40, 40])
tx.sheet_view.showGridLines = False

for ws_, col in zip(wb.worksheets, ["1F3A5F", "808080", "0000FF", "0000FF", "0000FF", "1F3A5F", "9C0006", "1F3A5F"]):
    ws_.sheet_properties.tabColor = col
wb.active = 0
wb.save(OUT)
print("saved", OUT)
