
name = input (" Enter the name of the Employee: ")
emp_id = int (input(" Enter the Employee ID : "))
basic_salary = float (input(" Enter the Basic Salary of the Employee : "))
special_allowances_monthly = float (input(" Enter the Special Allowances per month of the Employee : "))
bonus_percentage = float (input(" Bonus Percentage of the Employee per year : "))

gross_monthly_salary = basic_salary + special_allowances_monthly 
annual_gross_salary = ( gross_monthly_salary * 12) + (bonus_percentage/100) * ( 12 * gross_monthly_salary )
standard_deduction = 50000
taxable_income = annual_gross_salary - standard_deduction

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
print(f'Taxable Income = {taxable_income}')

print("Tax Slab:\n(*) $ 0 - $ 3,00,000 : 0% \n(*) $ 3,00,001 - $ 6,00,000 : 5% \n(*) $ 6,00,001 - $ 9,00,000 : 10% \n(*) $ 9,00,001 - $ 12,00,000 : 15% \n(*) $ 12,00,001 - $ 15,00,000 : 20% \n(*) $ Above $ 15,00,000 : 30% \n")
rebate=input("Do the 87A Rebate Apply for U(yes or no)")
if rebate == 'yes':
    

tax_salary =120000


net_salary = annual_gross_salary - tax_salary
print('')




