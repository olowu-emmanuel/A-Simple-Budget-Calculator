# Simple Budget Report Generator 📊

This is a straightforward Python command-line script I wrote to quickly analyze monthly finances. 

Unlike my dynamic budget calculator, this version uses fixed, predefined categories (like Rent, Light Bill, and Food) to quickly gather your data. It calculates your total income versus total expenses, tells you your financial status, and calculates the exact percentage of your income that you managed to save.

# What it does
* Fixed Category Tracking: Sequentially asks for specific income sources and common household bills to keep data entry quick and predictable.
* Instant Budget Report: Generates a formatted summary showing total income, total expenses, and the remaining balance.
* Financial Health Check: Uses `if/elif/else` conditions to evaluate your remaining balance and alert you if you are saving money, breaking even, or overspending.
* Savings Percentage Calculation: Does the math to show exactly what percentage of your total income was saved, complete with a logical safeguard to prevent division-by-zero errors if the income is entered as zero.

# How to run it locally
If you want to run this quick check on your finances, clone the repository and run the Python file.

Using your terminal (assuming you save the file as `simple_budget.py`):
```bash
python simple_budget.py
