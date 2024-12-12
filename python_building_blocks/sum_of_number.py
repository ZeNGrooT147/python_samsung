import sys

input_number = int(sys.argv[1])
sum=0

while ( input_number > 0 ):
    for i in range(9):
        r = input_number % 10                        # 567 % 10 = 7
        input_number = input_number//10              # 567 // 10 = 56
        sum = sum + r                                # sum = 0 +7 = 7  

print(f" Sum = {sum} ")