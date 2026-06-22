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