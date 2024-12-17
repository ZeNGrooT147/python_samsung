# Level 1 : Displaying

name = input (" Enter the name of the Employee: ")
emp_id = int (input(" Enter the Employee ID : "))
basic_salary = float (input(" Enter the Basic Salary of the Employee : "))
special_allowances_monthly = float (input(" Enter the Special Allowances per month of the Employee : "))
bonus_percentage = float (input(" Bonus Percentage of the Employee per year : "))

# Level 2 : Level 2: Taxable Income Calculation

"""Objective: Calculate taxable income after standard deductions.
Tasks:
• Deduct a Standard Deduction of ₹50,000 from the annual gross salary.
• Compute the Taxable Income and display all intermediate calculations.
Output: Display gross salary, standard deduction and taxable income"""

gross_monthly_salary = basic_salary + special_allowances_monthly 
annual_gross_salary = ( gross_monthly_salary * 12) + (bonus_percentage/100) * ( 12 * gross_monthly_salary )
standard_deduction = 50000
taxable_salary = annual_gross_salary - standard_deduction

"""
print("*************************************")
print(f" The Name of the Employee is {name} ")
print(f" The ID of the Employee is {emp_id} ")
print(f" The Basic Salary of the Employee is {basic_salary} ")
print(f" The Special Allowances per month of the Employee is {special_allowances_monthly} ")
print(f" The Bonus Percentage of the Employee is {bonus_percentage} ")
print(f" The Gross Monthly Salary of the Employee is {gross_monthly_salary} ")
print(f" The Annual Gross Salary of the Employee is {annual_gross_salary} ")
"""

print('%-4s %-12s %-14s %-12s %-9s %-14s %-s '%("ID", "NAME", "BASIC-SALARY", "ALLOWANCES","BONUS(%)", "MONTHLY-SALARY", "ANNUAL-SALARY"))
print('-' * 85)
print('%-4d %-12s %-14.2f %-12.2f %-9.2f %-14.2f %-.2f' % (emp_id, name, basic_salary, special_allowances_monthly , bonus_percentage , gross_monthly_salary, annual_gross_salary))

print(f'\nStandard Deduction = {standard_deduction}')
print(f'Taxable Income = {taxable_salary}')

# Level 3 : Tax and Rebate Calculation

"""Objective: Compute tax payable using the New Tax Regime (2023) slabs.
Tasks:
1. Calculate tax based on the following slabs:
o ₹0 - ₹3,00,000: 0%
o ₹3,00,001 - ₹6,00,000: 5%
o ₹6,00,001 - ₹9,00,000: 10%
o ₹9,00,001 - ₹12,00,000: 15%
o ₹12,00,001 - ₹15,00,000: 20%
o Above ₹15,00,000: 30%
2. Apply Section 87A Rebate:
o Taxable income ≤ ₹7,00,000 → 100% rebate (tax payable = ₹0).
3. Add a 4% Health and Education Cess to the calculated tax.
Output:
• Display a detailed tax breakdown, including slabs, cess, and total tax payable."""

print("Tax Slab:\n(*) $ 0 - $ 3,00,000 : 0% \n(*) $ 3,00,001 - $ 6,00,000 : 5% \n(*) $ 6,00,001 - $ 9,00,000 : 10% \n(*) $ 9,00,001 - $ 12,00,000 : 15% \n(*) $ 12,00,001 - $ 15,00,000 : 20% \n(*) $ Above $ 15,00,000 : 30% \n")

tax_amount = 0

if taxable_salary >= 300001 and taxable_salary <= 600000:
	tax_amount_minus_cess = taxable_salary * 0.05
elif taxable_salary >= 600001 and taxable_salary <= 900000:
	tax_amount_minus_cess = taxable_salary * 0.1
elif taxable_salary >= 900001 and taxable_salary <= 120000:
	tax_amount_minus_cess = taxable_salary * 0.15
elif taxable_salary >= 1200001 and taxable_salary <= 1500000:
	tax_amount_minus_cess = taxable_salary * 0.2
elif taxable_salary >= 150000:
	tax_amount_minus_cess = taxable_salary * 0.3
	
tax_amount = tax_amount_minus_cess + tax_amount_minus_cess * 0.04

rebate=input("Do the 87A Rebate Apply for U(yes or no) : ")
if rebate == 'yes':
		if taxable_salary <= 700000:
			tax_amount = 0
    
print(f'Tax amount without Cess : {tax_amount_minus_cess}')

cess_amount = tax_amount - tax_amount_minus_cess

print(f'Cess : {cess_amount}')
print(f'Total Tax amount to pay : {tax_amount}')


#Level 4: Net Salary Calculation

"""
Objective: Calculate annual net salary after tax deductions.
Tasks:
1. Compute Net Salary = Annual Gross Salary - Total Tax Payable.
2. Display:
o Annual Gross Salary
o Total Tax Payable (including cess)
o Annual Net Salary

net_salary = gross_annual_salary - tax_amount
print gross_annual_salary
print tax_amount
print net_salary
-------------------------"""
# Level 5: Report Generation

"""Objective: Generate a detailed report for employees.
Tasks:
1. Summarize all computed details:
o Employee Details (Name, EmpID)
o Gross Monthly Salary
o Annual Gross Salary
o Taxable Income
o Tax Payable (with breakdown)
o Annual Net Salary
2. Format the output as a report for better readability.
Output:
• Provide a clean, tabular report for employees.
"""
