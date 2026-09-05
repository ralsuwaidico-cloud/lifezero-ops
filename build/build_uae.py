"""Build: UAE Freelancer & Small Business Bookkeeping Tracker (VAT + Corporate Tax ready)."""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule, CellIsRule
from openpyxl.utils import get_column_letter
from openpyxl.comments import Comment
import datetime as dt

OUT = "/home/claude/products/uae-tracker/UAE_Business_Bookkeeping_VAT_CT_Tracker_2026.xlsx"
N = 503  # last data row (500 data rows from row 4)
FIRST = 4

FONT = "Arial"
ACCENT = "1F3A5F"      # navy
ACCENT2 = "2E75B6"
LIGHT = "EAF1FB"
INPUT_BLUE = "0000FF"
YELLOW = "FFF2CC"
GREY = "F2F2F2"
thin = Side(style="thin", color="BFBFBF")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)

AED = '"AED" #,##0.00;("AED" #,##0.00);"-"'
AED0 = '"AED" #,##0;("AED" #,##0);"-"'
PCT = '0.0%'
DATE = 'dd-mmm-yyyy'

wb = Workbook()

def f(bold=False, color="000000", size=10, italic=False):
    return Font(name=FONT, bold=bold, color=color, size=size, italic=italic)

def fill(hex_):
    return PatternFill("solid", start_color=hex_, end_color=hex_)

def header_row(ws, row, headers, widths=None):
    for i, h in enumerate(headers, 1):
        c = ws.cell(row=row, column=i, value=h)
        c.font = Font(name=FONT, bold=True, color="FFFFFF", size=10)
        c.fill = fill(ACCENT)
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = BORDER
    ws.row_dimensions[row].height = 32
    if widths:
        for i, w in enumerate(widths, 1):
            ws.column_dimensions[get_column_letter(i)].width = w

def title(ws, text, sub=None):
    ws["A1"] = text
    ws["A1"].font = Font(name=FONT, bold=True, size=16, color=ACCENT)
    if sub:
        ws["A2"] = sub
        ws["A2"].font = f(italic=True, color="595959")
    ws.sheet_view.showGridLines = False

def style_range(ws, rng, font=None, fmt=None, fill_=None, border=True, align=None):
    for row in ws[rng]:
        for c in row:
            if font: c.font = font
            if fmt: c.number_format = fmt
            if fill_: c.fill = fill_
            if border: c.border = BORDER
            if align: c.alignment = align

# ------------------------------------------------------------------ START HERE
ws = wb.active
ws.title = "START HERE"
title(ws, "UAE Freelancer & Small Business Bookkeeping Tracker 2026",
      "VAT + Corporate Tax ready · Excel & Google Sheets compatible")
ws.column_dimensions["A"].width = 3
ws.column_dimensions["B"].width = 110
rows = [
    ("HOW TO USE", True),
    ("1. Go to Settings and enter your business name, financial-year start, VAT status and your VAT period dates.", False),
    ("2. Log every invoice you issue in Income (one row per invoice). Choose the VAT treatment from the dropdown — VAT is calculated for you.", False),
    ("3. Log every business cost in Expenses. Mark whether the input VAT is recoverable (you have a valid tax invoice and the cost is business-related).", False),
    ("4. Open the VAT Return sheet before each filing: set the period dates and copy the boxes into the FTA EmaraTax portal.", False),
    ("5. Watch the Dashboard: monthly profit, unpaid invoices, VAT to set aside, and your Corporate Tax estimate update automatically.", False),
    ("", False),
    ("LEGEND", True),
    ("Blue text = cells you type into.   Black text = formulas (do not edit).   Yellow cells = key settings to check.", False),
    ("Rows 4–6 of Income and Expenses contain SAMPLE data. Clear the cell contents of those rows (don't delete the rows) before you start.", False),
    ("Never delete whole rows — clear cell contents instead, so formulas and dropdowns stay intact. Capacity: 500 rows per sheet.", False),
    ("", False),
    ("KEY UAE THRESHOLDS BUILT IN (editable in Settings — verify current figures at tax.gov.ae)", True),
    ("• VAT: 5% standard rate. Mandatory registration when taxable supplies exceed AED 375,000 in the past 12 months (or expected in the next 30 days); voluntary from AED 187,500.", False),
    ("• Corporate Tax: 0% on taxable income up to AED 375,000, 9% above. Small Business Relief (elect if revenue ≤ AED 3,000,000) gives 0% for tax periods ending on or before 31 Dec 2026.", False),
    ("• Registration deadlines and penalties are not modelled — this tracker estimates amounts, it does not file for you.", False),
    ("", False),
    ("DISCLAIMER", True),
    ("This workbook is a bookkeeping aid, not tax, legal or accounting advice. Figures are estimates based on the settings you enter. Confirm your obligations with the Federal Tax Authority (tax.gov.ae) or a registered tax agent. The author accepts no liability for filings made using this tool.", False),
]
r = 4
for text, bold in rows:
    c = ws.cell(row=r, column=2, value=text)
    c.font = f(bold=bold, color=ACCENT if bold else "000000", size=11 if bold else 10)
    c.alignment = Alignment(wrap_text=True, vertical="top")
    if bold: c.fill = fill(LIGHT)
    r += 1

