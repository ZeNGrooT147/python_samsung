
# cline1.py

import sys

sum_of_numbers = 0
print('User given numbers are')
for i in range(1, len(sys.argv)):
    print(sys.argv[i], end = '  ')
    sum_of_numbers = sum_of_numbers + int(sys.argv[i])

print(f'\nSum of the {len(sys.argv)-1} user given numbers is {sum_of_numbers}')

# argv[0] argv[1] argv[2]