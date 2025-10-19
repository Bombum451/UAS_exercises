def convert():
    print("How many gallons?")
    n = int(input())
    if n < 0:
        exit()
    print("That's " + str(n * 3.785) + " litres!")
    print("")
    return(n)
    
n = 0.001

while 1:
    n = convert()