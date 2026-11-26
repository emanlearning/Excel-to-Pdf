from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():

    pdf.add_page()

    # set the header
    pdf.set_font(size=26, style='B', family="Times")
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=16, txt=row["Topic"],
             ln=1, align='L')

    for i in range(25, 290, 10):
        pdf.line(10, i, 200, i)

    # set the footer
    pdf.ln(258)
    pdf.set_font(size=12, style='I', family="Times")
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"],
             ln=1, align='R')

    for i in range(row["Pages"] -1):

        pdf.add_page()
        # set the footer
        pdf.ln(274)
        pdf.set_font(size=12, style='I', family="Times")
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"],
                 ln=1, align='R')

        for i in range(25, 290, 10):
            pdf.line(10, i, 200, i)


pdf.output("output.pdf")