import pandas as pd

# Load Dataset
df = pd.read_csv("Data/Raw/01_fund_master.csv")

# Data Profiling
print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

# Convert Date
df["launch_date"] = pd.to_datetime(df["launch_date"])

# Remove Duplicates
df.drop_duplicates(inplace=True)

# Remove Leading/Trailing Spaces
text_cols = [
    "fund_house",
    "scheme_name",
    "category",
    "sub_category",
    "plan",
    "benchmark",
    "fund_manager",
    "risk_category",
    "sebi_category_code"
]

df[text_cols] = df[text_cols].apply(lambda x: x.str.strip())

# Save
df.to_csv("Data/Processed/fund_master_cleaned.csv", index=False)

print("Cleaning completed successfully!")