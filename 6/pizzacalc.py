def pizzacalc(diameter, price):
    return ((float(diameter) * float(diameter) * 3.14)/float(price))
    
diameter = input("What's the diameter of the first pizza? ")
price = input("What's the price of the first pizza? ")

value1 = pizzacalc(diameter, price)

diameter = input("What's the diameter of the second pizza? ")
price = input("What's the price of the second pizza? ")

value2 = pizzacalc(diameter, price)

if value1 > value2:
    print("The first pizza has better value. Difference: " + str(value1/value2))
elif value1 < value2:
    print("The second pizza has better value. Difference: " + str(value2/value1))
else:
    print("Both pizzas have the same value.")