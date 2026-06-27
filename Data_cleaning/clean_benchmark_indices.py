import pandas as pd

df = pd.read_csv("Data/Raw/10_benchmark_indices.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

df["date"] = pd.to_datetime(df["date"])

df.drop_duplicates(inplace=True)

df["index_name"] = df["index_name"].str.strip()

print("Invalid Close Value:", (df["close_value"] <= 0).sum())

df.to_csv("Data/Processed/benchmark_indices_cleaned.csv", index=False)

print("Cleaning completed successfully!")
