import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    df = pd.read_excel(filepath)
    filename = Path(filepath).stem

    invoice_nr, date = filename.split("-")

    pdf.set_font("times", size=16, style='B')
    pdf.cell(w=50, h=8, txt=f"Invoice Nr: {invoice_nr}." , ln=1)

    pdf.set_font("times", size=16, style='B')
    pdf.cell(w=50, h=8, txt=f"Date: {date}.", ln=1)

    columns = df.columns
    columns = [col.replace("_", " ").title() for col in columns]
    pdf.set_font("times", size=12, style='B')
    pdf.cell(w=30, h=8, txt= columns[0], border=1)
    pdf.cell(w=60, h=8, txt= columns[1], border=1)
    pdf.cell(w=40, h=8, txt= columns[2], border=1)
    pdf.cell(w=40, h=8, txt= columns[3], border=1)
    pdf.cell(w=25, h=8, txt= columns[4], border=1, ln=1)

    for index, row in df.iterrows():
        pdf.set_font("times", size=12)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=60, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=40, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=40, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=25, h=8, txt=str(row["total_price"]), border=1, ln=1)

    total_sum = df["total_price"].sum()
    pdf.set_font("times", size=12, style='B')
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=60, h=8, txt="", border=1)
    pdf.cell(w=40, h=8, txt="", border=1)
    pdf.cell(w=40, h=8, txt="", border=1)
    pdf.cell(w=25, h=8, txt=str(total_sum), border=1, ln=1)

    pdf.set_font("times", size=12, style='B')
    pdf.cell(w=50, h=8, txt=f"The total price is: {total_sum}", ln=1)

    pdf.set_font("times", size=12, style='B')
    pdf.cell(w=25, h=8, txt="PythonHow")
    pdf.image("pythonhow.png", w=10)

    pdf.output(f"PDFs/{filename}.pdf")