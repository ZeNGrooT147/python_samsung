import sys


digits =[int (digit) for digit in sys.argv[1]]
print(digits)

print(f"Sum of digits = {(sum(digits))}")