# ------------------------------------------------------------------ SETTINGS
st = wb.create_sheet("Settings")
title(st, "Settings", "Edit the blue cells. Yellow = check these before use.")
st.column_dimensions["A"].width = 44
st.column_dimensions["B"].width = 22
st.column_dimensions["C"].width = 60
st.column_dimensions["E"].width = 26
st.column_dimensions["F"].width = 30
st.column_dimensions["G"].width = 22

settings = [
    # row, label, value, fmt, note, yellow
    (4, "Business / trade name", "Your Business Name", None, "Appears on the Dashboard.", False),
    (5, "Financial year start", dt.date(2026, 1, 1), DATE, "Dashboard months and Corporate Tax estimate run 12 months from this date.", True),
    (6, "VAT registered? (Yes/No)", "Yes", None, "If No, VAT columns still calculate so you can see what you would charge once registered.", True),
    (7, "Standard VAT rate", 0.05, PCT, "UAE standard rate. Source: Federal Decree-Law No. 8 of 2017, tax.gov.ae", True),
    (8, "VAT mandatory registration threshold", 375000, AED0, "Taxable supplies in past 12 months (or expected next 30 days).", False),
    (9, "VAT voluntary registration threshold", 187500, AED0, "", False),
    (10, "Corporate Tax rate", 0.09, PCT, "Source: Federal Decree-Law No. 47 of 2022.", True),
    (11, "Corporate Tax 0% band (taxable income)", 375000, AED0, "Taxable income up to this amount is taxed at 0%.", False),
    (12, "Elect Small Business Relief? (Yes/No)", "Yes", None, "Available if revenue ≤ threshold below, for tax periods ending on or before 31 Dec 2026. Election is made in the CT return.", True),
    (13, "Small Business Relief revenue threshold", 3000000, AED0, "", False),
    (14, "Small Business Relief last eligible period end", dt.date(2026, 12, 31), DATE, "Relief not available for periods ending after this date.", False),
    (15, "Current VAT return period — start", dt.date(2026, 1, 1), DATE, "Your FTA-assigned tax period (quarterly for most SMEs). Used by the VAT Return sheet.", True),
    (16, "Current VAT return period — end", dt.date(2026, 3, 31), DATE, "", True),
    (17, "Opening cash balance", 0, AED, "Bank + cash at financial-year start (for the cash position tile).", False),
    (18, "Invoice overdue after (days)", 30, "0", "Used for the receivables ageing on the Dashboard.", False),
]
header_row(st, 3, ["Setting", "Value", "Notes / source"])
for row, label, val, fmt, note, yel in settings:
    st.cell(row=row, column=1, value=label).font = f(bold=True)
    c = st.cell(row=row, column=2, value=val)
    c.font = f(color=INPUT_BLUE)
    if fmt: c.number_format = fmt
    if yel: c.fill = fill(YELLOW)
    c.alignment = Alignment(horizontal="right")
    n = st.cell(row=row, column=3, value=note)
    n.font = f(italic=True, color="595959")
    n.alignment = Alignment(wrap_text=True, vertical="top")
    for col in (1, 2, 3):
        st.cell(row=row, column=col).border = BORDER

# Lists
header_row(st, 3, ["Setting", "Value", "Notes / source", "", "Income categories", "Expense categories", "VAT treatment"])
st.cell(row=3, column=4).fill = PatternFill(fill_type=None)
st.cell(row=3, column=4).border = Border()
inc_cats = ["Consulting / services", "Freelance project", "Retainer", "Product sales", "Commission", "Training", "Other income"]
exp_cats = ["Software & subscriptions", "Office / coworking rent", "Trade licence & permits", "Marketing & advertising",
            "Travel & transport", "Telecom & internet", "Professional fees (legal/accounting)", "Bank & payment fees",
            "Equipment & hardware", "Contractors & salaries", "Insurance", "Meals & entertainment", "Other expense"]
