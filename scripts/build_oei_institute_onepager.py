from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "info" / "What is the OEI Institute.pdf"
LOGO = ROOT / "images" / "oei-institute-logo.png"

INK = colors.HexColor("#18232b")
BLUE = colors.HexColor("#5b7a92")
PALE = colors.HexColor("#eef3f5")
PAPER = colors.HexColor("#f5f6f4")
MUTED = colors.HexColor("#59656d")
WHITE = colors.white
LINE = colors.HexColor("#d7dee2")

styles = {
    "kicker": ParagraphStyle("Kicker", fontName="Helvetica-Bold", fontSize=7.5, leading=10, textColor=BLUE, alignment=TA_RIGHT, spaceAfter=3),
    "micro": ParagraphStyle("Micro", fontName="Helvetica", fontSize=8, leading=11, textColor=MUTED, alignment=TA_RIGHT),
    "title": ParagraphStyle("Title", fontName="Helvetica-Bold", fontSize=25, leading=28, textColor=INK, spaceAfter=5),
    "subtitle": ParagraphStyle("Subtitle", fontName="Helvetica", fontSize=12, leading=16, textColor=BLUE, spaceAfter=8),
    "body": ParagraphStyle("Body", fontName="Helvetica", fontSize=9.2, leading=13, textColor=INK, spaceAfter=5),
    "section": ParagraphStyle("Section", fontName="Helvetica-Bold", fontSize=12, leading=15, textColor=INK, spaceBefore=5, spaceAfter=6),
    "cardhead": ParagraphStyle("CardHead", fontName="Helvetica-Bold", fontSize=9.1, leading=12, textColor=INK, spaceAfter=4),
    "cardbody": ParagraphStyle("CardBody", fontName="Helvetica", fontSize=8.1, leading=11, textColor=MUTED),
    "pillars": ParagraphStyle("Pillars", fontName="Helvetica", fontSize=8.2, leading=12, textColor=INK),
    "callhead": ParagraphStyle("CallHead", fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=WHITE, spaceAfter=4),
    "callbody": ParagraphStyle("CallBody", fontName="Helvetica", fontSize=8.6, leading=12, textColor=WHITE),
    "footer": ParagraphStyle("Footer", fontName="Helvetica", fontSize=7.5, leading=10, textColor=MUTED),
}


def on_page(canvas, doc):
    canvas.saveState()
    width, height = letter
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.6)
    canvas.line(doc.leftMargin, 0.42 * inch, width - doc.rightMargin, 0.42 * inch)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 0.25 * inch, "OEI Institute | Operational Forensics for Growing Teams")
    canvas.drawRightString(width - doc.rightMargin, 0.25 * inch, "operationalentropy.com")
    canvas.restoreState()


def card(title, body):
    return [Paragraph(title, styles["cardhead"]), Paragraph(body, styles["cardbody"])]


def build():
    doc = SimpleDocTemplate(
        str(OUTPUT), pagesize=letter, rightMargin=0.58 * inch,
        leftMargin=0.58 * inch, topMargin=0.42 * inch, bottomMargin=0.62 * inch,
        title="What is the OEI Institute?", author="OEI Institute",
    )
    logo = Image(str(LOGO), width=1.72 * inch, height=0.52 * inch)
    header = Table(
        [[logo, [Paragraph("GOVERNING INSTITUTION", styles["kicker"]), Paragraph("Operational Forensics for Growing Teams", styles["micro"])]]],
        colWidths=[2.0 * inch, 4.86 * inch],
    )
    header.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ("LINEBELOW", (0, 0), (-1, -1), 0.8, LINE),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
    ]))

    story = [header, Spacer(1, 0.18 * inch)]
    story += [
        Paragraph("What is the OEI Institute?", styles["title"]),
        Paragraph("The institution that governs the Operational Entropy Index methodology.", styles["subtitle"]),
        Paragraph(
            "The OEI Institute maintains the methodology's canon, definitions, evidence and practice standards, and its deliberate evolution. It supports consistent application through practitioner capability, documentation, structured workflows, diagnostic tools, and software.",
            styles["body"],
        ),
    ]

    identity = Table([[Paragraph(
        "<b>OEI Institute</b> is the governing institution. &nbsp;&nbsp; <b>Operational Entropy Index (OEI)</b> is the methodology it governs.",
        ParagraphStyle("Identity", fontName="Helvetica", fontSize=9.2, leading=13, textColor=WHITE),
    )]], colWidths=[6.86 * inch])
    identity.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), INK),
        ("BOX", (0, 0), (-1, -1), 0, INK),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    story += [identity, Spacer(1, 0.1 * inch), Paragraph("What the Institute does", styles["section"])]

    cards = Table([[ 
        card("Governs the method", "Maintains the established OEI canon, methodological definitions, and standards for evidence and practice."),
        card("Develops capability", "Builds practitioner development, competency assessment, and certification pathways under Institute governance."),
        card("Supports application", "Maintains documentation, workflows, tools, and software that support repeatable use of OEI."),
    ]], colWidths=[2.22 * inch, 2.22 * inch, 2.22 * inch])
    cards.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PAPER),
        ("BOX", (0, 0), (-1, -1), 0.6, LINE),
        ("INNERGRID", (0, 0), (-1, -1), 0.6, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    story += [cards, Spacer(1, 0.08 * inch)]
    story += [Paragraph(
        "<b>The five OEI pillars:</b> Founder Dependency; Knowledge Logistics; Workflow Velocity; Tool Discipline; Handoff Integrity",
        styles["pillars"],
    ), Paragraph("How organizations work with OEI", styles["section"])]

    routes = Table([[
        [Paragraph("Build internal capability", styles["cardhead"]), Paragraph("Develop staff capability through practitioner training and certification pathways as they take shape.", styles["cardbody"])],
        [Paragraph("Work with practitioners", styles["cardhead"]), Paragraph("Qualified OEI practitioners investigate and apply the methodology to an organization's operating context.", styles["cardbody"])],
    ]], colWidths=[3.43 * inch, 3.43 * inch])
    routes.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PALE),
        ("BOX", (0, 0), (-1, -1), 0.6, LINE),
        ("INNERGRID", (0, 0), (-1, -1), 0.6, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 11),
        ("RIGHTPADDING", (0, 0), (-1, -1), 11),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    story += [routes, Spacer(1, 0.09 * inch)]

    ai = Table([[
        Paragraph("AI Enablement Through OEI", styles["callhead"]),
        Paragraph(
            "AI Enablement applies OEI to consequential work where an organization needs to understand an AI opportunity, investigate the operating condition, and decide what evidence supports. It can be a starting route for an existing AI initiative, or an intervention when OEI findings justify it. AI is one possible response - not an OEI pillar or an automatic solution. The right result may be to modify, stop, or not proceed.",
            styles["callbody"],
        ),
    ]], colWidths=[1.72 * inch, 5.14 * inch])
    ai.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BLUE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 11),
        ("RIGHTPADDING", (0, 0), (-1, -1), 11),
        ("TOPPADDING", (0, 0), (-1, -1), 11),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 11),
    ]))
    story += [ai, Spacer(1, 0.08 * inch), Paragraph(
        'The broader practitioner and commercial structure continues to develop. Learn more at '
        '<link href="https://operationalentropy.com/about/" color="#5b7a92">operationalentropy.com/about/</link> '
        'and <link href="https://operationalentropy.com/ai-enablement/" color="#5b7a92">operationalentropy.com/ai-enablement/</link>.',
        styles["footer"],
    )]

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(OUTPUT)


if __name__ == "__main__":
    build()
