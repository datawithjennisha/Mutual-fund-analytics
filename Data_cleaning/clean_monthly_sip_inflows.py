import pandas as pd

df = pd.read_csv("Data/Raw/04_monthly_sip_inflows.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

df["month"] = pd.to_datetime(df["month"])

df.drop_duplicates(inplace=True)

print("Negative SIP:", (df["sip_inflow_crore"] < 0).sum())

df.to_csv("Data/Processed/monthly_sip_inflows_cleaned.csv", index=False)

print("Cleaning completed successfully!")