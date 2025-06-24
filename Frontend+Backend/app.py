import pandas as pd

# Excel ফাইল থেকে ডেটা পড়া
df = pd.read_excel("Employee_Info.xlsx", sheet_name="Sheet1")

# "BP" দিয়ে শুরু হওয়া ID গণনা করা
bp_count = df[df["EmployeeID"].str.startswith("BP")].shape[0]

print(f"{bp_count} employees have an ID starting with 'BP'")
