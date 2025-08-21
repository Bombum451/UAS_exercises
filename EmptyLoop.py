print("Please enter numbers.")

smallest = 1000000000
largest = -1000000000
n = input()

while n != "":
    if float(n) < float(smallest):
        smallest = n
    elif float(n) > float(largest):
        largest = n
    n = input()
        
print("Smallest: " + str(smallest))
print("Largest: " + str(largest))
exit()