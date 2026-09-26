from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "info"

INK = colors.HexColor("#202427")
MUTED = colors.HexColor("#68737b")
PRIMARY = colors.HexColor("#5b7a92")
PALE = colors.HexColor("#f2f5f6")
LINE = colors.HexColor("#d7dee2")
WHITE = colors.white

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="DocTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=25, leading=29, textColor=INK, alignment=TA_LEFT, spaceAfter=8))
styles.add(ParagraphStyle(name="Subtitle", parent=styles["Normal"], fontName="Helvetica", fontSize=12, leading=16, textColor=MUTED, spaceAfter=18))
styles.add(ParagraphStyle(name="H1x", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=15, leading=18, textColor=INK, spaceBefore=12, spaceAfter=7, keepWithNext=True))
styles.add(ParagraphStyle(name="H2x", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=11.5, leading=14, textColor=INK, spaceBefore=8, spaceAfter=4, keepWithNext=True))
styles.add(ParagraphStyle(name="Bodyx", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.3, leading=13.2, textColor=INK, spaceAfter=6))
styles.add(ParagraphStyle(name="Small", parent=styles["BodyText"], fontName="Helvetica", fontSize=8, leading=10.5, textColor=MUTED, spaceAfter=4))
styles.add(ParagraphStyle(name="Bulletx", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.1, leading=12.5, leftIndent=14, firstLineIndent=-8, bulletIndent=4, textColor=INK, spaceAfter=3))
styles.add(ParagraphStyle(name="Callout", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=9.2, leading=13, textColor=INK, backColor=PALE, borderColor=LINE, borderWidth=0.5, borderPadding=10, spaceBefore=14, spaceAfter=18))
styles.add(ParagraphStyle(name="Kicker", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=7.5, leading=9, textColor=PRIMARY, spaceAfter=5))
styles.add(ParagraphStyle(name="TLDRTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=22, leading=25, textColor=INK, spaceAfter=5))
styles.add(ParagraphStyle(name="TLDRBody", parent=styles["BodyText"], fontName="Helvetica", fontSize=8.2, leading=10.5, textColor=INK, spaceAfter=4))
styles.add(ParagraphStyle(name="TLDRH", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=10, leading=12, textColor=INK, spaceBefore=6, spaceAfter=3, keepWithNext=True))


def header_footer(canvas, doc):
    canvas.saveState()
    width, height = LETTER
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.5)
    canvas.line(doc.leftMargin, height - 0.48 * inch, width - doc.rightMargin, height - 0.48 * inch)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, height - 0.38 * inch, "OEI Institute | Operational Entropy Index")
    canvas.line(doc.leftMargin, 0.48 * inch, width - doc.rightMargin, 0.48 * inch)
    canvas.drawString(doc.leftMargin, 0.33 * inch, "Operational Forensics for Growing Teams")
    canvas.drawRightString(width - doc.rightMargin, 0.33 * inch, f"Page {doc.page}")
    canvas.restoreState()


def institute_header_footer(canvas, doc):
    canvas.saveState()
    width, height = LETTER
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.5)
    canvas.line(doc.leftMargin, height - 0.48 * inch, width - doc.rightMargin, height - 0.48 * inch)
    canvas.setFont("Helvetica-Bold", 7.5)
    canvas.setFillColor(PRIMARY)
    canvas.drawString(doc.leftMargin, height - 0.38 * inch, "OEI INSTITUTE")
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawRightString(width - doc.rightMargin, height - 0.38 * inch, "Operational Forensics for Growing Teams")
    canvas.line(doc.leftMargin, 0.48 * inch, width - doc.rightMargin, 0.48 * inch)
    canvas.setFont("Helvetica", 7.5)
    canvas.drawString(doc.leftMargin, 0.33 * inch, "The Institute governs the Operational Entropy Index methodology")
    canvas.drawRightString(width - doc.rightMargin, 0.33 * inch, f"Page {doc.page}")
    canvas.restoreState()


