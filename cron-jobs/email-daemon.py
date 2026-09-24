#!/usr/bin/env python3
"""
DocuFlow Legal — Email Scheduler Daemon
Checks date every 60 seconds; fires email scripts when date matches.
Run: nohup python3 cron-jobs/email-daemon.py >> cron-jobs/email-daemon.log 2>&1 &
"""
import subprocess, time, sys, os, json
from datetime import datetime, date, timezone
from datetime import timedelta as td
from pathlib import Path

# Use America/Chicago (CST/CDT) so daemon fires at midnight CST, not UTC
CHICAGO = timezone(td(hours=-5))  # naive but matches CST/CDT logic; actual offset computed below
def cst_now():
    """Return current datetime in America/Chicago timezone."""
    import zoneinfo
    cz = zoneinfo.ZoneInfo("America/Chicago")
    return datetime.now(cz)

def cst_today():
    """Return today's date in America/Chicago."""
    return cst_now().date()

# R1 E2/E3 held: prior accepted sends in logs; never resend as test.
DISPATCH = {
    '2026-09-23': [
        'python3 /data/wopie/wks/scripts/send-round13-email1.py',
        'python3 /data/wopie/wks/scripts/send-round14-email1.py',
        'python3 /data/wopie/wks/scripts/send-round15-email1.py',
        'python3 /data/wopie/wks/scripts/send-round16-email1.py',
        'python3 /data/wopie/wks/scripts/send-barry-adkins-v2.py',
        'python3 /data/wopie/wks/scripts/send-round18-email1.py',  # R18: Reyes Blum PLLC, 4 contacts
    ],
    '2026-09-24': [
        'python3 /data/wopie/wks/scripts/send-round14-email1.py',  # R14: Houston Immigration, 3 leads (re-scheduled from Sep 23 quota block)
        'python3 /data/wopie/wks/scripts/send-round5-email1.py',
        'python3 /data/wopie/wks/scripts/send-round17-email1.py',  # R17: Reddy Neumann Brown PC, 12 contacts
        'python3 /data/wopie/wks/scripts/send-round1-email2-v3.py --live',  # R1 E2 v3: case study / free pilot, 6 leads — LIVE (was test-only)
        'python3 /data/wopie/wks/scripts/r1-e2-rescue.py',  # R1 E2 Rescue: 4 leads únicos (jmonty, dramirez, rhamilton, brad) — dup con v3 removidos
        'python3 /data/wopie/wks/scripts/send-matthew-childress-v2.py',  # Matthew Childress V2: 24h follow-up Gray Reed
    ],
    '2026-09-25': [
        'python3 /data/wopie/wks/scripts/send-round9-email1.py',
        'python3 /data/wopie/wks/scripts/send-round10-email1.py',
        'python3 /data/wopie/wks/scripts/send-round19-email1.py',  # R19: Quan Law Group, 8 contacts
        'python3 /data/wopie/wks/scripts/send-round20-email1.py',  # R20: Cano Immigration, 2 contacts
    ],
    '2026-09-26': [
        'python3 /data/wopie/wks/scripts/send-round6-email1.py',
        'python3 /data/wopie/wks/scripts/send-round21-email1.py',  # R21: BBA Law Group, 9 contacts
        'python3 /data/wopie/wks/scripts/send-round22-email2.py --live',  # R22 E2: Bell Nunnally, 3d post-E1, free pilot — LIVE
        'python3 /data/wopie/wks/scripts/send-gray-reed-employment-e2.py',  # Gray Reed Employment E2: Ruth Ann Daniels, 3d post-E1
    ],
    '2026-09-27': [
        'python3 /data/wopie/wks/scripts/send-round23-email1.py',  # R23 E1: 10 specialty firms (immigration, employment, family, corporate, RE, litigation)
    ],
    '2026-09-30': [
        'python3 /data/wopie/wks/scripts/send-round23-email2.py',  # R23 E2: social proof + free pilot, 3d post-E1
    ],
    '2026-09-28': [
        'python3 /data/wopie/wks/scripts/send-round9-email2.py',
        'python3 /data/wopie/wks/scripts/send-round10-email2.py',
        'python3 /data/wopie/wks/scripts/send-round17-email2.py',  # R17 E2: Reddy Neumann Brown, 3 days after E1
    ],
    '2026-09-29': [
        'python3 /data/wopie/wks/scripts/send-round6-email2.py',
        'python3 /data/wopie/wks/scripts/send-round22-email3.py',  # R22 E3: Bell Nunnally, final touch
        'python3 /data/wopie/wks/scripts/send-gray-reed-employment-e3.py',  # Gray Reed Employment E3: Ruth Ann Daniels, final
    ],
    '2026-10-01': ['python3 /data/wopie/wks/scripts/send-round17-email3.py'],  # R17 E3: Reddy Neumann Brown, 5 days after E2
    '2026-10-02': [
        'python3 /data/wopie/wks/scripts/send-round25-email1.py',  # R25 E1: Immigration leads (Nikova, Vega, Ahluwalia, Williamson, Zhang)
        'python3 /data/wopie/wks/scripts/send-round9-email3.py',  # R9 E3: Monty & Ramirez + McCathern final close
        'python3 /data/wopie/wks/scripts/send-round10-email3.py',  # R10 E3: Bell Nunnally final close
    ],
    '2026-10-03': [
        'python3 /data/wopie/wks/scripts/send-round6-email3.py',  # R6 E3: final close
        'python3 /data/wopie/wks/scripts/send-round23-email3.py',  # R23 E3: final close, 6d post-E1
    ],
    '2026-10-05': [
        'python3 /data/wopie/wks/scripts/send-round25-email2.py',  # R25 E2: 3d post-E1 social proof + free pilot
        'python3 /data/wopie/wks/scripts/send-round7-email1.py',  # R7 E1: specialty firms
    ],
    '2026-10-06': [
        'python3 /data/wopie/wks/scripts/send-round24-email1.py',  # R24 E1: 6 fresh firms
    ],
    '2026-10-07': [
        'python3 /data/wopie/wks/scripts/send-round26-email1.py',  # R26 E1: Fong Ilagan (immigration) + Oberti Sullivan (employment), 6 contacts
    ],
    '2026-10-08': [
        'python3 /data/wopie/wks/scripts/send-round25-email3.py',  # R25 E3: 6d post-E1 final close
        'python3 /data/wopie/wks/scripts/send-round7-email2.py',  # R7 E2: social proof + free pilot
    ],
    '2026-10-09': [
        'python3 /data/wopie/wks/scripts/send-round24-email2.py',  # R24 E2: social proof + free pilot, 3d post-E1
    ],
    '2026-10-10': [
        'python3 /data/wopie/wks/scripts/send-round26-email2.py',  # R26 E2: 3d post-E1 social proof + free pilot
    ],
    '2026-10-12': [
        'python3 /data/wopie/wks/scripts/send-round7-email3.py',  # R7 E3: final close
        'python3 /data/wopie/wks/scripts/send-round24-email3.py',  # R24 E3: final close, 6d post-E1
    ],
    '2026-10-13': [
        'python3 /data/wopie/wks/scripts/send-round26-email3.py',  # R26 E3: 6d post-E1 final close
    ],
    '2026-10-14': [
        'python3 /data/wopie/wks/scripts/send-round27-email1.py',  # R27 E1: 25 firms immigration + employment Texas
    ],
    '2026-10-15': [
        'python3 /data/wopie/wks/scripts/send-round28-email1.py',  # R28 E1: 17 firms immigration + employment (Modi, Spiliotis, Clifford, etc.)
    ],
    '2026-10-18': [
        'python3 /data/wopie/wks/scripts/send-round28-email2.py',  # R28 E2: 3d post-E1 social proof + free pilot
    ],
    '2026-10-21': [
        'python3 /data/wopie/wks/scripts/send-round28-email3.py',  # R28 E3: 6d post-E1 final close
    ],
    '2026-10-22': [
        'python3 /data/wopie/wks/scripts/send-round29-email1.py',  # R29 E1: 21 firms immigration/employment/family/corporate Texas, 24 contacts
    ],
    '2026-10-25': [
        'python3 /data/wopie/wks/scripts/send-round29-email2.py',  # R29 E2: 3d post-E1 social proof + free pilot
    ],
    '2026-11-01': [
        'python3 /data/wopie/wks/scripts/send-round29-email3.py',  # R29 E3: final close / referral ask
    ],
    '2026-10-17': [
        'python3 /data/wopie/wks/scripts/send-round27-email2.py',  # R27 E2: 3d post-E1 free pilot follow-up
    ],
    '2026-10-20': [
        'python3 /data/wopie/wks/scripts/send-round27-email3.py',  # R27 E3: final close / referral ask
    ],
}

