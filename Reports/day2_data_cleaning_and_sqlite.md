Objective

The objective of Day 2 was to clean the raw mutual fund datasets, validate data quality, design a relational SQLite database using a Star Schema, load cleaned datasets into SQLite, and prepare analytical SQL queries for further analysis.

Tasks Completed
1. Data Cleaning

Performed data cleaning and validation on all provided datasets.

Cleaning Activities
Checked dataset structure using head(), shape, and info()
Identified missing values
Checked duplicate records
Converted date columns to datetime
Standardized text columns
Removed duplicate rows
Validated numeric fields
Saved cleaned datasets into the Data/Processed folder
Datasets Cleaned
Dataset	Cleaning Performed
fund_master	Date conversion, duplicate removal, text standardization
nav_history	Date conversion, sorting, forward fill, duplicate removal, NAV validation
aum_by_fund_house	Date conversion, duplicate removal, AUM validation
monthly_sip_inflows	Date conversion, duplicate removal, SIP validation
category_inflows	Date conversion, duplicate removal, category standardization
industry_folio_count	Date conversion, duplicate removal
scheme_performance	Numeric validation, expense ratio validation, duplicate removal
investor_transactions	Date conversion, transaction validation, KYC validation, duplicate removal
portfolio_holdings	Date conversion, weight validation, duplicate removal
benchmark_indices	Date conversion, index value validation, duplicate removal
Data Validation

The following business validations were performed:

NAV values must be greater than zero.
Expense Ratio must be between 0.1% and 2.5%.
Transaction Amount must be greater than zero.
Transaction Type standardized to:
SIP
Lumpsum
Redemption
KYC Status validated.
Duplicate records removed.
Date columns converted to datetime format.
SQLite Database Design

Designed a Star Schema for analytical reporting.

Dimension Tables
dim_fund
dim_date
Fact Tables
fact_nav
fact_transactions
fact_performance
fact_aum

Implemented:

Primary Keys
Foreign Keys
Relationships
AUTOINCREMENT Surrogate Keys
SQLite Database

Created:

bluestock_mf.db

Using:

sqlite3
schema.sql

Verified successful creation of all tables.

SQLAlchemy

Connected to SQLite using SQLAlchemy.

Loaded cleaned datasets into SQLite using:

create_engine()
DataFrame.to_sql()

Verified successful data loading.

SQL Deliverables

Prepared:

schema.sql
queries.sql

Analytical SQL queries include:

Top Funds by AUM
Monthly Average NAV
SIP Analysis
Transactions by State
Expense Ratio Analysis
Payment Mode Analysis
Highest NAV
Average Returns
KYC Status Summary
Fund-wise Transaction Count
Data Dictionary

Prepared a complete data dictionary documenting:

Column Names
Data Types
Business Definitions
Source References
Technologies Used
Python
Pandas
SQLite
SQLAlchemy
SQL
Git
GitHub
VS Code
Folder Structure
Mutual_funs_analytics/

│
├── Data/
│   ├── Raw/
│   └── Processed/
│
├── Data_cleaning/
│   ├── clean_nav_history.py
│   ├── clean_investor_transactions.py
│   ├── clean_scheme_performance.py
│   ├── create_database.py
│   └── load_data.py
│
├── SQL/
│   ├── schema.sql
│   └── queries.sql
│
├── Reports/
│   ├── data_dictionary.md
│   └── day2_summary.md
│
└── bluestock_mf.db
Key Learning Outcomes
Data Profiling
Data Cleaning using Pandas
Business Rule Validation
Missing Value Handling
Duplicate Detection
Datetime Conversion
Data Standardization
SQLite Database Creation
Star Schema Design
Fact and Dimension Modeling
Primary & Foreign Keys
SQLAlchemy Integration
Loading Data into SQLite
Writing Analytical SQL Queries
Git Version Control
Deliverables
10 Cleaned CSV Files
SQLite Database (bluestock_mf.db)
schema.sql
queries.sql
data_dictionary.md
Python Data Cleaning Scripts
Database Creation Script
Data Loading Script
Git Commit
Day 2: Cleaned data + SQLite DB loaded
Status

Day 2 Successfully Completed