vat_treat = ["Standard 5%", "Zero-rated 0%", "Exempt", "Out of scope"]
yn = ["Yes", "No"]
for i, v in enumerate(inc_cats): st.cell(row=4 + i, column=5, value=v).font = f(color=INPUT_BLUE)
for i, v in enumerate(exp_cats): st.cell(row=4 + i, column=6, value=v).font = f(color=INPUT_BLUE)
for i, v in enumerate(vat_treat): st.cell(row=4 + i, column=7, value=v).font = f()
st["E18"] = "Payment status"; st["E18"].font = f(bold=True)
st["E19"] = "Paid"; st["E20"] = "Unpaid"; st["E21"] = "Partially paid"; st["E22"] = "Written off"
st["G9"] = "Yes/No"; st["G9"].font = f(bold=True)
st["G10"] = "Yes"; st["G11"] = "No"
st["G13"] = "Payment method"; st["G13"].font = f(bold=True)
for i, v in enumerate(["Bank transfer", "Card", "Cash", "PayPal / Stripe", "Cheque", "Other"]):
    st.cell(row=14 + i, column=7, value=v)
st["A20"] = "Emirates ID / TRN (optional, for your records)"; st["A20"].font = f(bold=True)
st["B20"].font = f(color=INPUT_BLUE); st["B20"].border = BORDER; st["A20"].border = BORDER
st["A21"] = "Tax Registration Number (TRN)"; st["A21"].font = f(bold=True)
st["B21"].font = f(color=INPUT_BLUE); st["B21"].border = BORDER; st["A21"].border = BORDER

# Named ranges via defined names for readability
from openpyxl.workbook.defined_name import DefinedName
def name(nm, ref):
    wb.defined_names[nm] = DefinedName(nm, attr_text=ref)
name("FY_START", "Settings!$B$5")
name("VAT_RATE", "Settings!$B$7")
name("VAT_MAND", "Settings!$B$8")
name("VAT_VOL", "Settings!$B$9")
name("CT_RATE", "Settings!$B$10")
name("CT_BAND", "Settings!$B$11")
name("SBR_ELECT", "Settings!$B$12")
name("SBR_LIMIT", "Settings!$B$13")
name("SBR_END", "Settings!$B$14")
name("VP_START", "Settings!$B$15")
name("VP_END", "Settings!$B$16")
name("OPEN_CASH", "Settings!$B$17")
name("OVERDUE_DAYS", "Settings!$B$18")

# ------------------------------------------------------------------ INCOME
inc = wb.create_sheet("Income")
title(inc, "Income — invoices issued", "One row per invoice. Blue = type. VAT, totals and ageing are calculated.")
inc_headers = ["Invoice date", "Invoice #", "Client", "Description", "Category", "Amount excl. VAT (AED)",
               "VAT treatment", "VAT amount (AED)", "Total incl. VAT (AED)", "Payment status", "Date paid",
               "Amount received (AED)", "Days outstanding", "Overdue?", "Month #", "In VAT period?"]
inc_widths = [13, 12, 22, 30, 22, 17, 15, 15, 17, 15, 13, 17, 13, 10, 9, 12]
header_row(inc, 3, inc_headers, inc_widths)
inc.freeze_panes = "C4"
inc.auto_filter.ref = f"A3:P{N}"
samples_inc = [
    (dt.date(2026, 1, 12), "INV-001", "Al Noor Trading LLC", "Brand strategy workshop", "Consulting / services", 12000, "Standard 5%", "Paid", dt.date(2026, 1, 28), 12600),
    (dt.date(2026, 2, 3), "INV-002", "Sarah K. (Dubai)", "Website copywriting", "Freelance project", 4500, "Standard 5%", "Unpaid", None, None),
    (dt.date(2026, 2, 20), "INV-003", "Nordic Design AB (Sweden)", "Export of design services", "Freelance project", 8000, "Zero-rated 0%", "Paid", dt.date(2026, 3, 5), 8000),
]
for r in range(FIRST, N + 1):
    for col in range(1, 17):
        inc.cell(row=r, column=col).border = BORDER
        inc.cell(row=r, column=col).font = f(color=INPUT_BLUE) if col in (1, 2, 3, 4, 5, 6, 7, 10, 11, 12) else f()
    inc.cell(row=r, column=1).number_format = DATE
    inc.cell(row=r, column=11).number_format = DATE
    for col in (6, 8, 9, 12): inc.cell(row=r, column=col).number_format = AED
    inc.cell(row=r, column=8, value=f'=IF(F{r}="","",IF(G{r}="Standard 5%",F{r}*VAT_RATE,0))')
    inc.cell(row=r, column=9, value=f'=IF(F{r}="","",F{r}+H{r})')
    inc.cell(row=r, column=13, value=f'=IF(OR(A{r}="",J{r}="Paid",J{r}="Written off"),"",TODAY()-A{r})')
    inc.cell(row=r, column=14, value=f'=IF(M{r}="","",IF(M{r}>OVERDUE_DAYS,"OVERDUE",""))')
    inc.cell(row=r, column=15, value=f'=IF(A{r}="","",IF(A{r}<FY_START,0,(YEAR(A{r})-YEAR(FY_START))*12+MONTH(A{r})-MONTH(FY_START)+1))')
    inc.cell(row=r, column=16, value=f'=IF(A{r}="","",IF(AND(A{r}>=VP_START,A{r}<=VP_END),1,0))')
    for col in (15, 16): inc.cell(row=r, column=col).font = f(color="7F7F7F")
