from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

def generate_pdf(patient_name, wound_type, days, recommendations, filename="medical_report.pdf"):

    doc = SimpleDocTemplate(filename, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()
    story = []

    title = Paragraph("<b>Post-Surgical Wound Assessment Report</b>", styles["Title"])
    story.append(title)
    story.append(Spacer(1, 10))

    date = datetime.now().strftime("%d-%m-%Y %H:%M")
    story.append(Paragraph(f"<b>Date:</b> {date}", styles["Normal"]))
    story.append(Spacer(1, 8))

    story.append(Paragraph(f"<b>Patient Name:</b> {patient_name}", styles["Normal"]))
    story.append(Paragraph(f"<b>Detected Wound Type:</b> {wound_type}", styles["Normal"]))
    story.append(Paragraph(f"<b>Estimated Healing Time:</b> {days} days", styles["Normal"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("<b>Wound Care Recommendations:</b>", styles["Normal"]))
    story.append(Spacer(1, 6))

    for rec in recommendations:
        story.append(Paragraph(f"- {rec}", styles["Normal"]))

    story.append(Spacer(1, 15))
    story.append(Paragraph("<i>This report is generated using AI-assisted clinical decision support system.</i>", styles["Normal"]))

    doc.build(story)

    return filename
