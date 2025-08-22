print("How many numbers do you want in the list?")
n = int(input())
array = []

print("Now enter the numbers.")
i = input()

for x in range(1,n):
    array.append(i)
    i = int(input())
    
array.append(i)
thesum = 0
sum(array)

def sum():
    for x in array:
        thesum = int(thesum) + int(x)

print("The sum is: " + str(thesum))