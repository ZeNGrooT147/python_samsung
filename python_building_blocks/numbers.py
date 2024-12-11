#accept 3 distinct numbers from the user and find the biggets among them

#input_number1 = input ("Enter Number 1 : ")
#input_number2 = input ("Enter Number 2 : ")
#input_number3 = input ("Enter Number 3 : ")

input_number1 = 15 
input_number2 = 20
input_number3 = 15

if input_number1 > input_number2 and input_number1 > input_number3 :
    print(f"{input_number1} is The Biggest Number ")
elif input_number2 > input_number1 and input_number2 > input_number3 :
    print(f"{input_number2} is The Biggest Number ")
else :
    print(f"{input_number3} is The Biggest Number ")