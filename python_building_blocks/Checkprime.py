# prime number =  2 , 3, 5,7,11,13,17,19,23"
# composite number = 4,6,8,9,12
"""1=Not a prime number"""

input_number = int(input("Enter a number to Check the prime : "))

if(input_number == 0) or (input_number == 1):
    print(f" {input_number} is not a Prime Number")

elif (input_number % 2 == 0) or (input_number % 3 == 0) or (input_number % 4 == 0) or (input_number % 5 == 0) or (input_number % 6 == 0) or (input_number % 7 == 0) or (input_number % 8 == 0) or (input_number % 9 == 0):
    print(f" {input_number} is a Prime Number")

else:
    print(f" {input_number} is not a Prime Number")

