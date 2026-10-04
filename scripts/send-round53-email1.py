#!/usr/bin/env python3
"""
DocuFlow Legal — R53 Email #1 (Employment Boutique)
Clouse Brown PLLC — Dallas TX — employer-side employment law
3 attorneys Board Certified in Labor & Employment Law (TBLS)
Fires: 2026-10-03 00:10 CST — PENDING AUTHORIZATION
Source: clousebrown.com/attorneys — Sep 29 2026
Lead: andres research cycle E202
"""
import os
import sys
import time
import requests

API_KEY = os.environ.get("RESEND_API_KEY", "${RESEND_API_KEY}")
# NOTE: API key should be set as RESEND_API_KEY env var. Fallback is for local dev only.
FROM = "Andres <hello@docuflowlegal.com>"
REPLY_TO = "grupounna@gmail.com"
DEMO = "https://gerardounna.github.io/docuflowlegal/docuflow-product/demo-interface.html"
BOOKING = "https://gerardounna.github.io/docuflowlegal/booking-page.html"
LANDING = "https://gerardounna.github.io/docuflowlegal/landing-page.html"
PROPOSAL = "https://gerardounna.github.io/docuflowlegal/clouse-brown-proposal.html"

leads = [
    # Keith A. Clouse — Managing Partner, Board Certified L&E (TBLS)
    # 30+ years employer-side employment law
    {
        "id": "R53-01",
        "name": "Keith Clouse",
        "email": "keith@clousebrown.com",
        "firm": "Clouse Brown PLLC",
        "title": "Managing Partner",
        "city": "Dallas",
        "practice": "Employment Law (employer-side)",
        "pain": "executive employment agreements, non-competes, severance packages, EEOC responses",
        "subject": "Executive employment agreements — 20 min vs. 6 hours",
        "angle": "executive employment agreements, post-employment restrictions, non-compete enforcement",
    },
    # Alyson C. Brown — Partner, Board Certified L&E (TBLS)
    {
        "id": "R53-02",
        "name": "Alyson Brown",
        "email": "abrown@clousebrown.com",
        "firm": "Clouse Brown PLLC",
        "title": "Partner",
        "city": "Dallas",
        "practice": "Employment Law (employer-side)",
        "pain": "employment counseling, discrimination defense, EEOC responses, handbook drafting",
        "subject": "Employment handbook drafts — 20 min vs. 10 hours",
        "angle": "board certified employment counsel, high-volume repetitive drafting",
    },
    # Jesse E. Clouse — Associate, Labor & Employment Law
    {
        "id": "R53-03",
        "name": "Jesse Clouse",
        "email": "jclouse@clousebrown.com",
        "firm": "Clouse Brown PLLC",
        "title": "Associate",
        "city": "Dallas",
        "practice": "Employment Law (employer-side)",
        "pain": "employment agreements, severance, non-competes, discrimination defense",
        "subject": "Severance agreement drafts — 20 min vs. 4 hours",
        "angle": "employer-side employment counsel, repetitive document drafting opportunity",
    },
]

SUBJECTS = [
    "Executive employment agreements — DocuFlow pilot for {firm}",
    "Employment handbook + EEOC responses — DocuFlow for {firm}",
    "Severance agreements + non-competes — DocuFlow for {firm}",
]

