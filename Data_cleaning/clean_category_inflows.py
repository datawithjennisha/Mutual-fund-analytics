import pandas as pd

df = pd.read_csv("Data/Raw/05_category_inflows.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

df["month"] = pd.to_datetime(df["month"])

df["category"] = df["category"].str.strip()

df.drop_duplicates(inplace=True)

df.to_csv("Data/Processed/category_inflows_cleaned.csv", index=False)

print("Cleaning completed successfully!")
