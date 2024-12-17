
# 6. Read a string from the user and check if it is raining, then either go out with umbrella or play in water.


input_data = input('Tell me if it is raining now (type raining if yes, anything else if no): ')

if input_data.lower() == "raining":
    print('Go out with Umbrella')
else:
    print('You can go out with out Umbrella')