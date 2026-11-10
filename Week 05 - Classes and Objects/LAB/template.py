"""
RECORD CHECK  -  my version
===========================

Name  : Jasmine Chabbab
Lane  : Cyber
Date  : 10/11/2026

Run it:   python template.py
"""

# ====================================================================== CLASS
class Record:
    """stores source IP, failed logins, and total attempts"""

    def __init__(self, source_ip, failed_logins, total_attempts):
        self.source_ip = source_ip
        self.failed_logins = failed_logins
        self.total_attempts = total_attempts


# ==================================================================== RECORDS
r1 = Record("192.168.1.42", 18, 250)
r2 = Record("10.0.4.19", 95, 100)

records = [r1, r2]


# ==================================================================== OUTPUT
for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.source_ip}")
    print("=" * 34)
    print(f"  Failed Logins  : {record.failed_logins}")
    print(f"  Total Attempts : {record.total_attempts}")
    print("=" * 34)