import math
input_number1 = int(input ('Enter a number to check it is Perfect Square : ')) //25
root = math.sqrt(input_number1) # root = 5.0
print(type(root))
root = math.floor(root) # root1 = 5
print(type(root))
if (root * root == input_number1):  # 5 * 5 == 25
    print(input_number1 , " is a Perfect Square ")
else:
    print(input_number1 , "is a not a Perfect Square")