for i, s in enumerate(samples_inc):
    r = FIRST + i
    d, num, cl, desc, cat, amt, vt, status, paid, recv = s
    for col, v in zip((1, 2, 3, 4, 5, 6, 7, 10, 11, 12), (d, num, cl, desc, cat, amt, vt, status, paid, recv)):
        if v is not None: inc.cell(row=r, column=col, value=v)
dv = DataValidation(type="list", formula1="=Settings!$E$4:$E$10", allow_blank=True); inc.add_data_validation(dv); dv.add(f"E{FIRST}:E{N}")
dv = DataValidation(type="list", formula1="=Settings!$G$4:$G$7", allow_blank=True); inc.add_data_validation(dv); dv.add(f"G{FIRST}:G{N}")
dv = DataValidation(type="list", formula1="=Settings!$E$19:$E$22", allow_blank=True); inc.add_data_validation(dv); dv.add(f"J{FIRST}:J{N}")
inc.conditional_formatting.add(f"A{FIRST}:P{N}", FormulaRule(formula=[f'$N{FIRST}="OVERDUE"'], fill=fill("FDE9E7")))
inc.conditional_formatting.add(f"A{FIRST}:P{N}", FormulaRule(formula=[f'$J{FIRST}="Paid"'], fill=fill("E8F5E9")))

# ------------------------------------------------------------------ EXPENSES
ex = wb.create_sheet("Expenses")
title(ex, "Expenses — business costs", "One row per receipt / bill. Only tick 'Yes' for recoverable input VAT if you hold a valid tax invoice.")
ex_headers = ["Date", "Supplier", "Description", "Category", "Amount excl. VAT (AED)", "VAT treatment",
              "VAT on invoice (AED)", "Input VAT recoverable? (Yes/No)", "Recoverable VAT (AED)", "Total paid (AED)",
              "Payment method", "Deductible for CT? (Yes/No)", "Month #", "In VAT period?"]
ex_widths = [13, 22, 30, 28, 17, 15, 15, 16, 16, 16, 16, 15, 9, 12]
header_row(ex, 3, ex_headers, ex_widths)
ex.freeze_panes = "C4"
ex.auto_filter.ref = f"A3:N{N}"
samples_ex = [
    (dt.date(2026, 1, 5), "Dubai Economy (DED)", "Freelance permit renewal", "Trade licence & permits", 7500, "Out of scope", "No", "Bank transfer", "Yes"),
    (dt.date(2026, 1, 15), "Adobe", "Creative Cloud annual", "Software & subscriptions", 2400, "Standard 5%", "Yes", "Card", "Yes"),
    (dt.date(2026, 2, 8), "Nasab Coworking", "Hot desk — February", "Office / coworking rent", 1500, "Standard 5%", "Yes", "Card", "Yes"),
]
for r in range(FIRST, N + 1):
    for col in range(1, 15):
        ex.cell(row=r, column=col).border = BORDER
        ex.cell(row=r, column=col).font = f(color=INPUT_BLUE) if col in (1, 2, 3, 4, 5, 6, 8, 11, 12) else f()
    ex.cell(row=r, column=1).number_format = DATE
    for col in (5, 7, 9, 10): ex.cell(row=r, column=col).number_format = AED
    ex.cell(row=r, column=7, value=f'=IF(E{r}="","",IF(F{r}="Standard 5%",E{r}*VAT_RATE,0))')
    ex.cell(row=r, column=9, value=f'=IF(E{r}="","",IF(AND(H{r}="Yes",F{r}="Standard 5%"),G{r},0))')
    ex.cell(row=r, column=10, value=f'=IF(E{r}="","",E{r}+G{r})')
    ex.cell(row=r, column=13, value=f'=IF(A{r}="","",IF(A{r}<FY_START,0,(YEAR(A{r})-YEAR(FY_START))*12+MONTH(A{r})-MONTH(FY_START)+1))')
    ex.cell(row=r, column=14, value=f'=IF(A{r}="","",IF(AND(A{r}>=VP_START,A{r}<=VP_END),1,0))')
    for col in (13, 14): ex.cell(row=r, column=col).font = f(color="7F7F7F")
for i, s in enumerate(samples_ex):
    r = FIRST + i
    d, sup, desc, cat, amt, vt, rec, pm, ded = s
    for col, v in zip((1, 2, 3, 4, 5, 6, 8, 11, 12), (d, sup, desc, cat, amt, vt, rec, pm, ded)):
        ex.cell(row=r, column=col, value=v)
