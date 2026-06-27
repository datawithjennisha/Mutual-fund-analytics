import pandas as pd

df = pd.read_csv("Data/Raw/03_aum_by_fund_house.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

df["date"] = pd.to_datetime(df["date"])

df.drop_duplicates(inplace=True)

df["fund_house"] = df["fund_house"].str.strip()

print("Invalid AUM:", (df["aum_crore"] < 0).sum())

df.to_csv("Data/Processed/aum_by_fund_house_cleaned.csv", index=False)

print("Cleaning completed successfully!")