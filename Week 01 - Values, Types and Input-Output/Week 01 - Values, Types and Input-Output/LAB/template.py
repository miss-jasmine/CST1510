"""
RECORD CHECK  -  my version
===========================

Name  : Jasmine Chabbab
Lane  :  Cybersecurity
Date  : 30/09/2026

Run it:   python template.py
"""

# ==================================================================== INPUT
label = input("Enter source IP (e.g., 10.0.0.5): ")
first = float(input("Enter failed logins (e.g., 12): "))
second = float(input("Enter total attempts (e.g., 400): "))


# ================================================================== PROCESS
# difference: remaining/successful attempts
difference = second - first   

# percent: failed logins as a percentage of total attempts
percent = (first / second) * 100


# Output: Display the results in a formatted manner
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# Print the grade tier to two decimal places, right-aligned in a 10 characters
print(f"Failed     : {first:>10.2f}")
print(f"Total      : {second:>10.2f}")
print(f"Successful : {difference:>+10.2f}")  # Shows sign (+) for Excellent tier
print(f"Percent    : {percent:>10.2f} %")

print(f"Status     : MONITORING TRAFFIC")

print("=" * 34)
