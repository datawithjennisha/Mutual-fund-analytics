-- ===========================================
-- 1. Top 5 Funds by AUM
-- ===========================================
SELECT scheme_name, aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- ===========================================
-- 2. Average NAV by Month
-- ===========================================
SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS average_nav
FROM nav_history
GROUP BY month
ORDER BY month;

-- ===========================================
-- 3. Total SIP Amount
-- ===========================================
SELECT
SUM(amount_inr) AS total_sip_amount
FROM investor_transactions
WHERE transaction_type='SIP';

-- ===========================================
-- 4. Transactions by State
-- ===========================================
SELECT
state,
COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- ===========================================
-- 5. Funds with Expense Ratio < 1%
-- ===========================================
SELECT
scheme_name,
expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- ===========================================
-- 6. Average Investment by Payment Mode
-- ===========================================
SELECT
payment_mode,
AVG(amount_inr) AS average_amount
FROM investor_transactions
GROUP BY payment_mode;

-- ===========================================
-- 7. Top 10 Highest NAV
-- ===========================================
SELECT *
FROM nav_history
ORDER BY nav DESC
LIMIT 10;

-- ===========================================
-- 8. Average Returns
-- ===========================================
SELECT
AVG(return_1yr_pct) AS avg_1yr,
AVG(return_3yr_pct) AS avg_3yr,
AVG(return_5yr_pct) AS avg_5yr
FROM scheme_performance;

-- ===========================================
-- 9. Verified vs Pending KYC
-- ===========================================
SELECT
kyc_status,
COUNT(*) AS investors
FROM investor_transactions
GROUP BY kyc_status;

-- ===========================================
-- 10. Transactions by Fund
-- ===========================================
SELECT
amfi_code,
COUNT(*) AS transactions
FROM investor_transactions
GROUP BY amfi_code
ORDER BY transactions DESC;