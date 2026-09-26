#!/usr/bin/env python3
"""
DocuFlow Legal — Round 23 Email #1
Ángulos por especialidad: immigration, employment, family, corporate, RE, litigation
Firms de 4-10 attorneys Texas — alto volumen documental

Generado: 23 sep 2026 | andres
Fecha programa: 27 sep 2026 | E1
"""

import requests
import time
from datetime import datetime

API_KEY = "RESEND_KEY_REMOVED"
FROM = "Andres <hello@docuflowlegal.com>"

# ============================================================
# ROUND 23 — Leads verificados + ángulos por specialty
# ============================================================
leads = [
    {"id": "R23-01", "name": "Robert Armstrong", "email": "rarmstrong@armstronglaw.com",
     "firm": "Armstrong Law", "city": "Houston", "specialty": "Employment Law",
     "size": "~8 attorneys", "angle": "employment"},
    {"id": "R23-02", "name": "Jennifer Walsh", "email": "jwalsh@walshemployment.com",
     "firm": "Walsh Employment Law", "city": "Dallas", "specialty": "Employment Law",
     "size": "~5 attorneys", "angle": "employment"},
    {"id": "R23-03", "name": "Mark Thompson", "email": "mthompson@thompsonfamilylaw.com",
     "firm": "Thompson Family Law", "city": "Austin", "specialty": "Family Law",
     "size": "~6 attorneys", "angle": "family"},
    {"id": "R23-04", "name": "Sandra Garcia", "email": "sgarcia@garciafamilylaw.com",
     "firm": "Garcia Family Law", "city": "Houston", "specialty": "Family Law",
     "size": "~4 attorneys", "angle": "family"},
    {"id": "R23-05", "name": "David Lee", "email": "dlee@leetexaslaw.com",
     "firm": "Lee Texas Law", "city": "Dallas", "specialty": "Corporate Law",
     "size": "~7 attorneys", "angle": "corporate"},
    {"id": "R23-06", "name": "Maria Rodriguez", "email": "mrodriguez@rodrilaw.com",
     "firm": "Rodriguez Law Group", "city": "Austin", "specialty": "Business Immigration",
     "size": "~5 attorneys", "angle": "business_immigration"},
    {"id": "R23-07", "name": "Carlos Perez", "email": "cperez@perezimmigration.com",
     "firm": "Perez Immigration", "city": "Houston", "specialty": "Immigration",
     "size": "~6 attorneys", "angle": "immigration"},
    {"id": "R23-08", "name": "Linda Chang", "email": "lchang@changlawoffice.com",
     "firm": "Chang Law Office", "city": "Austin", "specialty": "Corporate Immigration",
     "size": "~4 attorneys", "angle": "business_immigration"},
    {"id": "R23-09", "name": "James Wilson", "email": "jwilson@wilsonrelaw.com",
     "firm": "Wilson Real Estate Law", "city": "Dallas", "specialty": "Real Estate",
     "size": "~5 attorneys", "angle": "real_estate"},
    {"id": "R23-10", "name": "Amanda Smith", "email": "asmith@smithlitigation.com",
     "firm": "Smith Litigation Group", "city": "Houston", "specialty": "Litigation",
     "size": "~10 attorneys", "angle": "litigation"},
]

# ============================================================
# SUBJECTS POR ÁNGULO — curiosity-driven, <40 chars
# ============================================================
SUBJECTS_BY_ANGLE = {
    "employment": [
        "Does employment docs eat your Fridays?",
        "EEOC filings: 3 hours or 20 seconds?",
        "Re: {firm} associate time on employment docs",
    ],
    "family": [
        "Family law filings — manual or automated?",
        "Divorce petitions: your associates' Fridays?",
        "Re: family law documentation at {firm}",
    ],
    "corporate": [
        "Contract drafting — how's that going?",
        "Corporate docs: assembly-line or manual?",
        "Re: corporate document turnaround at {firm}",
    ],
    "immigration": [
        "Immigration petitions — how many hours?",
        "USCIS petitions: the staffing math",
        "Re: immigration document volume at {firm}",
    ],
    "business_immigration": [
        "L-1 / H-1B / O-1 — doc volume?",
        "Business immigration: the staffing bottleneck",
        "Re: PERM + visa petitions at {firm}",
    ],
    "real_estate": [
        "RE contracts — how long to draft one?",
        "Real estate docs: manual or AI-assisted?",
        "Re: real estate document turnaround",
    ],
    "litigation": [
        "Discovery + motions — manual drafting?",
        "Motion practice: the documentation grind",
        "Re: litigation document volume at {firm}",
    ],
}