SCRIPT_DIR = Path('/data/wopie/wks')
LOG_FILE = SCRIPT_DIR / 'cron-jobs' / 'dispatcher.log'
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

FiredFile = SCRIPT_DIR / 'cron-jobs' / 'fired_dates.json'

def load_fired():
    if FiredFile.exists():
        return set(json.load(FiredFile.open()).get('fired', []))
    return set()

def save_fired(fired):
    FiredFile.write_text(json.dumps({'fired': sorted(fired)}, indent=2))

def fire_date(d):
    fired = load_fired()
    d_str = d.isoformat()
    if d_str in fired:
        print(f'[{datetime.now().isoformat()}] {d_str} ya disparado — skip')
        return
    if d_str not in DISPATCH:
        print(f'[{datetime.now().isoformat()}] {d_str} — no emails programados')
        return
    print(f'[{datetime.now().isoformat()}] 🔥 FIRES: {d_str} — {len(DISPATCH[d_str])} script(s)')
    for cmd in DISPATCH[d_str]:
        print(f'  >>> {cmd}')
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=str(SCRIPT_DIR))
        out = r.stdout.strip()[:300]
        err = r.stderr.strip()[:100]
        print(f'  stdout: {out}')
        if err: print(f'  stderr: {err}')
    fired.add(d_str)
    save_fired(fired)
    print(f'[{datetime.now().isoformat()}] ✅ {d_str} completado y registrado')

# Immediate check
today = cst_today()
print(f'[{cst_now().isoformat()}] Email Daemon started — today CST: {today}')
fire_date(today)

# Check every 60 seconds
while True:
    time.sleep(60)
    new_today = cst_today()
    if new_today != today:
        today = new_today
        fire_date(today)