def doc_for(path, on_page=header_footer, author="Fletcher GH Consulting"):
    doc = BaseDocTemplate(
        str(path),
        pagesize=LETTER,
        leftMargin=0.67 * inch,
        rightMargin=0.67 * inch,
        topMargin=0.66 * inch,
        bottomMargin=0.62 * inch,
        title=path.stem,
        author=author,
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="body")
    doc.addPageTemplates(PageTemplate(id="main", frames=[frame], onPage=on_page))
    return doc


def title_block(title, subtitle):
    return [Spacer(1, 0.16 * inch), Paragraph(title, styles["DocTitle"]), Paragraph(subtitle, styles["Subtitle"])]


def p(text, style="Bodyx"):
    return Paragraph(text, styles[style])


def bullet(text, style="Bulletx"):
    return Paragraph(f"&#8226; {text}", styles[style])


def h1(text):
    return Paragraph(text, styles["H1x"])


def h2(text):
    return Paragraph(text, styles["H2x"])


def pricing_table(rows):
    table = Table(rows, colWidths=[1.54 * inch, 1.02 * inch, 1.02 * inch, 1.02 * inch, 1.02 * inch, 1.02 * inch], repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), INK),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 7.2),
        ("LEADING", (0, 0), (-1, -1), 9),
        ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("GRID", (0, 0), (-1, -1), 0.35, LINE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, PALE]),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return table


def build_about():
    path = OUT / "About the Operational Entropy Index.pdf"
    story = title_block("About the Operational Entropy Index", "A current overview of the OEI framework, diagnostic method, and engagement ecosystem")
    story += [
        h1("What the OEI is"),
        p("The Operational Entropy Index (OEI) is a structured methodology for examining operational strain as organizations grow. The OEI Institute governs its canon, methodological definitions, evidence and practice standards, and deliberate evolution."),
        p("Operational entropy is the tendency for disorder, friction, and unnecessary complexity to accumulate over time. It appears when decisions require more coordination, knowledge becomes fragmented, workflows slow down, tools create workarounds, or responsibilities fail during handoffs."),
        p("Entropy cannot be permanently eliminated. The objective is to identify and mitigate it, measure whether interventions work, and establish mechanisms that help prevent it from rapidly returning."),
        Paragraph("OEI is a structured, repeatable diagnostic process. It combines evidence from people, workflows, systems, and operating outcomes rather than relying on a single opinion or generic consulting template.", styles["Callout"]),
        h1("The five OEI pillars"),
    ]
    categories = [
        ("1. Founder Dependency", "Is the company operationally hostage to one person's presence? Measures reliance on founders or other key individuals for approvals, decisions, context, and operational continuity."),
        ("2. Knowledge Logistics", "Does the right information reach the right people reliably? Examines how critical context is documented, updated, retrieved, transferred, and used."),
        ("3. Workflow Velocity", "Where is execution speed being lost in the process chain? Traces waiting, approval latency, rework, unclear ownership, and other causes of lost momentum."),
        ("4. Tool Discipline", "Are systems fit for purpose and used consistently? Evaluates tool fit, adoption, training, process alignment, redundant applications, and manual workarounds."),
        ("5. Handoff Integrity", "Do responsibility and context transfer cleanly between people or teams? Examines ownership transitions, readiness criteria, shared context, and accountability across handoffs."),
    ]
    for name, desc in categories:
        story.append(KeepTogether([h2(name), p(desc)]))
    story += [
        h1("How the OEI works"),
        bullet("<b>Structured interviews:</b> Gather evidence from people across the company, not only leadership."),
        bullet("<b>Workflow mapping:</b> Trace how work actually moves and where approvals, dependencies, or handoffs fail."),
        bullet("<b>Operational testing:</b> Measure cycle time, consistency, rework, adoption, and other observable outcomes."),
        bullet("<b>Root-cause mapping:</b> Connect visible symptoms to the structural conditions producing them."),
        h1("What an engagement produces"),
        bullet("A baseline OEI score across the five pillars."),
        bullet("A map of where execution is leaking and the root causes involved."),
        bullet("A prioritized roadmap of structural changes."),
        bullet("Proof-of-concept improvements appropriate to the engagement scope."),
        h1("Ways to work with OEI"),
        p("Organizations can develop OEI capability internally through practitioner development, or have qualified OEI practitioners perform diagnosis and methodology application. A bounded Focused Investigation is also available for a specific operational condition. The broader practitioner and commercial structure continues to develop under Institute governance."),
        h2("Focused Operational Investigations"),
        p("Founder Absence Simulation, Institutional Memory Recovery Sprint, Workflow Momentum Analysis, Operational Stack Review, and Handoff Failure Analysis are bounded investigations with a current public range of $1,000 to $4,000 USD. Each includes a 4-Day OEI Diagnosis."),
        h2("Entropy Compatible Hiring"),
        p("Entropy Compatible Hiring (ECH) Version 0.1.3 BETA is separate Windows desktop software. It provides ten role-agnostic interview instruments and an Existing Employee Contribution Mapping module."),
        p("ECH is not a personality test, does not score overall candidate quality, and does not replace evaluation of skills, experience, technical competence, references, or broader hiring fit. A formal OEI engagement is not required. ECH is offered as a one-time purchase for $950-$1,450 USD."),
    ]
    doc_for(path, on_page=header_footer, author="OEI Institute").build(story)
    return path


