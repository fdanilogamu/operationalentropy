from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    Image,
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
styles.add(ParagraphStyle(name="PacketKicker", fontName="Helvetica-Bold", fontSize=7.5, leading=10, textColor=PRIMARY, spaceAfter=5))
styles.add(ParagraphStyle(name="PacketTitle", fontName="Helvetica-Bold", fontSize=23, leading=26, textColor=INK, spaceAfter=4))
styles.add(ParagraphStyle(name="PacketSubtitle", fontName="Helvetica", fontSize=11, leading=14, textColor=PRIMARY, spaceAfter=9))
styles.add(ParagraphStyle(name="PacketSection", fontName="Helvetica-Bold", fontSize=12, leading=15, textColor=INK, spaceBefore=5, spaceAfter=6, keepWithNext=True))
styles.add(ParagraphStyle(name="PacketBody", fontName="Helvetica", fontSize=9, leading=12.5, textColor=INK, spaceAfter=5))
styles.add(ParagraphStyle(name="PacketSmall", fontName="Helvetica", fontSize=8, leading=10.5, textColor=MUTED))
styles.add(ParagraphStyle(name="PacketCardHead", fontName="Helvetica-Bold", fontSize=9, leading=11, textColor=INK, spaceAfter=3))
styles.add(ParagraphStyle(name="PacketCardBody", fontName="Helvetica", fontSize=8, leading=10.5, textColor=MUTED))
styles.add(ParagraphStyle(name="PacketDarkHead", fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=WHITE, spaceAfter=3))
styles.add(ParagraphStyle(name="PacketDarkBody", fontName="Helvetica", fontSize=8.4, leading=11.4, textColor=WHITE))
styles.add(ParagraphStyle(name="PacketHeaderRight", fontName="Helvetica", fontSize=7.5, leading=10, textColor=MUTED, alignment=2))
styles.add(ParagraphStyle(name="PacketHeaderKicker", fontName="Helvetica-Bold", fontSize=7.5, leading=10, textColor=PRIMARY, alignment=2, spaceAfter=3))


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


def packet_header_footer(canvas, doc):
    canvas.saveState()
    width, height = LETTER
    canvas.line(doc.leftMargin, 0.42 * inch, width - doc.rightMargin, 0.42 * inch)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 0.26 * inch, "The Institute governs the Operational Entropy Index methodology")
    canvas.drawRightString(width - doc.rightMargin, 0.26 * inch, f"Page {doc.page}")
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


def packet_doc_for(path, title=None):
    doc = BaseDocTemplate(
        str(path), pagesize=LETTER, leftMargin=0.58 * inch, rightMargin=0.58 * inch,
        topMargin=0.88 * inch, bottomMargin=0.62 * inch,
        title=title or path.stem, author="OEI Institute",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="packet-body")
    doc.addPageTemplates(PageTemplate(id="packet", frames=[frame], onPage=packet_header_footer))
    return doc


def packet_title(title, subtitle, kicker="OEI INSTITUTE | INFORMATION PACKET"):
    return [Paragraph(kicker, styles["PacketKicker"]), Paragraph(title, styles["PacketTitle"]), Paragraph(subtitle, styles["PacketSubtitle"])]


def packet_brand_block():
    logo = Image(str(ROOT / "images" / "oei-institute-logo.png"), width=1.72 * inch, height=0.52 * inch)
    header = Table([[logo, [
        Paragraph("OEI INSTITUTE", styles["PacketHeaderKicker"]),
        Paragraph("Operational Forensics for Growing Teams", styles["PacketHeaderRight"]),
    ]]], colWidths=[2 * inch, 5.34 * inch])
    header.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ("LINEBELOW", (0, 0), (-1, -1), 0.8, LINE), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
    ]))
    return header


def packet_card(title, body):
    return Table([[Paragraph(title, styles["PacketCardHead"])], [Paragraph(body, styles["PacketCardBody"])]], style=TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PALE), ("BOX", (0, 0), (-1, -1), 0.6, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 9), ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))


def packet_card_grid(rows, widths):
    table = Table(rows, colWidths=widths, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 2),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5), ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return table