BODY_HTML_TEMPLATE = """<!DOCTYPE html>
<html><head><meta charset="utf-8"></head>
<body style="margin:0;padding:0;background:#f8fafc;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#f8fafc;padding:24px 16px;">
<tr><td align="center">
<table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;width:100%;">

<!-- Header -->
<tr><td style="background:#ffffff;border-radius:12px 12px 0 0;padding:32px 32px 24px;border-bottom:3px solid #6366f1;">
  <p style="margin:0 0 8px;color:#6366f1;font-size:11px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;">DocuFlow Legal · Texas</p>
  <h1 style="margin:0;font-size:22px;font-weight:800;color:#0f172a;">{firm}</h1>
  <p style="margin:8px 0 0;color:#64748b;font-size:13px;">Employer-Side Employment Law · Board Certified L&E</p>
</td></tr>

<!-- Body -->
<tr><td style="background:#ffffff;padding:32px;">
  <p style="font-size:15px;line-height:1.7;color:#334155;margin:0 0 20px;">Hi {first_name},</p>
  <p style="font-size:15px;line-height:1.7;color:#334155;margin:0 0 20px;">
  Clouse Brown handles some of the most document-intensive employment matters in Dallas — executive employment agreements, severance packages, WARN Act notices, EEOC position statements, and post-employment restriction agreements.
  </p>
  <p style="font-size:15px;line-height:1.7;color:#334155;margin:0 0 20px;">
  Firms like yours spend 4–8 hours per document on first drafts that follow the same structure every time. Associates are billing clients, not reviewing documents they could have drafted in 20 minutes.
  </p>

  <!-- Pain point box -->
  <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#fef2f2;border:1px solid #fecaca;border-radius:10px;margin:0 0 24px;">
  <tr><td style="padding:20px 24px;">
    <p style="margin:0 0 8px;font-size:13px;font-weight:700;color:#991b1b;">What we automate:</p>
    <p style="margin:0;font-size:13px;color:#7f1d1d;line-height:1.7;">
    • Executive employment agreements &nbsp;&nbsp;• Severance packages<br>
    • WARN Act notices &nbsp;&nbsp;• EEOC position statements<br>
    • Non-compete &nbsp;&nbsp;• Employment handbook sections<br>
    All trained on YOUR firm's format and clause library.
    </p>
  </td></tr>
  </table>

  <p style="font-size:15px;line-height:1.7;color:#334155;margin:0 0 20px;">
  <strong>Free pilot:</strong> Send us 5 representative documents from your practice. We train on Clouse Brown's format overnight. You test the output on 3 real matters over 2 weeks. Judge the quality — no commitment.
  </p>
  <p style="font-size:15px;line-height:1.7;color:#334155;margin:0 0 24px;">
  <strong>Pricing:</strong> Professional $1,497 setup + $497/month flat — unlimited documents, no per-attorney fees.
  </p>

  <!-- CTA -->
  <table cellpadding="0" cellspacing="0" border="0" style="margin:0 0 24px;">
  <tr>
  <td style="padding:0 8px 0 0;"><a href="{DEMO}" style="display:inline-block;background:#6366f1;color:#ffffff;font-size:14px;font-weight:600;padding:12px 20px;border-radius:8px;text-decoration:none;">Try Live Demo →</a></td>
  <td style="padding:0 8px 0 0;"><a href="{BOOKING}" style="display:inline-block;background:#ffffff;color:#6366f1;font-size:14px;font-weight:600;padding:12px 20px;border-radius:8px;text-decoration:none;border:2px solid #6366f1;">Book 30-min Call</a></td>
  <td><a href="{PROPOSAL}" style="display:inline-block;background:#ffffff;color:#1e40af;font-size:14px;font-weight:600;padding:12px 20px;border-radius:8px;text-decoration:none;border:2px solid #bfdbfe;">View Custom Proposal →</a></td>
  </tr>
  </table>

  <p style="font-size:13px;color:#64748b;line-height:1.6;margin:0;">
  Best,<br>
  <strong>Andres Bustamante</strong><br>
  DocuFlow Legal · hello@docuflowlegal.com
  </p>
</td></tr>

<!-- Footer -->
<tr><td style="background:#f1f5f9;padding:20px 32px;border-radius:0 0 12px 12px;">
  <p style="font-size:11px;color:#64748b;margin:0;line-height:1.6;">
  DocuFlow Legal · Austin, TX<br>
  <a href="{LANDING}" style="color:#6366f1;">docuflowlegal.com</a> · hello@docuflowlegal.com<br>
  <span style="color:#94a3b8;">You're receiving this because you're a Texas employment attorney. Unsubscribe anytime.</span>
  </p>
</td></tr>

</table></td></tr></table></body></html>"""