dv = DataValidation(type="list", formula1="=Settings!$F$4:$F$16", allow_blank=True); ex.add_data_validation(dv); dv.add(f"D{FIRST}:D{N}")
dv = DataValidation(type="list", formula1="=Settings!$G$4:$G$7", allow_blank=True); ex.add_data_validation(dv); dv.add(f"F{FIRST}:F{N}")
dv = DataValidation(type="list", formula1="=Settings!$G$10:$G$11", allow_blank=True); ex.add_data_validation(dv); dv.add(f"H{FIRST}:H{N}"); dv.add(f"L{FIRST}:L{N}")
dv = DataValidation(type="list", formula1="=Settings!$G$14:$G$19", allow_blank=True); ex.add_data_validation(dv); dv.add(f"K{FIRST}:K{N}")

INC = f"Income!$A${FIRST}:$A${N}"
def incr(col): return f"Income!${col}${FIRST}:${col}${N}"
def exr(col): return f"Expenses!${col}${FIRST}:${col}${N}"

# ------------------------------------------------------------------ VAT RETURN
vr = wb.create_sheet("VAT Return")
title(vr, "VAT Return helper", "Set the period in Settings (B15:B16). Copy these boxes into the FTA EmaraTax return.")
vr.column_dimensions["A"].width = 6; vr.column_dimensions["B"].width = 58; vr.column_dimensions["C"].width = 20; vr.column_dimensions["D"].width = 20; vr.column_dimensions["E"].width = 50
vr["B4"] = "Period start"; vr["C4"] = "=VP_START"; vr["C4"].number_format = DATE
vr["B5"] = "Period end"; vr["C5"] = "=VP_END"; vr["C5"].number_format = DATE
vr["B6"] = "VAT registered?"; vr["C6"] = "=Settings!B6"
for a in ("B4", "B5", "B6"): vr[a].font = f(bold=True)
for a in ("C4", "C5", "C6"): vr[a].font = f(color="008000"); vr[a].alignment = Alignment(horizontal="right")
header_row(vr, 8, ["Box", "Description", "Amount (AED)", "VAT (AED)", "How it is calculated"])
inP = incr("P"); exP = exr("P") if False else f"Expenses!$N${FIRST}:$N${N}"
lines = [
    ("1a", "Standard-rated supplies (sales at 5%)",
     f'=SUMIFS({incr("F")},{incr("G")},"Standard 5%",{inP},1)',
     f'=SUMIFS({incr("H")},{incr("G")},"Standard 5%",{inP},1)',
     "Income rows dated within the period with VAT treatment 'Standard 5%'."),
    ("4", "Zero-rated supplies (exports, certain services)",
     f'=SUMIFS({incr("F")},{incr("G")},"Zero-rated 0%",{inP},1)', "=0",
     "Income rows with 'Zero-rated 0%'."),
    ("5", "Exempt supplies",
     f'=SUMIFS({incr("F")},{incr("G")},"Exempt",{inP},1)', "=0",
     "Income rows with 'Exempt'."),
    ("—", "Out-of-scope income (not reported on the return)",
     f'=SUMIFS({incr("F")},{incr("G")},"Out of scope",{inP},1)', "=0",
     "Shown for reconciliation only."),
    ("8", "TOTAL OUTPUT VAT DUE", "=C9+C10+C11", "=D9+D10+D11", "Sum of boxes 1a, 4, 5."),
    ("9", "Standard-rated expenses with recoverable input VAT",
     f'=SUMIFS({exr("E")},{exr("H")},"Yes",{exr("F")},"Standard 5%",{exP},1)',
     f'=SUMIFS({exr("I")},{exP},1)',
     "Expense rows in the period where 'Input VAT recoverable' = Yes and treatment = Standard 5%."),
    ("11", "TOTAL RECOVERABLE INPUT VAT", "=C14", "=D14", ""),
    ("12/13", "NET VAT PAYABLE (positive) / REFUNDABLE (negative)", "", "=D13-D15", "Output VAT − recoverable input VAT."),
]
r = 9
for box, desc, amt, vat, how in lines:
    vr.cell(row=r, column=1, value=box); vr.cell(row=r, column=2, value=desc)
    vr.cell(row=r, column=3, value=amt if amt != "" else None); vr.cell(row=r, column=4, value=vat)
    vr.cell(row=r, column=5, value=how)
    bold = box in ("8", "11", "12/13")
    for col in range(1, 6):
        c = vr.cell(row=r, column=col); c.border = BORDER
        c.font = f(bold=bold)
        if bold: c.fill = fill(LIGHT)
    vr.cell(row=r, column=3).number_format = AED; vr.cell(row=r, column=4).number_format = AED
    vr.cell(row=r, column=5).font = f(italic=True, color="595959"); vr.cell(row=r, column=5).alignment = Alignment(wrap_text=True)
    r += 1