def packet_callout(title, body, background=INK):
    table = Table([[Paragraph(title, styles["PacketDarkHead"])], [Paragraph(body, styles["PacketDarkBody"])]], colWidths=[7.34 * inch])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), background),
        ("LEFTPADDING", (0, 0), (-1, -1), 11), ("RIGHTPADDING", (0, 0), (-1, -1), 11),
        ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return table


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
    story = [packet_brand_block(), Spacer(1, 8)]
    story += packet_title("About the Operational Entropy Index", "A governed methodology for investigating operational strain and supporting responsible action")
    story += [
        packet_callout("The Institute governs. The method investigates.", "The OEI Institute maintains the Operational Entropy Index canon and practice standards. OEI gives organizations a shared way to examine how strain develops as work, people, and systems grow."),
        Spacer(1, 8),
        Paragraph("What the OEI examines", styles["PacketSection"]),
        p("Operational entropy is friction and unnecessary complexity that accumulate in how work gets done. It can appear as delayed decisions, fragmented knowledge, slow or restarted workflows, tool workarounds, or failed handoffs. OEI examines operating conditions through evidence rather than relying on a single perspective.", "PacketBody"),
        Paragraph("The five OEI pillars", styles["PacketSection"]),
    ]
    pillars = [
        packet_card("Founder Dependency", "Reliance on key people for decisions, context, or continuity."),
        packet_card("Knowledge Logistics", "Whether critical information reaches people in usable form."),
        packet_card("Workflow Velocity", "Where work waits, stalls, restarts, or accumulates rework."),
        packet_card("Tool Discipline", "Whether tools support the work or create more friction."),
        packet_card("Handoff Integrity", "Whether ownership and context transfer reliably."),
    ]
    story.append(packet_card_grid([[pillars[0], pillars[1]], [pillars[2], pillars[3]], [pillars[4], ""]], [3.67 * inch, 3.67 * inch]))
    story += [
        Spacer(1, 4),
        Paragraph("How OEI builds a useful picture", styles["PacketSection"]),
        packet_card_grid([
            [packet_card("Gather evidence", "Structured interviews and operational records bring multiple perspectives into view."), packet_card("Trace real work", "Workflow mapping follows decisions, information, tools, dependencies, and handoffs.")],
            [packet_card("Test what happens", "Operational samples help distinguish stated process from observed practice."), packet_card("Connect causes", "Root-cause mapping links visible friction to the conditions producing it.")],
        ], [3.67 * inch, 3.67 * inch]),
        PageBreak(),
        packet_brand_block(),
        Spacer(1, 8),
        Paragraph("From investigation to application", styles["PacketTitle"]),
        Paragraph("OEI supports a clearer response by separating what is observed, what it may mean, and what the evidence can support.", styles["PacketSubtitle"]),
        Paragraph("What OEI can produce", styles["PacketSection"]),
        packet_card_grid([[
            packet_card("A baseline", "A structured view of the operating condition and relevant OEI pillars."),
            packet_card("A causal map", "Evidence connecting observed friction with its underlying conditions."),
        ], [
            packet_card("Priorities", "A grounded view of where action is most likely to improve the work."),
            packet_card("A way to learn", "Measures that help teams assess whether an intervention improves operations."),
        ]], [3.67 * inch, 3.67 * inch]),
        Spacer(1, 6),
        Paragraph("How organizations work with OEI", styles["PacketSection"]),
        packet_card_grid([[
            packet_card("Build internal capability", "Develop practitioner capability through training and certification pathways as they take shape under Institute governance."),
            packet_card("Work with practitioners", "Qualified practitioners investigate and apply OEI to an organization's operating context."),
        ]], [3.67 * inch, 3.67 * inch]),
        Spacer(1, 7),
        packet_callout("AI Enablement Through OEI", "AI Enablement can be a starting route for an existing AI initiative or an intervention when OEI findings support it. The work investigates the operating condition, tests whether a governed AI capability can improve it, and follows the evidence. AI is not an OEI pillar or an automatic solution. The right outcome may be to modify, stop, or not proceed.", PRIMARY),
        Spacer(1, 6),
        p("Focused investigations examine a bounded operating condition. Entropy Compatible Hiring (ECH) is a separate software product that supports structured hiring interviews and existing-employee contribution mapping; it can be used independently of a formal OEI engagement.", "PacketSmall"),
    ]
    packet_doc_for(path).build(story)
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
    story = [packet_brand_block(), Spacer(1, 8)]
    story += packet_title("OEI Institute Overview", "Operational Forensics for Growing Teams", "INSTITUTE OVERVIEW | SEPTEMBER 2026")
    story += [
        packet_callout("The Institute governs. OEI is the methodology.", "The OEI Institute maintains the methodology's canon, definitions, evidence and practice standards, and deliberate evolution. OEI gives teams a shared framework for investigating how operational strain develops as organizations grow."),
        Spacer(1, 7),
        Paragraph("What the Institute does", styles["PacketSection"]),
        packet_card_grid([[
            packet_card("Govern", "Maintain the established method and its practice standards."),
            packet_card("Develop", "Build practitioner capability and pathways for responsible application."),
            packet_card("Support", "Maintain documentation, workflows, tools, and software."),
        ]], [2.45 * inch, 2.45 * inch, 2.44 * inch]),
        Paragraph("The five OEI pillars", styles["PacketSection"]),
        packet_card_grid([[
            packet_card("Founder Dependency", "Key-person reliance"),
            packet_card("Knowledge Logistics", "Information access and movement"),
            packet_card("Workflow Velocity", "How work moves"),
        ], [
            packet_card("Tool Discipline", "How tools support work"),
            packet_card("Handoff Integrity", "Transfer of ownership and context"),
            "",
        ]], [2.45 * inch, 2.45 * inch, 2.44 * inch]),
        Paragraph("A method for responsible application", styles["PacketSection"]),
        p("Operational forensics examines work as it functions in practice. OEI combines interviews, workflow observation, records, operational samples, and structured analysis to distinguish observation from interpretation, test explanations, and support action grounded in evidence.", "PacketBody"),
        packet_callout("AI Enablement Through OEI", "AI Enablement is one way to begin when an organization has an AI initiative or mandate and needs to know whether AI can improve consequential work. It can also follow OEI findings as a justified intervention. AI is not an OEI pillar, and the evidence may support changing course or not proceeding.", PRIMARY),
        Spacer(1, 7),
        p("Organizations can develop OEI capability internally or work with qualified OEI practitioners. Focused investigations offer a bounded way to examine a specific operating condition. The broader practitioner and commercial structure continues to develop.", "PacketSmall"),
    ]
    packet_doc_for(path, title="OEI Institute Overview").build(story)
    return path


if __name__ == "__main__":
    outputs = [build_about(), build_services(), build_tldr()]
    for output in outputs:
        print(output)
