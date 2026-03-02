from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4

def generate_pdf(content):
    file_path = "generated_resume.pdf"
    doc = SimpleDocTemplate(file_path, pagesize=A4)

    styles = getSampleStyleSheet()
    elements = []

    paragraphs = content.split("\n")

    for para in paragraphs:
        elements.append(Paragraph(para, styles["Normal"]))
        elements.append(Spacer(1, 10))

    doc.build(elements)

    return file_path