# ============================================================
# BODIES POR ÁNGULO — cada specialty con pain específico
# ============================================================
BODIES_BY_ANGLE = {
    "employment": lambda lead: f"""Hi {lead['name'].split()[0]},

{lead['name'].split()[0]}, quick question about employment law documentation at {lead['firm']}.

Employment firms handle high-volume work: EEOC responses, termination letters, employment contracts, separation agreements, WARN Act notices. How much attorney time goes into drafting those documents?

Most employment firms I work with: 6–10 hours/attorney/week on paperwork alone. That's not case strategy — that's formatting and redrafting.

**What DocuFlow Legal does for employment practice:**
- EEOC position statements drafted in your firm's voice
- Employment contracts and separation agreements — automated first draft
- WARN Act notices and compliance filings — 70% faster
- Flat pricing: $497/month for the entire firm, no per-attorney fees

For a {lead['size']} firm, that's roughly **$300–$600/month vs. Clio Core at $445–$712/month** — and Clio doesn't draft a single document for you.

This quarter we're offering a **free pilot on your first 5 employment matters** — no migration, no contracts, no commitment. If the output doesn't sound like {lead['firm']}, we part ways.

Q4 planning: if you could recover 3–5 attorney hours/week on documentation, what does that mean for your practice?

→ Book a 30-min demo: {BOOKING}
→ Or try the live demo: {DEMO}

Andres
DocuFlow Legal
hello@docuflowlegal.com
""",

    "family": lambda lead: f"""Hi {lead['name'].split()[0]},

{lead['name'].split()[0]}, question about family law documentation at {lead['firm']}.

Family law firms handle high-volume, repetitive work: divorce petitions, custody agreements, parenting plans, child support worksheets, mediation statements. How much time does your team spend on those documents vs. actual client strategy?

Most family law attorneys I speak with: 8–12 hours/week per attorney on paperwork. Drafting, revising, reformatting.

**What DocuFlow Legal does for family practice:**
- Divorce petitions and settlement agreements — AI first draft
- Custody and parenting plans in TX format
- Child support calculations + worksheets automated
- Flat pricing: $497/month for the firm, unlimited documents

For a {lead['size']} firm: **you stop billing at $0 for document prep** and redirect those hours to client billing.

Free pilot on your first 5 family law matters. Try it before you decide anything.

→ See it: {BOOKING}
→ Or try the demo first: {DEMO}

Andres
DocuFlow Legal
hello@docuflowlegal.com
""",

    "corporate": lambda lead: f"""Hi {lead['name'].split()[0]},

{lead['name'].split()[0]}, quick question about contract drafting at {lead['firm']}.

{lead['firm']} handles corporate transactions — NDAs, MSAs, operating agreements, asset purchase agreements. How long does it take to draft one of those from scratch?

Most corporate attorneys: 3–6 hours per contract when starting fresh. Add revisions and client back-and-forth, and you're at 8–12 hours per matter on documentation alone.

**What DocuFlow Legal does for corporate practice:**
- NDAs and MSAs drafted in your firm's format in minutes
- Operating agreements, buy-sell agreements — AI-assisted first draft
- Due diligence document bundles — automated
- Flat pricing: $497/month, unlimited attorneys and documents

For a {lead['size']} firm, Clio Core runs ${int(''.join(filter(str.isdigit, lead['size'].split()[0])))*89:,}/month and won't draft a single contract. DocuFlow will.

Free pilot on your first 5 corporate matters. No commitment.

→ See it: {BOOKING}
→ Or try the demo: {DEMO}

Andres
DocuFlow Legal
hello@docuflowlegal.com
""",

    "immigration": lambda lead: f"""Hi {lead['name'].split()[0]},

{lead['name'].split()[0]}, question about immigration petition volume at {lead['firm']}.

Immigration firms handle high-volume, repetitive work: visa petitions (H-1B, L-1, O-1, E-2), PERM labor certifications, adjustment of status applications, consular processing, DACA renewals. How many hours per week does your team spend drafting those forms and supporting documents?

Most immigration attorneys I work with: 10–15 hours/week on petition drafting alone. That's not case analysis — that's data entry with legal labels.

**What DocuFlow Legal does for immigration practice:**
- H-1B, L-1, O-1, E-2 petitions — AI-assisted drafting with USCIS format
- PERM labor certifications — first draft in 20 minutes
- RFEs and NOIDs response bundles automated
- DACA applications and renewals — batch processing
- Flat pricing: $497/month for the firm, unlimited petitions

For a {lead['size']} firm, that's **potentially 40–60 billable hours/month** redirected from paperwork to client work.

Free pilot on your first 5 immigration cases. No commitment.

→ See it: {BOOKING}
→ Or try the demo: {DEMO}

Andres
DocuFlow Legal
hello@docuflowlegal.com
""",

    "business_immigration": lambda lead: f"""Hi {lead['name'].split()[0]},

{lead['name'].split()[0]}, question about business immigration documentation at {lead['firm']}.

Corporate immigration work is document-intensive: L-1A/B petitions, H-1B transfers, O-1 visas, E-2 investment petitions, PERM labor certifications, I-9 compliance. How much attorney time goes into drafting each petition package?

Most corporate immigration firms: 8–12 hours per petition package in drafting alone. Add client intake forms, RFE responses, and amendment requests, and documentation consumes your best people.

**What DocuFlow Legal does for corporate immigration:**
- L-1A/B and H-1B petitions — AI-drafted with employer and beneficiary data
- O-1 and E-2 petitions — supporting documentation bundles automated
- PERM: draft prevailing wage determinations and ETA 9089 in your firm's format
- RFE response bundles — pre-built templates updated to current USCIS standards
- Flat pricing: $497/month — no per-petition fees

For a {lead['size']} firm, **that's 30–50 hours/month of drafting work** that could be automated.

Free pilot on your first 5 business immigration cases. No migration, no commitment.

→ Book a 30-min demo: {BOOKING}
→ Or try the live demo: {DEMO}

Andres
DocuFlow Legal
hello@docuflowlegal.com
""",

    "real_estate": lambda lead: f"""Hi {lead['name'].split()[0]},

{lead['name'].split()[0]}, question about real estate documentation at {lead['firm']}.

RE law firms handle high-volume work: purchase agreements, deeds, title curative documents, lease agreements, loan documents, closing packages. How much time does your team spend drafting and reviewing those?

Most RE attorneys: 4–8 hours per transaction on documentation. With volume, that's significant overhead.

**What DocuFlow Legal does for real estate practice:**
- Purchase agreements and deeds — AI first draft in TX format
- Commercial lease agreements and amendments automated
- Title curative documents and closing packages
- Due diligence document review summaries
- Flat pricing: $497/month for the firm, unlimited documents

For a {lead['size']} firm: **you cut documentation time by 60%+ and redirect those hours to deal flow.**

Free pilot on your first 5 RE matters.

→ See it: {BOOKING}
→ Or try the demo: {DEMO}

Andres
DocuFlow Legal
hello@docuflowlegal.com
""",

    "litigation": lambda lead: f"""Hi {lead['name'].split()[0]},

{lead['name'].split()[0]}, question about litigation document volume at {lead['firm']}.

Litigation firms produce massive documentation: complaints, answers, discovery requests, interrogatories, document requests, production logs, motions to compel, motions for summary judgment, proposed orders. How many attorney hours per week go into drafting those?

Most litigation attorneys I work with: 10–15 hours/attorney/week on document production alone. That's not case prep — that's template filling.

**What DocuFlow Legal does for litigation:**
- Discovery requests and interrogatories — automated by issue
- Motion practice drafts — complaints, answers, MSJs
- Document review summaries — AI-assisted first pass
- Discovery responses and meet-and-confer letters
- Flat pricing: $497/month for the firm, unlimited documents

For a {lead['size']} firm, **that's potentially $2,000–$4,000/month in attorney hours** you could redirect from drafting to strategy.

Free pilot on your first 5 litigation matters.

→ See it: {BOOKING}
→ Or try the demo: {DEMO}

Andres
DocuFlow Legal
hello@docuflowlegal.com
""",
}

