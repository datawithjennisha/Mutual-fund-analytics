import pandas as pd
from pathlib import Path

DATA_PATH = Path("Data/raw")

csv_files = list(DATA_PATH.glob("*.csv"))

print(f"\nFound {len(csv_files)} CSV files\n")

for file in csv_files:

    print("=" * 80)
    print(f"FILE: {file.name}")
    print("=" * 80)

    try:
        df = pd.read_csv(file)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nHead:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("\n")

    except Exception as e:
        print(f"Error reading {file.name}: {e}")

# AMFI Validation

print("\n" + "="*80)
print("AMFI CODE VALIDATION")
print("="*80)

fund_master = pd.read_csv("Data/raw/01_fund_master.csv")
nav_history = pd.read_csv("Data/raw/02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print("Fund Master Codes:", len(master_codes))
print("NAV History Codes:", len(nav_codes))
print("Missing Codes:", len(missing_codes))