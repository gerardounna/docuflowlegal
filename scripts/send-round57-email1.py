#!/usr/bin/env python3
"""
R57 E1 — Fisher Phillips Houston (7 attorneys)
Dispara: Oct 6 2026 00:10 CST
Angulo: AltaClaro DepoSim firmwide Sep 23 2026 — FP ya invierte en IA legal
       DocuFlow = complemento natural para employment documents
INTEL: fisherphillips.com/en/insights — AltaClaro DepoSim firmwide deployment Sep 23 2026
       "Nearly 900 attorneys globally" — decision for entire practice
"""
import os, sys, time, json

API_KEY = os.environ.get("RESEND_API_KEY", "${RESEND_API_KEY}")
FROM_EMAIL = "Andres <hello@docuflowlegal.com>"
LANDING = "https://gerardounna.github.io/docuflowlegal/landing-page.html"
BOOKING = "https://gerardounna.github.io/docuflowlegal/booking-page.html"
DEMO = "https://gerardounna.github.io/docuflowlegal/docuflow-product/demo-interface.html"
PROPOSAL = "https://gerardounna.github.io/docuflowlegal/fisher-phillips-proposal.html"
STRIPE_PRO = "https://buy.stripe.com/8x23coaQ253xa93a93fZ4abK00"

# ─────────────────────────────────────────────────────────────────────────────
# ANGULO CENTRAL: AltaClaro DepoSim firmwide Sep 23 2026
# Fisher Phillips ya invierte en IA legal firmwide. DocuFlow = complemento.
# ─────────────────────────────────────────────────────────────────────────────

