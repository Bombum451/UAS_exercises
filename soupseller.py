name = str(input("What's your name? "))
name = name.upper()

banned = ["MATTI"]
price = 5.90

if name not in banned:
    portions = int(input("How many portions of soup? "))
    print("The total cost is " + str(portions * price) + " euros.")
    
print("Next, please!")