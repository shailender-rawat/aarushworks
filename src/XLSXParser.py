# read XLSX File

import pandas as pd

# Load the dataset
df = pd.read_csv('sample_dataset.csv')

# for each record in df calculate following ratios


# Calculate Debt-to-Equity Ratio
debt_to_equity_ratio = df['Total Debt'] / df['Total Equity']

# Calculate Interest Coverage Ratio
interest_coverage_ratio = df['EBIT'] / df['Interest Expense']

# Calculate Current Ratio
current_ratio = df['Current Assets'] / df['Current Liabilities']

# Calculate Debt Service Coverage Ratio
debt_service_coverage_ratio = (df['EBIT'] + df['Depreciation']) / (df['Interest Expense'] + df['Principal Payments'])

# Calculate Fixed Charge Coverage Ratio
fixed_charge_coverage_ratio = (df['EBIT'] + df['Fixed Charges']) / (df['Interest Expense'] + df['Fixed Charges'])

# Calculate Leverage Ratio
leverage_ratio = df['Total Debt'] / df['Total Assets']

# Calculate Minimum Liquidity Ratio
minimum_liquidity_ratio = df['Cash and Equivalents'] / df['Current Liabilities']

# Calculate Capital Expenditure Ratio
capital_expenditure_ratio = df['Capital Expenditures'] / df['EBITDA']

# Calculate Working Capital Ratio
working_capital_ratio = (df['Current Assets'] - df['Current Liabilities']) / df['Total Assets']

# Calculate Minimum Net Worth
minimum_net_worth = df['Total Assets'] - df['Total Liabilities']

# Print the results
print('Debt-to-Equity Ratio:', debt_to_equity_ratio)
print('Interest Coverage Ratio:', interest_coverage_ratio)
print('Current Ratio:', current_ratio)
print('Debt Service Coverage Ratio:', debt_service_coverage_ratio)
print('Fixed Charge Coverage Ratio:', fixed_charge_coverage_ratio)
print('Leverage Ratio:', leverage_ratio)
print('Minimum Liquidity Ratio:', minimum_liquidity_ratio)
print('Capital Expenditure Ratio:', capital_expenditure_ratio)
print('Working Capital Ratio:', working_capital_ratio)
print('Minimum Net Worth:', minimum_net_worth)