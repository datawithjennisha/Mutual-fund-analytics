import pandas as pd
from sqlalchemy import create_engine

# ==============================
# Create SQLite Engine
# ==============================
engine = create_engine("sqlite:///bluestock_mf.db")

print(" Connected to SQLite Database")

# ==============================
# Load Cleaned CSV Files
# ==============================
nav_df = pd.read_csv("Data/Processed/nav_history_cleaned.csv")
transactions_df = pd.read_csv("Data/Processed/investor_transactions_cleaned.csv")
performance_df = pd.read_csv("Data/Processed/scheme_performance_cleaned.csv")

# ==============================
# Load Data into SQLite
# ==============================
nav_df.to_sql(
    "nav_history",
    engine,
    if_exists="replace",
    index=False
)

transactions_df.to_sql(
    "investor_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance_df.to_sql(
    "scheme_performance",
    engine,
    if_exists="replace",
    index=False
)

print("\n All datasets loaded successfully!")

# ==============================
# Verify Row Counts
# ==============================
print("\n========== Row Counts ==========")

print("nav_history:", len(nav_df))
print("investor_transactions:", len(transactions_df))
print("scheme_performance:", len(performance_df))

# ==============================
# Display Database Tables
# ==============================
query = """
SELECT name
FROM sqlite_master
WHERE type='table';
"""

tables = pd.read_sql(query, engine)

print("\n========== Database Tables ==========")
print(tables)