vr["D16"].fill = fill(YELLOW); vr["D16"].font = f(bold=True, size=12)
vr["B18"] = "Non-recoverable VAT paid in period (cost to you)"; vr["B18"].font = f(bold=True)
vr["D18"] = f'=SUMIFS({exr("G")},{exP},1)-D14'; vr["D18"].number_format = AED; vr["D18"].border = BORDER; vr["B18"].border = BORDER
vr["B20"] = "Registration check — taxable turnover, last 12 months to today"; vr["B20"].font = f(bold=True)
vr["D20"] = (f'=SUMIFS({incr("F")},{incr("G")},"Standard 5%",{INC},">"&(TODAY()-365))'
             f'+SUMIFS({incr("F")},{incr("G")},"Zero-rated 0%",{INC},">"&(TODAY()-365))')
vr["D20"].number_format = AED; vr["D20"].border = BORDER; vr["B20"].border = BORDER
vr["B21"] = "Status vs thresholds"; vr["B21"].font = f(bold=True); vr["B21"].border = BORDER
vr["D21"] = '=IF(D20>=VAT_MAND,"ABOVE MANDATORY THRESHOLD — must be registered",IF(D20>=VAT_VOL,"Above voluntary threshold — may register","Below voluntary threshold"))'
vr["D21"].font = f(bold=True, color="C00000"); vr["D21"].border = BORDER
vr["B23"] = "Note: taxable turnover = standard-rated + zero-rated supplies (exempt and out-of-scope excluded). Always confirm box mapping against the current FTA return form."
vr["B23"].font = f(italic=True, color="595959"); vr["B23"].alignment = Alignment(wrap_text=True)
vr.row_dimensions[23].height = 30
vr.merge_cells("B23:E23")

# ------------------------------------------------------------------ CORPORATE TAX
ct = wb.create_sheet("Corporate Tax")
title(ct, "Corporate Tax estimate — current financial year", "Accrual basis: all invoices issued and costs incurred in the 12 months from the financial-year start.")
ct.column_dimensions["A"].width = 56; ct.column_dimensions["B"].width = 20; ct.column_dimensions["C"].width = 60
header_row(ct, 3, ["Line", "AED", "Notes"])
FY_END = "EDATE(FY_START,12)-1"
ct_lines = [
    ("Financial year", f'=TEXT(FY_START,"dd-mmm-yyyy")&" to "&TEXT({FY_END},"dd-mmm-yyyy")', None, "From Settings."),
    ("Revenue (all income excl. VAT)", f'=SUMIFS({incr("F")},{INC},">="&FY_START,{INC},"<="&{FY_END})', AED, "All Income rows in the year, regardless of payment status (accrual)."),
    ("Deductible expenses (excl. VAT, marked deductible = Yes)", f'=SUMIFS({exr("E")},{exr("L")},"Yes",{exr("A")},">="&FY_START,{exr("A")},"<="&{FY_END})', AED, "Note: entertainment is only 50% deductible under UAE CT law — adjust below if relevant."),
    ("Non-recoverable VAT on deductible expenses", f'=SUMIFS({exr("G")},{exr("L")},"Yes",{exr("H")},"No",{exr("A")},">="&FY_START,{exr("A")},"<="&{FY_END})', AED, "Irrecoverable VAT is a business cost."),
    ("Manual adjustments (+ adds to income / − deducts)", 0, AED, "Blue input: e.g. −50% of meals & entertainment, depreciation, disallowed fines."),
    ("Accounting / taxable profit (estimate)", "=B5-B6-B7+B8", AED, "Revenue − expenses − irrecoverable VAT + adjustments."),
    ("Small Business Relief elected?", "=SBR_ELECT", None, "From Settings."),
    ("Eligible for Small Business Relief this year?", f'=IF(AND(SBR_ELECT="Yes",B5<=SBR_LIMIT,{FY_END}<=SBR_END),"Yes","No")', None, "Requires revenue ≤ threshold AND period ending on/before the relief end date."),
    ("Taxable income above 0% band", "=MAX(0,B9-CT_BAND)", AED, "Profit above the AED 375,000 band."),
    ("ESTIMATED CORPORATE TAX", '=IF(B11="Yes",0,B12*CT_RATE)', AED, "0 if relief applies; otherwise 9% × income above the band."),
    ("Effective tax rate on profit", '=IF(B9<=0,0,B13/B9)', PCT, ""),
    ("Suggested monthly set-aside for CT", '=B13/12', AED, "Park this each month so the payment is painless."),
]
r = 4
for label, val, fmt, note in ct_lines:
    ct.cell(row=r, column=1, value=label).font = f(bold=True)
    c = ct.cell(row=r, column=2, value=val)
    c.font = f(color=INPUT_BLUE) if r == 8 else f()
    if fmt: c.number_format = fmt
    c.alignment = Alignment(horizontal="right")
    n = ct.cell(row=r, column=3, value=note); n.font = f(italic=True, color="595959"); n.alignment = Alignment(wrap_text=True, vertical="top")
    for col in (1, 2, 3): ct.cell(row=r, column=col).border = BORDER
    r += 1
