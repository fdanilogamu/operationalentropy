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
    canvas.drawString(doc.leftMargin, height - 0.38 * inch, "Fletcher GH Consulting | Operational Entropy Index (OEI)")
    canvas.line(doc.leftMargin, 0.48 * inch, width - doc.rightMargin, 0.48 * inch)
    canvas.drawString(doc.leftMargin, 0.33 * inch, "CONFIDENTIAL & PROPRIETARY")
    canvas.drawRightString(width - doc.rightMargin, 0.33 * inch, f"Page {doc.page}")
    canvas.restoreState()


def doc_for(path):
    doc = BaseDocTemplate(
        str(path),
        pagesize=LETTER,
        leftMargin=0.67 * inch,
        rightMargin=0.67 * inch,
        topMargin=0.66 * inch,
        bottomMargin=0.62 * inch,
        title=path.stem,
        author="Fletcher GH Consulting",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="body")
    doc.addPageTemplates(PageTemplate(id="main", frames=[frame], onPage=header_footer))
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
        p("The Operational Entropy Index (OEI) is a proprietary diagnostic tool and structured intervention process built to identify, measure, and reduce the organizational drag that erodes execution speed as companies scale."),
        p("Operational entropy is the tendency for disorder, friction, and unnecessary complexity to accumulate over time. It appears when decisions require more coordination, knowledge becomes fragmented, workflows slow down, tools create workarounds, or responsibilities fail during handoffs."),
        p("Entropy cannot be permanently eliminated. The objective is to identify and mitigate it, measure whether interventions work, and establish mechanisms that help prevent it from rapidly returning."),
        Paragraph("OEI is a structured, repeatable diagnostic process. It combines evidence from people, workflows, systems, and operating outcomes rather than relying on a single opinion or generic consulting template.", styles["Callout"]),
        h1("The five diagnostic categories"),
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
        bullet("A baseline OEI score across the five dimensions."),
        bullet("A map of where execution is leaking and the root causes involved."),
        bullet("A prioritized roadmap of structural changes."),
        bullet("Proof-of-concept improvements appropriate to the engagement scope."),
        h1("Ways to work with OEI"),
        p("The consulting pathway includes an Initial OEI Diagnosis, 15- or 30-Day Audits, a 30-Day Single Pain Point Sprint, a 90-Day Operational Entropy Reset, and One-Year OEI Trend Analysis. Most comprehensive work starts with the diagnosis, while focused investigations provide a faster route when the problem is already visible."),
        h2("Focused Operational Investigations"),
        p("Founder Absence Simulation, Institutional Memory Recovery Sprint, Workflow Momentum Analysis, Operational Stack Review, and Handoff Failure Analysis are bounded investigations typically priced from $500 to $2,000 USD."),
        h2("Entropy Compatible Hiring"),
        p("Entropy Compatible Hiring (ECH) is separate Windows desktop software. It provides ten role-agnostic, OEI-derived interview instruments that help organizations observe operational behavior through applied exercises, predefined signals, and evidence capture."),
        p("ECH is not a personality test, does not score overall candidate quality, and does not replace evaluation of skills, experience, technical competence, references, or broader hiring fit. A formal OEI engagement is not required. Version 0.1.0 BETA is offered as a one-time purchase for $950-$1,450 USD."),
    ]
    doc_for(path).build(story)
    return path


def engagement_block(number, title, meta, price, description, included):
    items = [p(f"{number} | {title}", "Kicker"), h2(title), p(f"<b>{meta}</b> | <b>Baseline investment: {price}</b>"), p(description)]
    items.extend(bullet(x) for x in included)
    items.append(Spacer(1, 6))
    return KeepTogether(items)


