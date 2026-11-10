"""
RECORD CHECK  -  my version
===========================

Name  : Jasmine Chabbab
Lane  :  Cybersecurity
Date  : 30/9/26

Run it:   python template.py
"""

# ==================================================================== INPUT
# 1. ask for three values.

label = input("Enter Source IP: ")
value = float(input("Enter failed logins: "))
limit = float(input("Enter allowed limit: "))


# ================================================================== PROCESS
# 2. work out the difference and percentage. 
difference = value - limit

percent = (value / limit) * 100

# if else OVER LIMIT or OK

if value > limit:
    status = "OVER LIMIT"
else:
    status = "OK"


# print the report with the three values, plus status, inside a border.

print()
print("=" * 40)
print(f"  RECORD CHECK  -  {label}")
print("=" * 40)

print(f"Failed Logins : {value}")
print(f"Allowed Limit : {limit}")
print(f"Difference    : {difference}")
print(f"Percentage    : {percent}%")
print(f"Status        : {status}")

print("=" * 40)