ct["A13"].fill = fill(LIGHT); ct["B13"].fill = fill(YELLOW); ct["B13"].font = f(bold=True, size=12)
ct["B8"].fill = fill(YELLOW)
ct["A18"] = ("Reminder: every taxable person (including freelancers with a licence/permit) must register for Corporate Tax with the FTA and file a return "
             "within 9 months of the financial-year end, even when the tax due is zero or Small Business Relief is claimed. Registration deadlines and penalties are not modelled here.")
ct["A18"].font = f(italic=True, color="595959"); ct["A18"].alignment = Alignment(wrap_text=True); ct.merge_cells("A18:C18"); ct.row_dimensions[18].height = 45

# ------------------------------------------------------------------ DASHBOARD
db = wb.create_sheet("Dashboard", 1)
title(db, '=Settings!B4&" — Dashboard"', None)
db["A2"] = '="Financial year from "&TEXT(FY_START,"dd mmm yyyy")&"   ·   Today: "&TEXT(TODAY(),"dd mmm yyyy")'
db["A2"].font = f(italic=True, color="595959")
for col, w in zip("ABCDEFGHIJ", [26, 17, 17, 16, 30, 17, 16, 17, 16, 14]):
    db.column_dimensions[col].width = w

# KPI tiles rows 4-6 (label row 4, value row 5) — two banks
kpis = [
    ("Revenue YTD (excl. VAT)", f'=SUMIFS({incr("F")},{incr("O")},">=1",{incr("O")},"<=12")', AED0),
    ("Expenses YTD (excl. VAT)", f'=SUMIFS({exr("E")},{exr("M")},">=1",{exr("M")},"<=12")', AED0),
    ("Profit YTD", "=B5-C5", AED0),
    ("Cash received YTD", f'=OPEN_CASH+SUMIFS({incr("L")},{incr("O")},">=1",{incr("O")},"<=12")-SUMIFS({exr("J")},{exr("M")},">=1",{exr("M")},"<=12")', AED0),
    ("Unpaid invoices (incl. VAT)", f'=SUMIFS({incr("I")},{incr("J")},"Unpaid")+SUMIFS({incr("I")},{incr("J")},"Partially paid")-SUMIFS({incr("L")},{incr("J")},"Partially paid")', AED0),
]
kpis2 = [
    ("Overdue invoices (count)", f'=COUNTIF({incr("N")},"OVERDUE")', "0"),
    ("Net VAT due this period", "='VAT Return'!D16", AED0),
    ("Corporate Tax estimate (year)", "='Corporate Tax'!B13", AED0),
    ("VAT registration status", "=IF('VAT Return'!D20>=VAT_MAND,\"Mandatory\",IF('VAT Return'!D20>=VAT_VOL,\"Voluntary\",\"Below\"))", None),
    ("Profit margin YTD", '=IF(B5=0,0,D5/B5)', PCT),
]
def tiles(row, items):
    for i, (label, formula, fmt) in enumerate(items):
        col = 2 + i
        l = db.cell(row=row, column=col, value=label); l.font = Font(name=FONT, bold=True, color="FFFFFF", size=9)
        l.fill = fill(ACCENT2); l.alignment = Alignment(horizontal="center", wrap_text=True); l.border = BORDER
        v = db.cell(row=row + 1, column=col, value=formula); v.font = f(bold=True, size=13, color=ACCENT)
        v.fill = fill(LIGHT); v.alignment = Alignment(horizontal="center"); v.border = BORDER
        if fmt: v.number_format = fmt
    db.row_dimensions[row].height = 28; db.row_dimensions[row + 1].height = 26
tiles(4, kpis); tiles(7, kpis2)
db["A4"] = "Money"; db["A7"] = "Compliance"
for a in ("A4", "A7"): db[a].font = f(bold=True, color=ACCENT, size=11); db[a].alignment = Alignment(vertical="center")

# Monthly table
header_row(db, 10, ["Month", "Revenue (excl. VAT)", "Expenses (excl. VAT)", "Profit", "Cash in", "Cash out", "Output VAT", "Recoverable input VAT", "Net VAT", "Margin"])
for i in range(12):
    r = 11 + i
    db.cell(row=r, column=1, value=f'=TEXT(EDATE(FY_START,{i}),"mmm yyyy")').font = f(bold=True)
    db.cell(row=r, column=2, value=f'=SUMIFS({incr("F")},{incr("O")},{i+1})')
    db.cell(row=r, column=3, value=f'=SUMIFS({exr("E")},{exr("M")},{i+1})')
    db.cell(row=r, column=4, value=f'=B{r}-C{r}')
    db.cell(row=r, column=5, value=f'=SUMIFS({incr("L")},{incr("O")},{i+1})')
    db.cell(row=r, column=6, value=f'=SUMIFS({exr("J")},{exr("M")},{i+1})')
    db.cell(row=r, column=7, value=f'=SUMIFS({incr("H")},{incr("O")},{i+1})')
    db.cell(row=r, column=8, value=f'=SUMIFS({exr("I")},{exr("M")},{i+1})')
    db.cell(row=r, column=9, value=f'=G{r}-H{r}')
    db.cell(row=r, column=10, value=f'=IF(B{r}=0,0,D{r}/B{r})')
    for col in range(1, 11):
        c = db.cell(row=r, column=col); c.border = BORDER
        if col > 1: c.font = f()
        c.number_format = PCT if col == 10 else AED0
        if i % 2: c.fill = fill(GREY)
    db.cell(row=r, column=1).number_format = "General"