TEXT_TEMPLATE = """Hi {first_name},

Clouse Brown handles some of the most document-intensive employment matters in Dallas — executive employment agreements, severance packages, WARN Act notices, and EEOC position statements.

Firms like yours spend 4–8 hours per document on first drafts that follow the same structure every time.

What we automate:
• Executive employment agreements
• Severance packages  
• WARN Act notices
• EEOC position statements
• Non-compete agreements
All trained on YOUR firm's format and clause library.

Free pilot: Send us 5 representative documents. We train overnight. You test on 3 real matters — no commitment.

Pricing: Professional $1,497 setup + $497/month flat — unlimited documents, no per-attorney fees.

Try the demo: {DEMO}
Book a call: {BOOKING}
View our Clouse Brown proposal: {PROPOSAL}

Best,
Andres Bustamante
DocuFlow Legal
hello@docuflowlegal.com

---
Unsubscribe: {UNSUBSCRIBE}"""


def send_email(lead, dry_run=False):
    subject_idx = int(lead["id"].split("-")[1]) - 1
    subject = SUBJECTS[subject_idx % len(SUBJECTS)].format(firm=lead["firm"])
    
    html = BODY_HTML_TEMPLATE.format(
        first_name=lead["name"].split()[0],
        firm=lead["firm"],
        DEMO=DEMO,
        BOOKING=BOOKING,
        LANDING=LANDING,
        PROPOSAL=PROPOSAL,
    )
    text = TEXT_TEMPLATE.format(
        first_name=lead["name"].split()[0],
        firm=lead["firm"],
        DEMO=DEMO,
        BOOKING=BOOKING,
        PROPOSAL=PROPOSAL,
        UNSUBSCRIBE="{UNSUBSCRIBE_URL}",
    )
    
    if dry_run:
        print(f"[TEST] Would send to {lead['email']}: {subject}")
        return True
    
    payload = {
        "from": FROM,
        "to": [lead["email"]],
        "subject": subject,
        "html": html,
        "text": text,
        "reply_to": REPLY_TO,
        "tags": [{"name": "round", "value": "53"}, {"name": "lead_id", "value": lead["id"]}],
    }
    r = requests.post(
        "https://api.resend.com/emails",
        json=payload,
        headers={"Authorization": f"Bearer {API_KEY}"},
        timeout=20,
    )
    ok = r.status_code in (200, 202)
    j = r.json()
    eid = j.get("id", j.get("message", "?"))
    status = "OK" if ok else f"FAIL({r.status_code})"
    print(f"  [{status}] {lead['id']} {lead['email']} -> {str(eid)[:60]}")
    return ok


if __name__ == "__main__":
    mode = "live" if "--live" in sys.argv else "test"
    print(f"=== DocuFlow R53 E1 — Clouse Brown PLLC — {mode} mode ===")
    print(f"Fires: 2026-10-03 00:10 CST | {len(leads)} leads")
    
    if mode == "test":
        for lead in leads:
            send_email(lead, dry_run=True)
    else:
        results = []
        for lead in leads:
            ok = send_email(lead)
            results.append({"lead_id": lead["id"], "email": lead["email"], "ok": ok})
            time.sleep(1.2)
        
        # Save results
        import json
        from datetime import datetime
        with open("/data/wopie/wks/scripts/send-round53-email1-log.json", "w") as f:
            json.dump({
                "timestamp": datetime.now().isoformat(),
                "round": 53,
                "email": 1,
                "leads_sent": len([r for r in results if r["ok"]]),
                "results": results,
            }, f, indent=2)
        
        sent = len([r for r in results if r["ok"]])
        print(f"\n=== R53 E1 complete: {sent}/{len(leads)} sent ===")
