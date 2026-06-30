# Input name 
name = input("Enter your name: ")
print(f"Hello {name}! Lets calculate your budget.\n")

# Income
MonthlySalary = float(input("Enter your Monthly Salary: "))
SideIncome = float(input("Enter your side income: "))
OtherIncome = float(input("Enter your other income: "))
TotalIncome = MonthlySalary + SideIncome + OtherIncome

# Expenses 
rent = float(input("Enter your rent: "))
LightBill = float(input("Enter your light bill: "))
GasBill = float(input("Enter your gas bill: "))
food = float(input("Enter your food bill: "))
transport = float(input("Enter your Transport bill: "))
OtherExpenses = float(input("Enter your other expenses: "))
TotalExpenses = rent + LightBill + GasBill + food + transport + OtherExpenses

# Budget Analysis
remaining = TotalIncome - TotalExpenses

print("\n--- BUDGET REPORT ---")
print(f"Total Income: ${TotalIncome:.2f}")
print(f"Total Expenses: ${TotalExpenses:.2f}")
print(f"Remaining Money: ${remaining: 2f}")

# Status
if remaining > 0:
    print("You are saving money")
elif remaining == 0:
    print("You are breaking even")
else :
    print("You are overspending!!!!")

# Saving percentage
if TotalIncome > 0:
    SavingPercentage = (remaining / TotalIncome) * 100
    print(f"Percentage of income saved: {SavingPercentage:.1f}%")
else :
    print("Income is Zero,cannot calculate savings perentage.")





