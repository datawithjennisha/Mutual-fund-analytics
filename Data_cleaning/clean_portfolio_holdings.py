import pandas as pd

df = pd.read_csv("Data/Raw/09_portfolio_holdings.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

df["portfolio_date"] = pd.to_datetime(df["portfolio_date"])

df.drop_duplicates(inplace=True)

text_cols = [
    "stock_symbol",
    "stock_name",
    "sector"
]

df[text_cols] = df[text_cols].apply(lambda x: x.str.strip())

print("Invalid Weight:", (df["weight_pct"] < 0).sum())

df.to_csv("Data/Processed/portfolio_holdings_cleaned.csv", index=False)

print("Cleaning completed successfully!")
