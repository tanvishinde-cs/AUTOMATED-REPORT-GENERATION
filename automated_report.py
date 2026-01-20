from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import csv
from datetime import date

csv_file = r"sales_data.csv"
pdf_file = "Automated_Report.pdf"

products = []
total_sales = 0

with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        quantity = int(row["Quantity"])
        price = int(row["Price"])
        sales = quantity * price
        total_sales += sales
        products.append([row["Product"], quantity, price, sales])

doc = SimpleDocTemplate(pdf_file, pagesize=A4)
styles = getSampleStyleSheet()
elements = []

elements.append(Paragraph("<b>AUTOMATED REPORT GENERATION</b>", styles["Title"]))
elements.append(Paragraph("Internship Project – CODTECH", styles["Normal"]))
elements.append(Paragraph(f"Issued On: {date.today()}", styles["Normal"]))
elements.append(Paragraph("<br/>", styles["Normal"]))

table_data = [["Product", "Quantity", "Price", "Total"]] + products

table = Table(table_data)
table.setStyle(TableStyle([
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey)
]))

elements.append(table)
elements.append(Paragraph("<br/>", styles["Normal"]))
elements.append(Paragraph(f"<b>Grand Total Sales:</b> ₹{total_sales}", styles["Normal"]))

doc.build(elements)

print("PDF Report Generated Successfully!")
