""" 8. Check if it is cloudy or sunny. If sunny and hot, then go out with jacket. If only sunny the go out as you wish.
If it is cloudy, then check if it is raining. IF it is only cloudy then go out as you wish. IF rainy go out with umbrella."""

print("Whether the atmosphere is cloudy or sunny(enter cloudy or sunny)")

str1=input()

if (str1=='cloudy'):
    print("Whether It is Raining:(yes or no)")
    str2=input()
    if str2=='yes':
        print('Go out with umbrella')
    else:
        print('Go out as you Wish ')
elif (str1=='sunny'):
    print('Whether it is Sunny and Hot or just Sunny (enter both or sunny)')
    str3=input()
    if str3 =='both':
        print('Go out with jacket')
    elif str3 == 'sunny' :
        print(' Go out as you wish ')
    else :
            print('Wrong input')
else:
    print('Wrong input')
    