r = 23
db.cell(row=r, column=1, value="TOTAL").font = f(bold=True)
for col in range(2, 10):
    L = get_column_letter(col)
    c = db.cell(row=r, column=col, value=f"=SUM({L}11:{L}22)"); c.font = f(bold=True); c.number_format = AED0
db.cell(row=r, column=10, value="=IF(B23=0,0,D23/B23)").number_format = PCT
for col in range(1, 11):
    db.cell(row=r, column=col).fill = fill(LIGHT); db.cell(row=r, column=col).border = BORDER; db.cell(row=r, column=col).font = f(bold=True)
db.conditional_formatting.add("D11:D22", CellIsRule(operator="lessThan", formula=["0"], font=Font(name=FONT, color="C00000")))

# Category tables
header_row(db, 26, ["Income by category", "Revenue (excl. VAT)", "% of total"])
for i, cat in enumerate(inc_cats):
    r = 27 + i
    db.cell(row=r, column=1, value=f"=Settings!E{4+i}")
    db.cell(row=r, column=2, value=f'=SUMIFS({incr("F")},{incr("E")},A{r},{incr("O")},">=1",{incr("O")},"<=12")').number_format = AED0
    db.cell(row=r, column=3, value=f'=IF($B$23=0,0,B{r}/$B$23)').number_format = PCT
    for col in (1, 2, 3): db.cell(row=r, column=col).border = BORDER; db.cell(row=r, column=col).font = f()
header_row(db, 26, ["Income by category", "Revenue (excl. VAT)", "% of total", "", "Expenses by category", "Amount (excl. VAT)", "% of total"])
db.cell(row=26, column=4).fill = PatternFill(fill_type=None); db.cell(row=26, column=4).border = Border()
for i, cat in enumerate(exp_cats):
    r = 27 + i
    db.cell(row=r, column=5, value=f"=Settings!F{4+i}")
    db.cell(row=r, column=6, value=f'=SUMIFS({exr("E")},{exr("D")},E{r},{exr("M")},">=1",{exr("M")},"<=12")').number_format = AED0
    db.cell(row=r, column=7, value=f'=IF($C$23=0,0,F{r}/$C$23)').number_format = PCT
    for col in (5, 6, 7): db.cell(row=r, column=col).border = BORDER; db.cell(row=r, column=col).font = f()

# Receivables ageing
header_row(db, 42, ["Receivables ageing (unpaid)", "Count", "Amount incl. VAT"])
ages = [("Not yet overdue", f'=COUNTIFS({incr("M")},">=0",{incr("M")},"<="&OVERDUE_DAYS)', f'=SUMIFS({incr("I")},{incr("M")},">=0",{incr("M")},"<="&OVERDUE_DAYS)'),
        ("Overdue 1–30 days", f'=COUNTIFS({incr("M")},">"&OVERDUE_DAYS,{incr("M")},"<="&(OVERDUE_DAYS+30))', f'=SUMIFS({incr("I")},{incr("M")},">"&OVERDUE_DAYS,{incr("M")},"<="&(OVERDUE_DAYS+30))'),
        ("Overdue 31–90 days", f'=COUNTIFS({incr("M")},">"&(OVERDUE_DAYS+30),{incr("M")},"<="&(OVERDUE_DAYS+90))', f'=SUMIFS({incr("I")},{incr("M")},">"&(OVERDUE_DAYS+30),{incr("M")},"<="&(OVERDUE_DAYS+90))'),
        ("Overdue 90+ days", f'=COUNTIFS({incr("M")},">"&(OVERDUE_DAYS+90))', f'=SUMIFS({incr("I")},{incr("M")},">"&(OVERDUE_DAYS+90))')]
for i, (lab, cnt, amt) in enumerate(ages):
    r = 43 + i
    db.cell(row=r, column=1, value=lab); db.cell(row=r, column=2, value=cnt); db.cell(row=r, column=3, value=amt).number_format = AED0
    for col in (1, 2, 3): db.cell(row=r, column=col).border = BORDER; db.cell(row=r, column=col).font = f()

wb.calculation.fullCalcOnLoad = True
wb.save(OUT)
print("saved", OUT)