def engagement_block(number, title, meta, price, description, included):
    items = [p(f"{number} | {title}", "Kicker"), h2(title), p(f"<b>{meta}</b> | <b>Baseline investment: {price}</b>"), p(description)]
    items.extend(bullet(x) for x in included)
    items.append(Spacer(1, 6))
    return KeepTogether(items)


def build_services():
    path = OUT / "OEI Services and Pricing.pdf"
    story = title_block("OEI Services and Pricing", "Current capability pathways, public pricing ranges, and optional interventions")
    story += [
        p("OEI engagements are scoped according to the capability, organizational context, and level of intervention required. The Institute is developing the broader practitioner and commercial structure. Final scope and pricing are determined during engagement scoping."),
        h1("Two ways to work with OEI"),
        h2("Build capability internally"),
        p("Train and certify members of your organization to apply the OEI methodology. Practitioner development and certification pathways are taking shape under Institute governance. Current public range: $8,000-$15,000+ USD. The number of practitioners, organizational context, and supporting requirements shape final scope and pricing."),
        h2("Bring in OEI practitioners"),
        p("Have qualified practitioners perform the diagnosis and methodology application for your organization. Current public range for OEI engagements: $20,000-$45,000+ USD. Scope varies with organizational size, complexity, and the operational territory investigated and addressed."),
        h1("Focused Investigations"),
        p("A bounded entry point to investigate a specific operational domain through evidence-first OEI inquiry. Each investigation is scoped to the question and the work required; they are not identical, fixed-scope packages. Each includes a 4-Day OEI Diagnosis. Current public range: $1,000-$4,000 USD."),
        bullet("<b>Founder Absence Simulation:</b> Tests what fails, stalls, or escalates when the founder steps away."),
        bullet("<b>Institutional Memory Recovery Sprint:</b> Recovers essential knowledge trapped in people or history."),
        bullet("<b>Workflow Momentum Analysis:</b> Locates waiting, friction, and loss of execution momentum."),
        bullet("<b>Operational Stack Review:</b> Evaluates the fit and interaction of tools, systems, and workarounds."),
        bullet("<b>Handoff Failure Analysis:</b> Traces where ownership, readiness, or context breaks during transfer."),
        PageBreak(),
        h1("Optional AI Enablement"),
        p("AI Enablement may be added to either OEI pathway when findings identify a worthwhile opportunity. It is scoped from the evidence and is not an automatic part of every engagement. OEI may determine that AI is not the right response."),
        pricing_table([
            ["Indicative stage", "Planning estimate"],
            ["Investigate", "Approximately $3,500"],
            ["Design", "$2,000-$5,000"],
            ["Build & Validate", "$3,000-$12,000"],
            ["Enable & Handoff", "$1,500-$4,000"],
        ]),
        p("Illustrative overall estimates: a small intervention may be approximately $5,000-$14,000 USD; a more substantial intervention may reach $20,000-$35,000+ USD. Stages are not necessarily charged independently or delivered in sequence."),
        h1("Entropy Compatible Hiring"),
        p("ECH Version 0.1.3 BETA is separate Windows desktop software with ten role-agnostic interview instruments and an Existing Employee Contribution Mapping module. It can be used independently; a formal OEI engagement is not required. One-time purchase range: $950-$1,450 USD."),
    ]
    doc_for(path, on_page=header_footer, author="OEI Institute").build(story)
    return path


