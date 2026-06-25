import pandas as pd

# ==============================
# Load Dataset
# ==============================
df = pd.read_csv("Data/Raw/02_nav_history.csv")

# ==============================
# Data Profiling
# ==============================
print("========== First 5 Rows ==========")
print(df.head())

print("\n========== Shape ==========")
print(df.shape)

print("\n========== Dataset Info ==========")
print(df.info())

print("\n========== Missing Values ==========")
print(df.isnull().sum())

print("\n========== Duplicate Rows ==========")
print(df.duplicated().sum())

# ==============================
# Convert Date Column
# ==============================
df["date"] = pd.to_datetime(df["date"])

print("\n========== Data Types ==========")
print(df.dtypes)

# ==============================
# Sort Dataset
# ==============================
df = df.sort_values(
    by=["amfi_code", "date"]
).reset_index(drop=True)

print("\n========== Sorted Dataset ==========")
print(df.head())

# ==============================
# Forward Fill Missing NAV
# (Within Each Mutual Fund)
# ==============================
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# ==============================
# Validate NAV
# Business Rule: NAV > 0
# ==============================
invalid_nav = df[df["nav"] <= 0]

print("\n========== Invalid NAV Records ==========")
print(invalid_nav)

print("\nInvalid NAV Count:", len(invalid_nav))

# ==============================
# Remove Duplicate Rows
# ==============================
df.drop_duplicates(inplace=True)

# ==============================
# Save Cleaned Dataset
# ==============================
df.to_csv(
    "Data/Processed/nav_history_cleaned.csv",
    index=False
)

print("\n✅ Cleaning completed successfully!")

print("\n========== Final Dataset Shape ==========")
print(df.shape)

print("\n========== First 5 Cleaned Rows ==========")
print(df.head())