# Day 1 – Data Ingestion & Data Quality Assessment

## Objective

Set up the project environment, load all provided datasets using Pandas, perform initial data exploration, and assess overall data quality.

---

## Datasets Loaded

| Dataset | Rows | Columns |
|----------|---------|---------|
| Fund Master | 40 | 15 |
| NAV History | 46,000 | 3 |
| AUM by Fund House | 90 | 5 |
| Monthly SIP Inflows | 48 | 6 |
| Category Inflows | 144 | 3 |
| Industry Folio Count | 21 | 6 |
| Scheme Performance | 40 | 19 |
| Investor Transactions | 32,778 | 13 |
| Portfolio Holdings | 322 | 8 |
| Benchmark Indices | 8,050 | 3 |

---

## Data Quality Checks Performed

### Missing Value Analysis

| Dataset | Missing Values |
|----------|----------|
| Monthly SIP Inflows | 12 values in `yoy_growth_pct` |
| All Other Datasets | No Missing Values |

### Duplicate Record Analysis

- No duplicate records detected across any dataset.

### Data Type Assessment

- Numerical fields stored as Integer and Float.
- Categorical fields stored as Object.
- Date columns currently stored as Object and require conversion to Datetime format.

---

## Key Observations

1. Successfully loaded all 10 datasets using Pandas.
2. AMFI Code is consistently available across major datasets and can be used as the primary key.
3. NAV History contains 46,000 historical observations suitable for trend analysis.
4. Investor Transactions dataset contains 32,778 records for investor behavior analysis.
5. Portfolio Holdings dataset contains stock-level allocation information.
6. Benchmark Indices dataset contains 8,050 market index observations.

---

## Anomalies Identified

### Minor Issues

- `yoy_growth_pct` contains 12 missing values.
- Date columns require datatype conversion.
- `live_nav.csv` uses DD-MM-YYYY format while other datasets use YYYY-MM-DD format.

### Critical Issues

- No duplicate records found.
- No corrupted files detected.
- No missing AMFI Codes observed.
- No major data quality concerns identified.

---

## Conclusion

All datasets were successfully ingested and validated. Data quality is excellent with minimal missing values and no duplicate records. The datasets are ready for data cleaning, transformation, exploratory analysis, and database integration in subsequent phases of the project.