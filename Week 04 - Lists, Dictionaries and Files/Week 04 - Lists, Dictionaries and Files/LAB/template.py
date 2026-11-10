"""
RECORD CHECK  -  my version
===========================

Name  : Jasmine
Lane  : Cyber
Date  : 21 Oct 2026

Run it:   python template.py
"""

def check_record(value, limit):
    """calculates the difference, percentage of limit used, and status"""
    difference = value - limit
    percent = (value / limit) * 100
    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"    
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """displays formatted cyber security status report for a single IP address"""
    print(f"--- Report for IP: {label} ---")
    print(f"Failed Logins: {value} / Limit: {limit}")
    print(f"Percentage of Limit Used: {percent:.1f}%")
    print(f"Difference to Limit: {difference:+d}")
    print(f"Status: {status}\n")

# list of records dictionaries containing label, value and limit
records = [
    {"label": "10.0.0.5", "value": 12, "limit": 400},
    {"label": "192.168.1.50", "value": 450, "limit": 400},
    {"label": "172.16.0.22", "value": 200, "limit": 200}
]

# loop over records that calls checks and prints a report
for record in records:
    # Unpack the calculations from check_record
    diff, pct, stat = check_record(record["value"], record["limit"])
    
    # pass information into the print report function
    print_report(record["label"], record["value"], record["limit"], diff, pct, stat)
