
"""

Read as many strings as you wish from comman line. Each string has 2 parts which are seperated by space. The 1st part is name of the state and the 2nd part is its capital.
Now create 2 lists named states and capitals. And store the states from the command line Args into states and similarly the capitals.
Print the States and Capitals data in a table format. Apply proper formatting to the O/P.


Eg:
$ python states_capitals.py "goa panjim" "karnataka bengaluru" "haryana chandigarh" "odhisa bhubaneswar"

"""

import sys

states = []
capitals = []

for i in range(1, len(sys.argv)):
	index_of_space = argv[i].find(' ')
	states.append(argv[i][:index_of_space])
	capitals.append(argv[i][index_of_space+1:])
	
print('%-15 %-15s'%('STATE', 'CAPITAL'))
print('-' * 32)
for i in range(len(sys.argv)-1):
	print('%-15 %-15s'%(states[i], capitals[i]))