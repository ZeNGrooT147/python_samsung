# 5. Check if user given number is 2 digit number

print("Enter a Number to check whether it is two digit number : ")
input_user =  int(input())

if input_user > 9 and input_user < 100 :
    print( input_user , ' is a two digit number')