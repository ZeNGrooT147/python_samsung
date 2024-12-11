
print("\n Welcome to our Hotel Canara ")
menu={
    1 : 'Idli - vada',
    2 : 'Benne - dosa',
    3 : 'Poha',
    4 : 'Vada - Pav',
    5 : 'Puri'
}

print("\n1. Idli - vada\n2. Benne - dosa\n3. Poha\n4. Vada - Pav\n5. Puri\n")
food_number = int (input("Enter the food Number u want to order: "))

food = menu.get(food_number)

if food == 'invalid':
    print("The item is not present in the Menu")

print( f' Mam , here is you {food} ')