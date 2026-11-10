"""
RECORD CHECK  -  my version
===========================

Name  : Jasmine Chabbab
Lane  :  Cyber
Date  : 6/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

df = pd.read_csv("cyber_logins.csv")
df["percent"] = (df["failed_logins"] / df["total_attempts"]) * 100
print(df)