leads = [
    {
        "name": "Stephen J. Roppolo",
        "email": "sroppolo@fisherphillips.com",
        "title": "Partner",
        "practice": "Employment litigation, trade secrets, non-competes",
        "first_name": "Stephen",
        "angle": "non-compete",
    },
    {
        "name": "Teresa Valderrama",
        "email": "tvalderrama@fisherphillips.com",
        "title": "Partner",
        "practice": "Wage & hour, whistleblower claims, discrimination",
        "first_name": "Teresa",
        "angle": "wage_hour",
    },
    {
        "name": "John D. Surma",
        "email": "jsurma@fisherphillips.com",
        "title": "Partner",
        "practice": "Workplace safety, OSHA compliance and litigation",
        "first_name": "John",
        "angle": "osha",
    },
    {
        "name": "Lindsay Reimer",
        "email": "lreimer@fisherphillips.com",
        "title": "Attorney",
        "practice": "Employment discrimination, harassment, retaliation",
        "first_name": "Lindsay",
        "angle": "general",
    },
    {
        "name": "Kristin L. Smith",
        "email": "ksmith@fisherphillips.com",
        "title": "Attorney",
        "practice": "Employment law",
        "first_name": "Kristin",
        "angle": "general",
    },
    {
        "name": "Nicole Gross",
        "email": "ngross@fisherphillips.com",
        "title": "Attorney",
        "practice": "Employment law",
        "first_name": "Nicole",
        "angle": "general",
    },
    {
        "name": "Cheryl Blount",
        "email": "cblount@fisherphillips.com",
        "title": "Attorney",
        "practice": "Employment litigation",
        "first_name": "Cheryl",
        "angle": "general",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# EMAIL BODIES — todos con el ángulo DepoSim
# ─────────────────────────────────────────────────────────────────────────────

BODY_NONCOMPEE = """Hi Stephen,

Quick question — and this will only take 2 minutes of your time.

I saw that Fisher Phillips deployed AltaClaro DepoSim firmwide in September. Nearly 900 attorneys now using AI for depositions. That's a significant investment — and it tells me something: your firm is serious about AI improving legal work.

Here's the natural next step: **DocuFlow** handles the employment documents your team drafts every day — severance agreements, non-compete demand letters, employment contracts, cease-and-desist.

The workflow your attorneys already understand:
- Feed key facts → AI generates first draft in seconds
- Review and finalize → back to client faster

For non-compete work specifically, we see firms saving 3-5 hours per severance agreement. For a team your size, that's meaningful.

Live demo (2 min severance agreement generation): {demo}

Or book 30 minutes with me directly: {booking}

See our Fisher Phillips-specific proposal (with DepoSim angle): {proposal}

Best,
Andres
DocuFlow Legal
{landing}"""

BODY_WAGE_HOUR = """Hi Teresa,

Quick question — and this will only take 2 minutes of your time.

I saw that Fisher Phillips deployed AltaClaro DepoSim firmwide in September. Nearly 900 attorneys now using AI for depositions. That's a significant investment — and it tells me something: your firm is serious about AI improving legal work.

Here's the natural next step: **DocuFlow** handles the employment documents your team drafts every day — wage claim responses, prevailing wage determinations, FLSA documentation, EEOC position statements.

The workflow your attorneys already understand:
- Feed key facts → AI generates first draft in seconds
- Review and finalize → back to client faster

For wage & hour work, FLSA documentation alone can take 2-4 hours per matter. With DocuFlow, that drops to minutes.

Live demo (2 min wage documentation generation): {demo}

Or book 30 minutes with me directly: {booking}

See our Fisher Phillips-specific proposal (with DepoSim angle): {proposal}

Best,
Andres
DocuFlow Legal
{landing}"""

BODY_OSHA = """Hi John,

Quick question — and this will only take 2 minutes of your time.

I saw that Fisher Phillips deployed AltaClaro DepoSim firmwide in September. Nearly 900 attorneys now using AI for depositions. That's a significant investment — and it tells me something: your firm is serious about AI improving legal work.

Here's the natural next step: **DocuFlow** handles the compliance documentation your OSHA practice generates — incident reports, safety correspondence, OSHA citation responses, and compliance documentation.

The workflow your attorneys already understand:
- Feed key facts → AI generates first draft in seconds
- Review and finalize → back to client faster

For a growing OSHA practice, incident documentation alone can take 4-6 hours per major matter. With DocuFlow, that drops to minutes.

Live demo (OSHA incident doc generation): {demo}

Or book 30 minutes with me directly: {booking}

See our Fisher Phillips-specific proposal (with DepoSim angle): {proposal}

Best,
Andres
DocuFlow Legal
{landing}"""

BODY_GENERAL = """Hi {first_name},

Quick question — and this will only take 2 minutes of your time.

I saw that Fisher Phillips deployed AltaClaro DepoSim firmwide in September. Nearly 900 attorneys now using AI for depositions. That's a significant investment — and it tells me something: your firm is serious about AI improving legal work.

Here's the natural next step: **DocuFlow** handles the employment documents your team drafts every day — severance agreements, EEOC responses, employment contracts, demand letters.

The workflow your attorneys already understand:
- Feed key facts → AI generates first draft in seconds
- Review and finalize → back to client faster

For an employment practice, the repetitive documents are significant. We see firms saving 3-5 hours per severance agreement alone. For your whole team, that's real billing time recovered.

Live demo (2 min document generation): {demo}

Or book 30 minutes with me directly: {booking}

See our Fisher Phillips-specific proposal (with DepoSim angle): {proposal}

Best,
Andres
DocuFlow Legal
{landing}"""

BODIES = {
    "non-compete": BODY_NONCOMPEE,
    "wage_hour": BODY_WAGE_HOUR,
    "osha": BODY_OSHA,
    "general": BODY_GENERAL,
}

SUBJECTS = {
    "non-compete": "Non-compete severance agreements — 3 hrs → minutes",
    "wage_hour": "Wage & hour documentation — 2 hrs → minutes",
    "osha": "OSHA compliance documentation — 4 hrs → minutes",
    "general": "Document automation for employment practice — 3 hrs → minutes",
}

SUBJECT2 = {
    "non-compete": "Re: Non-compete severance agreements — 3 hrs → minutes",
    "wage_hour": "Re: Wage & hour documentation — 2 hrs → minutes",
    "osha": "Re: OSHA compliance documentation — 4 hrs → minutes",
    "general": "Re: Document automation for employment practice",
}


def send_email(lead):
    angle = lead.get("angle", "general")
    body_tpl = BODIES.get(angle, BODIES["general"])
    body = body_tpl.format(
        first_name=lead["first_name"],
        landing=LANDING,
        demo=DEMO,
        booking=BOOKING,
        proposal=PROPOSAL,
        stripe=STRIPE_PRO,
    )
    subject_tpl = SUBJECTS.get(angle, SUBJECTS["general"])

    payload = {
        "from": FROM_EMAIL,
        "to": [lead["email"]],
        "subject": subject_tpl,
        "text": body,
        "reply_to": "grupounna@gmail.com",
        "tags": [{"name": "round", "value": "R57"}, {"name": "stage", "value": "E1"}, {"name": "firm", "value": "fisherphillips"}],
    }

    import urllib.request
    import json as _json

    data = _json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://api.resend.com/emails",
        data=data,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = _json.loads(resp.read())
            print(f"  ✅ {lead['email']} → ID: {result.get('id', 'n/a')}")
            return True
    except urllib.error.HTTPError as e:
        body_err = e.read().decode()
        print(f"  ❌ {lead['email']} → HTTP {e.code}: {body_err[:200]}")
        return False
    except Exception as e:
        print(f"  ❌ {lead['email']} → {e}")
        return False


if __name__ == "__main__":
    # CONTAINMENT: skip if not --live
    import sys as _sys
    _live = "--live" in _sys.argv

    print(f"R57 E1 — Fisher Phillips Houston — AltaClaro DepoSim angle")
    print(f"Inteli: FP firmwide AltaClaro DepoSim deployment Sep 23 2026")
    print(f"Leads: {len(leads)} | Mode: {'LIVE' if _live else 'DRY RUN'}")
    print("-" * 60)

    if _live:
        results = [send_email(l) for l in leads]
        ok = sum(results)
        print(f"\nResults: {ok}/{len(results)} sent successfully")
        # Write result log
        with open("/data/wopie/wks/logs/r57-e1.log", "a") as f:
            from datetime import datetime
            f.write(f"[{datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}] R57 E1: {ok}/{len(leads)} sent\n")
    else:
        print("Dry run — use --live to send")
        for l in leads:
            angle = l.get("angle", "general")
            print(f"  DRY: {l['email']} | {l['name']} | {l['title']} | angle: {angle}")
            print(f"        Subject: {SUBJECTS.get(angle, SUBJECTS['general'])}")