def build_services():
    path = OUT / "OEI Services and Pricing.pdf"
    story = title_block("OEI Services and Pricing", "Current engagement paths, prerequisites, deliverables, and revenue-based pricing")
    story += [
        p("Every engagement begins with a discovery call. Most comprehensive work starts with the Initial Diagnosis, which delivers standalone value and provides the baseline for deeper analysis. Prices below are baseline for companies under $5M in annual revenue unless otherwise noted."),
        h1("Core engagement paths"),
        engagement_block("01", "Initial OEI Diagnosis", "Standalone | 4 days", "$2,000", "Structured interviews, workflow mapping, operational testing, and measurement produce an initial view of where operating speed is leaking.", ["Baseline OEI score across five dimensions", "Executive summary and prioritized next steps"]),
        engagement_block("02A", "15-Day OEI Audit", "Requires Initial Diagnosis | 15 days", "$8,000", "A shorter deep-dive for simpler analyses, fewer monitored areas, or a more focused depth of inquiry.", ["Focused root-cause findings", "Recommendations roadmap", "Quarterly check-in included"]),
        engagement_block("02B", "30-Day OEI Audit", "Requires Initial Diagnosis | 30 days", "$15,000", "A comprehensive audit for broader monitoring, deeper analysis, and a fuller operational map.", ["Detailed root-cause mapping and documentation review", "Benchmarking context and prioritized roadmap", "Quarterly check-in included"]),
        engagement_block("03", "30-Day Single Pain Point Sprint", "Requires Diagnosis + Audit | 30 days", "$25,000", "A focused structural intervention for one clearly defined, high-impact bottleneck.", ["Implementation support and change management", "Training where necessary", "30-day post-launch monitoring", "Quarterly check-ins for six months"]),
        engagement_block("04", "90-Day Operational Entropy Reset", "Requires Diagnosis + Audit | 90 days", "$45,000", "Structural fixes for the top three interconnected bottlenecks identified through the audit.", ["Process redesign and full implementation", "Leadership and team coaching where necessary", "Systems and tool optimization", "90-day post-launch support and quarterly check-ins"]),
        engagement_block("05", "One-Year OEI Trend Analysis", "Standalone; completed or active engagement recommended | 4 quarterly sessions", "$5,000 per year", "Quarterly measurement that tracks how entropy shifts, verifies whether fixes hold, and identifies new patterns early.", ["OEI score remeasurement", "Updated recommendations each quarter", "Year-round support"]),
        PageBreak(),
        h1("Revenue-based pricing"),
        p("Core consulting fees scale with verified annual revenue. Companies at $100M+ receive custom pricing scoped to the organization."),
        pricing_table([
            ["Engagement", "Under $5M", "$5M-$25M", "$25M-$50M", "$50M-$100M", "$100M+"],
            ["Diagnosis", "$2,000", "$2,500", "$3,000", "$3,500", "Custom"],
            ["15-Day Audit", "$8,000", "$10,000", "$12,000", "$14,000", "Custom"],
            ["30-Day Audit", "$15,000", "$18,750", "$22,500", "$26,250", "Custom"],
            ["30-Day Sprint", "$25,000", "$31,250", "$37,500", "$43,750", "Custom"],
            ["90-Day Reset", "$45,000", "$56,250", "$67,500", "$78,750", "Custom"],
            ["One-Year Trend", "$5,000", "$6,250", "$7,500", "$8,750", "Custom"],
        ]),
        Spacer(1, 10),
        h1("Focused Operational Investigations"),
        p("When the operating problem is already visible, a focused investigation may be used without completing the comprehensive OEI pathway. Typical investment: $500-$2,000 USD."),
        bullet("<b>Founder Absence Simulation:</b> Tests what fails, stalls, or escalates when the founder steps away."),
        bullet("<b>Institutional Memory Recovery Sprint:</b> Recovers essential knowledge trapped in people or history."),
        bullet("<b>Workflow Momentum Analysis:</b> Locates waiting, friction, and loss of execution momentum."),
        bullet("<b>Operational Stack Review:</b> Evaluates the fit and interaction of tools, systems, and workarounds."),
        bullet("<b>Handoff Failure Analysis:</b> Traces where ownership, readiness, or context breaks during transfer."),
        h1("Entropy Compatible Hiring software"),
        p("ECH Version 0.1.0 BETA is a separate Windows desktop product with ten role-agnostic interview instruments. It can be used with OEI findings or independently and does not replace role-specific hiring evaluation."),
        Paragraph("One-time Beta pricing: $950-$1,450 USD. ECH pricing is not scaled by company revenue.", styles["Callout"]),
        h1("Pathway and payment notes"),
        bullet("The Initial Diagnosis is standalone; audits require the diagnosis."),
        bullet("The 30-Day Sprint and 90-Day Reset require both diagnosis and audit."),
        bullet("One-Year Trend Analysis is standalone, but is most useful with a completed or active engagement."),
        bullet("Focused investigations and ECH may be accessed independently."),
        bullet("Diagnosis and One-Year Trend Analysis are paid upfront. Longer consulting engagements are paid 50% upfront and 50% at the midpoint."),
        bullet("Travel, custom tool development, permanent staff augmentation, and implementation beyond the engagement window are outside standard pricing."),
    ]
    doc_for(path).build(story)
    return path


