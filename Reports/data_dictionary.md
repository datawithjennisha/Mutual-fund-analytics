# Mutual Fund Analytics Data Dictionary

---

## nav_history

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Unique AMFI Scheme Code |
| date | DATE | NAV Date |
| nav | REAL | Net Asset Value |

---

## investor_transactions

| Column | Data Type | Description |
|---------|-----------|-------------|
| investor_id | TEXT | Unique Investor ID |
| transaction_date | DATE | Transaction Date |
| amfi_code | INTEGER | Mutual Fund Scheme Code |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | REAL | Transaction Amount |
| state | TEXT | Investor State |
| city | TEXT | Investor City |
| city_tier | TEXT | Tier 1 / Tier 2 / Tier 3 |
| age_group | TEXT | Investor Age Group |
| gender | TEXT | Male / Female |
| annual_income_lakh | REAL | Annual Income |
| payment_mode | TEXT | UPI / Cheque / Net Banking |
| kyc_status | TEXT | Verified / Pending |

---

## scheme_performance

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Scheme Code |
| scheme_name | TEXT | Mutual Fund Name |
| fund_house | TEXT | AMC Name |
| category | TEXT | Fund Category |
| return_1yr_pct | REAL | 1-Year Return |
| return_3yr_pct | REAL | 3-Year Return |
| return_5yr_pct | REAL | 5-Year Return |
| expense_ratio_pct | REAL | Expense Ratio |
| aum_crore | REAL | Assets Under Management |
| risk_grade | TEXT | Risk Classification |