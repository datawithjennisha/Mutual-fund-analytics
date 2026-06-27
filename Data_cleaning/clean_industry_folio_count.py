import pandas as pd

df = pd.read_csv("Data/Raw/06_industry_folio_count.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

df["month"] = pd.to_datetime(df["month"])

df.drop_duplicates(inplace=True)

df.to_csv("Data/Processed/industry_folio_count_cleaned.csv", index=False)

print("Cleaning completed successfully!")
