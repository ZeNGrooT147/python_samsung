
# 18) Find Sum of Even Placed digits of a number (The Left most digit of the number is at position 1)

import sys
sum = 0
count = 1
input_number = sys.argv[1]
for i in input_number:
    i = int(i)
    if(count % 2== 0):
        if i % 2 == 0 :
            sum+=i
    count+=1
print(sum)