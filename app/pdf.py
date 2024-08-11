import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle

SAVE_DIR = "generated_pdfs"
os.makedirs(SAVE_DIR, exist_ok=True)

def generate_pdf(heading: str, subheading: str, table_data: list[list[str]], base_url: str) -> str:
    if not isinstance(heading, str) or not heading.strip():
        raise ValueError("Heading must be a non-empty string")
    if not isinstance(subheading, str) or not subheading.strip():
        raise ValueError("Subheading must be a non-empty string")
    
    if not isinstance(table_data, list) or not all(isinstance(row, list) for row in table_data):
        raise ValueError("Table data must be a list of lists")
    
    if len(table_data) == 0 or len(table_data[0]) == 0:
        raise ValueError("Table data must contain at least one row and one column")
    
    pdf_filename = f"{heading.replace(' ', '_').lower()}_report.pdf"
    pdf_filepath = os.path.join(SAVE_DIR, pdf_filename)

    c = canvas.Canvas(pdf_filepath, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, heading)

    c.setFont("Helvetica", 12)
    c.drawString(100, 730, subheading)

    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    table_width, table_height = table.wrapOn(c, 400, 200)
    table.drawOn(c, 100, 700 - table_height)

    c.showPage()
    c.save()

    pdf_url = f"{base_url}/generated_pdfs/{pdf_filename}"
    return pdf_url