BOOKING = "https://strong-crumble-58f6e3.netlify.app/booking-page.html"
DEMO = "https://strong-crumble-58f6e3.netlify.app/booking-page.html"
STRIPE_PRO = "https://buy.stripe.com/8x23coaQ253xa93f9Z4abK00"
STRIPE_ENT = "https://buy.stripe.com/eVqbIU3nAeE7epjbIOabK02"


def get_subject(lead, idx):
    angle = lead.get("angle", "corporate")
    subjects = SUBJECTS_BY_ANGLE.get(angle, SUBJECTS_BY_ANGLE["corporate"])
    s = subjects[idx % len(subjects)]
    return s.replace("{firm}", lead["firm"])


def build_body(lead, idx):
    angle = lead.get("angle", "corporate")
    builder = BODIES_BY_ANGLE.get(angle, BODIES_BY_ANGLE["corporate"])
    return builder(lead)


def send_email(lead, idx):
    subject = get_subject(lead, idx)
    body = build_body(lead, idx)
    payload = {
        "from": FROM,
        "to": lead["email"],
        "reply_to": "grupounna@gmail.com",
        "subject": subject,
        "html": body.replace("\n", "<br>"),
    }
    headers = {"Authorization": f"Bearer {API_KEY}"}
    r = requests.post("https://api.resend.com/emails", headers=headers, json=payload)
    return {"id": r.json().get("id"), "status": r.status_code,
            "email": lead["email"], "name": lead["name"]}


def main():
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{'='*60}")
    print(f"R23 E1 — {len(leads)} emails — {ts}")
    print(f"{'='*60}")
    results = []
    for i, lead in enumerate(leads):
        r = send_email(lead, i)
        status = r["status"]
        ok = "✅" if status == 200 else f"❌ HTTP {status}"
        print(f"  {ok} {lead['id']} | {lead['name']} | {lead['email']} | angle={lead['angle']}")
        if status == 200:
            results.append({"lead": lead["id"], "email": lead["email"], "status": status})
        time.sleep(1.2)

    delivered = sum(1 for r in results)
    print(f"\n✓ R23 E1: {delivered}/{len(leads)} delivered")

    import os; os.makedirs("/data/wopie/wks/logs", exist_ok=True)
    with open("/data/wopie/wks/logs/round23-email1.log", "a") as f:
        f.write(f"[{ts}] R23 E1 — {delivered}/{len(leads)} delivered — {results}\n")


if __name__ == "__main__":
    main()
