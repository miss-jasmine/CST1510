"""
RECORD CHECK  -  my version
===========================

Name  : Jasmine Chabbab
Lane  : Cyber
Date  : 8/11/2026

Run it:   python template.py
"""

# ================================================================ PARSE LINE
def parse_line(raw_line):
    """sort into a clean dictionary."""
    clean_line = raw_line.strip().lower()
    parts = [field.strip() for field in clean_line.split(",")]
    server = parts[0]
    
    used_val = int(parts[1].split("=")[1].strip())
    total_val = int(parts[2].split("=")[1].strip())
    return {
        "server": server,
        "used": used_val,
        "total": total_val
    }


messy_lines = [
    "  Srv-01 , used=87 , total=100\n",
    "SRV-02,used=120,total=100",
    "  srv-03,used=45 ,total=100 ",
    "Srv-04 , used = 93 , total=100",
    "  sRv-05  ,  USED = 12 ,  Total = 100 \n"
]

for line in messy_lines:
    cleaned_record = parse_line(line)
    print(cleaned_record)


# ====================================================================== CLASS
class Record:
    """present recorded value and threshold limit"""

    def __init__(self, label, value, limit):
        """initialise a record with label, value, and limit"""
        self.label = label
        self.value = value
        self.limit = limit


# ==================================================================== RECORDS
records = [
    Record("srv-01", 87, 100),
    Record("srv-02", 120, 100)
]


# ==================================================================== OUTPUT
for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  Value : {record.value}")
    print(f"  Limit : {record.limit}")
    print("=" * 34)