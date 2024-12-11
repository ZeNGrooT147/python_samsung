"""9. Check if it is cloudy or sunny. If sunny and hot, then go out with jacket. If only sunny the go out as you wish.
If it is cloudy, then check if it is raining. IF it is only cloudy then go out as you wish. IF rainy then check if it is lightning.
If it is raining and lightning, then do not go out. If it is only raining then either go out with umbrella or play in water. If it is only cloudy and lightning then do not go out. """


weather=input("Whether the atmosphere is cloudy or sunny(enter cloudy or sunny) : ").strip().lower()

if (weather=='sunny'):
    sunny =input('Whether it is Sunny and Hot (yes or no) : ')
    if sunny =='yes':
        print('Go out with jacket')
    elif sunny == 'no' :
        print(' Go out as you wish ')
    else :
            print('Wrong input')

elif (weather=='cloudy'):
    raining=input("Whether It is Raining (yes or no) ")
    if raining=='yes':
        print('Go out with umbrella')
    elif raining == 'no':
        print(' Go out as you wish ')
    else:
        print(' Invalid Input ')

else:
    print('Wrong input')