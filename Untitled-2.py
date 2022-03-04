g_income = float(input("Enter Your Gross Income:"))
dependents = int(input("Enter Number of Dependents:"))

standard_deduction = 10000
additional_deduction = dependents * 3000

total_deduction = standard_deduction + additional_deduction

x = g_income - total_deduction
income_tax = x * 0.20

print("The Income Tax is:", income_tax)