def build_tldr():
    path = OUT / "OEI TLDR.pdf"
    story = [
        Spacer(1, 0.08 * inch),
        Paragraph("OEI Institute", styles["TLDRTitle"]),
        Paragraph("Operational Forensics for Growing Teams", styles["Subtitle"]),
        Paragraph("INTERIM ONE-PAGER | SEPTEMBER 2026", styles["Kicker"]),
    ]
    story += [
        Paragraph("The OEI Institute is the governing institution for the Operational Entropy Index methodology. It exists to help growing organizations understand and address the operational strain that emerges through growth.", styles["TLDRBody"]),
        Paragraph("THE OPERATIONAL ENTROPY INDEX", styles["TLDRH"]),
        Paragraph("The Operational Entropy Index is a structured methodology for examining how operational strain develops across growing teams. It provides a shared framework for investigation, analysis, and responsible application.", styles["TLDRBody"]),
        Paragraph("THE FIVE PILLARS", styles["TLDRH"]),
        Paragraph("<b>Founder Dependency</b> - reliance on key people for decisions and continuity. &nbsp;&nbsp; <b>Knowledge Logistics</b> - whether critical information reaches the people who need it. &nbsp;&nbsp; <b>Workflow Velocity</b> - where execution loses momentum. &nbsp;&nbsp; <b>Tool Discipline</b> - whether systems are fit and consistently used. &nbsp;&nbsp; <b>Handoff Integrity</b> - whether ownership and context transfer cleanly.", styles["TLDRBody"]),
        Paragraph("OPERATIONAL FORENSICS", styles["TLDRH"]),
        Paragraph("Operational forensics examines how work actually functions through evidence. It reconstructs movement across people, systems, records, and workflows, separates observation from interpretation, tests explanations, and reaches findings that can support action.", styles["TLDRBody"]),
        Paragraph("THE INSTITUTE'S ROLE", styles["TLDRH"]),
        Paragraph("The Institute maintains the established OEI canon, methodological definitions, evidence and practice standards, and the deliberate evolution of the methodology. It is developing practitioner training, competency assessment, and certification infrastructure. It also maintains documentation, structured workflows, diagnostic tools, and software that support repeatable application.", styles["TLDRBody"]),
        Paragraph("HOW OEI REACHES ORGANIZATIONS", styles["TLDRH"]),
        Paragraph("OEI may reach organizations through Institute-maintained tools, direct engagements, and structured use of the methodology. Services and Pricing are being restructured around the Institute framework as the delivery model develops.", styles["TLDRBody"]),
        Paragraph("LEARN MORE", styles["TLDRH"]),
        Paragraph("Explore the Operational Entropy Index at /about/operational-entropy-index/ or contact the Institute to discuss an operational problem.", styles["TLDRBody"]),
    ]
    doc_for(path, on_page=institute_header_footer, author="OEI Institute").build(story)
    return path


if __name__ == "__main__":
    outputs = [build_about(), build_services(), build_tldr()]
    for output in outputs:
        print(output)
