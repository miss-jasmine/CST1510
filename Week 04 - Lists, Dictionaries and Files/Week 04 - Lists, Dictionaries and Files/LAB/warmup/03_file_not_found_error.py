# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

import os

# 1. finds the script's folder path in warmup
script_dir = os.path.dirname(os.path.abspath(__file__))

# 2. move's the lab folder path up one level from the script's folder
lab_dir = os.path.dirname(script_dir)

# 3. targets the text file inside LAB folder
file_path = os.path.join(lab_dir, "records_sample.txt")

with open(file_path) as f:
    print(f.read())
