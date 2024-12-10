# 4. Check if user given year is a leap year

print("Enter a year to check whether it is a leap year:")
input_year = int(input())

if input_year % 4 == 0 and input_year % 100 != 0 or input_year % 400 ==0:
    print(input_year,'is a leap year')