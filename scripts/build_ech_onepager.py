from pathlib import Path
import sys

from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from update_oei_pdfs import (  # noqa: E402
    OUT,
    packet_brand_block,
    packet_callout,
    packet_card,
    packet_card_grid,
    packet_doc_for,
    packet_title,
    p,
    styles,
)


def build():
    output = OUT / "What is Entropy Compatible Hiring.pdf"
    story = [packet_brand_block(), Spacer(1, 8)]
    story += packet_title(
        "What is Entropy Compatible Hiring?",
        "Structured tools for observing operational behavior in hiring and internal contribution mapping.",
        "OEI SOFTWARE | VERSION 0.1.3 BETA",
    )
    story += [
        packet_callout(
            "A separate Windows desktop product",
            "Entropy Compatible Hiring (ECH) uses ten OEI-derived, role-agnostic archetypes and structured interview instruments. It helps teams observe how candidates respond to the operational conditions of their company, and provides a distinct module for exploring potential contributions among existing employees.",
        ),
        Spacer(1, 5),
        Paragraph("Two distinct uses", styles["PacketSection"]),
        packet_card_grid([[
            packet_card(
                "Candidate hiring",
                "Choose an archetype, add company context, review and approve an applied exercise, then record supporting, contrary, or insufficient behavioral evidence. The report supports role-specific evaluation; it does not make a hiring decision.",
            ),
            packet_card(
                "Existing Employee Contribution Mapping",
                "Employee reflection and manager observation remain separate. Their comparison highlights convergence, discrepancy, and missing evidence, then suggests an archetype for a bounded work exercise.",
            ),
        ]], [3.67 * inch, 3.67 * inch]),
        Paragraph("What ECH is designed to support", styles["PacketSection"]),
        packet_card_grid([[
            packet_card("Structured instruments", "Ten archetype-specific interview instruments with applied exercises and observation guidance."),
            packet_card("Evidence capture", "Record what was observed, what was contrary, and what remains insufficient."),
            packet_card("Reviewable reports", "Keep evidence and its context visible for human interpretation."),
        ]], [2.45 * inch, 2.45 * inch, 2.44 * inch]),
        Spacer(1, 5),
        packet_callout(
            "Clear assessment boundaries",
            "ECH records operational-behavior evidence relevant to specific OEI archetypes. It does not determine overall candidate quality or replace assessment of skills, experience, technical competence, references, or broader hiring fit. Employee contribution results are exploratory hypotheses, not performance ratings or permanent labels; validate a recommended archetype through a bounded work exercise.",
            background=colors.HexColor("#5b7a92"),
        ),
        Spacer(1, 6),
        Paragraph("Version 0.1.3 BETA | $950-$1,450 USD one-time purchase | No subscription", styles["PacketCardHead"]),
        p("Beta limitations: session data is not durable and clears when the application closes or a case concludes. AI-assisted exercise generation requires a customer-supplied OpenAI API key. Participant experiences are local pop-out windows, not remotely hosted links.", "PacketSmall"),
    ]
    packet_doc_for(output, title="What is Entropy Compatible Hiring?").build(story)
    print(output)


if __name__ == "__main__":
    build()
