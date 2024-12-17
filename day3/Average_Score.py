
average_score = int(input(' Enter the Average Score : '))

if average_score <= 49 and average_score >= 0 :  #Basically we need to use the condition first which is hard to pass
    print('Result = Fail ')
elif average_score <= 79:
    print('Result = Second Class')
elif average_score <= 95:
    print('Result = First Class')
elif average_score <= 100:
    print('Result = Distinction')
else:
    print(' Invalid Score ')

    
 




