def build_tldr():
    path = OUT / "OEI TLDR.pdf"
    story = [Spacer(1, 0.08 * inch), Paragraph("Operational Entropy Index (OEI)", styles["TLDRTitle"]), Paragraph("One-page overview", styles["Subtitle"])]
    story += [
        Paragraph("OEI identifies, measures, and reduces the friction, dependency, and unnecessary complexity that accumulate as organizations scale. Entropy cannot be permanently eliminated; OEI helps organizations mitigate it and build mechanisms that keep it from rapidly returning.", styles["TLDRBody"]),
        Paragraph("WHAT OEI EXAMINES", styles["TLDRH"]),
        Paragraph("<b>Founder Dependency</b> - reliance on key people for decisions and continuity. &nbsp;&nbsp; <b>Knowledge Logistics</b> - whether critical information reaches the people who need it. &nbsp;&nbsp; <b>Workflow Velocity</b> - where execution loses momentum. &nbsp;&nbsp; <b>Tool Discipline</b> - whether systems are fit and consistently used. &nbsp;&nbsp; <b>Handoff Integrity</b> - whether ownership and context transfer cleanly.", styles["TLDRBody"]),
        Paragraph("HOW IT WORKS", styles["TLDRH"]),
        Paragraph("Structured interviews, workflow mapping, operational testing, and root-cause mapping produce a baseline OEI score, a map of operating leaks, and prioritized next steps.", styles["TLDRBody"]),
        Paragraph("CORE ENGAGEMENTS - BASELINE PRICING", styles["TLDRH"]),
    ]
    rows = [
        ["Engagement", "Duration", "Prerequisite", "From"],
        ["Initial OEI Diagnosis", "4 days", "None", "$2,000"],
        ["15-Day OEI Audit", "15 days", "Diagnosis", "$8,000"],
        ["30-Day OEI Audit", "30 days", "Diagnosis", "$15,000"],
        ["Single Pain Point Sprint", "30 days", "Diagnosis + audit", "$25,000"],
        ["Operational Entropy Reset", "90 days", "Diagnosis + audit", "$45,000"],
        ["One-Year Trend Analysis", "4 quarterly sessions", "None; engagement recommended", "$5,000/year"],
    ]
    table = Table(rows, colWidths=[2.22 * inch, 1.35 * inch, 2.2 * inch, 0.98 * inch], repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), INK), ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"), ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 7.4), ("LEADING", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.35, LINE), ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, PALE]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("TOPPADDING", (0, 0), (-1, -1), 4.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5),
    ]))
    story += [table,
        Paragraph("Pricing shown is baseline for companies under $5M in annual revenue and scales by revenue tier. $100M+ engagements are custom scoped.", styles["Small"]),
        Paragraph("OTHER WAYS TO START", styles["TLDRH"]),
        Paragraph("<b>Focused Operational Investigations:</b> Five bounded investigations for already-visible problems, typically $500-$2,000 USD. <b>Entropy Compatible Hiring:</b> Separate Windows desktop Beta software with ten role-agnostic interview instruments; $950-$1,450 USD as a one-time purchase. Neither requires a formal OEI engagement.", styles["TLDRBody"]),
        Paragraph("PATHWAY RULE", styles["TLDRH"]),
        Paragraph("Most comprehensive work starts with the Initial Diagnosis. Audits require diagnosis; sprints and resets require diagnosis plus audit. One-Year Trend Analysis is standalone but most useful with a completed or active engagement.", styles["TLDRBody"]),
    ]
    doc_for(path).build(story)
    return path


if __name__ == "__main__":
    outputs = [build_about(), build_services(), build_tldr()]
    for output in outputs:
        print(output)
