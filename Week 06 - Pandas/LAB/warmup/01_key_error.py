# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

import pandas as pd

df = pd.DataFrame({"Label": ["R-001", "R-002"], "Value": [87, 120], "Limit": [100, 100]})

print(df["Value"])
