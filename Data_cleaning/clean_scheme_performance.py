import pandas as pd

# ==============================
# Load Dataset
# ==============================
df = pd.read_csv("Data/Raw/07_scheme_performance.csv")

# ==============================
# Data Profiling
# ==============================
print("========== First 5 Rows ==========")
print(df.head())

print("\n========== Shape ==========")
print(df.shape)

print("\n========== Column Names ==========")
print(df.columns)

print("\n========== Dataset Info ==========")
print(df.info())

print("\n========== Missing Values ==========")
print(df.isnull().sum())

print("\n========== Duplicate Rows ==========")
print(df.duplicated().sum())

print("\n========== Data Types ==========")
print(df.dtypes)

# ==============================
# Convert Numeric Columns
# ==============================
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

df[numeric_cols] = df[numeric_cols].apply(
    pd.to_numeric,
    errors="coerce"
)

# ==============================
# Expense Ratio Validation
# Business Rule: 0.1% - 2.5%
# ==============================
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\n========== Invalid Expense Ratio ==========")
print(invalid_expense)

# ==============================
# Return Column Summary
# ==============================
print("\n========== Return Statistics ==========")
print(df[[
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]].describe())

# ==============================
# Remove Duplicate Rows
# ==============================
df.drop_duplicates(inplace=True)

# ==============================
# Save Cleaned Dataset
# ==============================
df.to_csv(
    "Data/Processed/scheme_performance_cleaned.csv",
    index=False
)

print("\n✅ Cleaning completed successfully!")

print("\n========== Final Dataset Shape ==========")
print(df.shape)

print("\n========== First 5 Cleaned Rows ==========")
print(df.head())