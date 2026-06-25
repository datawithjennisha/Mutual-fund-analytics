-- =========================================
-- Dimension Table: Fund
-- =========================================
CREATE TABLE IF NOT EXISTS dim_fund (
    fund_key INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER UNIQUE NOT NULL,
    scheme_name TEXT NOT NULL,
    fund_house TEXT,
    category TEXT,
    plan TEXT,
    risk_grade TEXT
);

-- =========================================
-- Dimension Table: Date
-- =========================================
CREATE TABLE IF NOT EXISTS dim_date (
    date_key INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE UNIQUE NOT NULL,
    day INTEGER,
    month INTEGER,
    quarter INTEGER,
    year INTEGER,
    weekday TEXT
);

-- =========================================
-- Fact Table: NAV
-- =========================================
CREATE TABLE IF NOT EXISTS fact_nav (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_key INTEGER,
    date_key INTEGER,
    nav REAL,

    FOREIGN KEY (fund_key) REFERENCES dim_fund(fund_key),
    FOREIGN KEY (date_key) REFERENCES dim_date(date_key)
);

-- =========================================
-- Fact Table: Investor Transactions
-- =========================================
CREATE TABLE IF NOT EXISTS fact_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_key INTEGER,
    date_key INTEGER,

    investor_id TEXT,
    transaction_type TEXT,
    amount_inr REAL,

    state TEXT,
    city TEXT,
    city_tier TEXT,

    age_group TEXT,
    gender TEXT,

    annual_income_lakh REAL,
    payment_mode TEXT,
    kyc_status TEXT,

    FOREIGN KEY (fund_key) REFERENCES dim_fund(fund_key),
    FOREIGN KEY (date_key) REFERENCES dim_date(date_key)
);

-- =========================================
-- Fact Table: Scheme Performance
-- =========================================
CREATE TABLE IF NOT EXISTS fact_performance (
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_key INTEGER,

    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,

    benchmark_3yr_pct REAL,

    alpha REAL,
    beta REAL,

    sharpe_ratio REAL,
    sortino_ratio REAL,

    std_dev_ann_pct REAL,
    max_drawdown_pct REAL,

    expense_ratio_pct REAL,
    morningstar_rating INTEGER,

    FOREIGN KEY (fund_key) REFERENCES dim_fund(fund_key)
);

-- =========================================
-- Fact Table: AUM
-- =========================================
CREATE TABLE IF NOT EXISTS fact_aum (
    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_key INTEGER,
    date_key INTEGER,

    aum_crore REAL,

    FOREIGN KEY (fund_key) REFERENCES dim_fund(fund_key),
    FOREIGN KEY (date_key) REFERENCES dim_date(date_key)
);