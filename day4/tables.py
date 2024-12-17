
# 1) Accept number from the user from command line and print its Math table for multiple upto 20

"""
N=12

12 * 1 = 12
12 * 2 = 24
.
12 * 20 = 240

"""

# cline1.py

import sys

# python table.py 14

input_number = int(sys.argv[1])

for i in range(1, 21):
    #print(f'{input_number} * {i} = {input_number * i}')
    print('%d * %02d = %03d'%(input_number, i, input_number*i))