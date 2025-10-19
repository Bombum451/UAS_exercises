print("How many numbers do you want in the list?")
n = int(input())
array = []
array2 = []

print("Now enter the numbers.")
i = input()

for x in range(1,n):
    array.append(int(i))
    i = int(input())
    
array.append(int(i))
print(array)
    
def trim(array):
    for y in array:
        if y % 2 == 0:
            array2.append(y)
    return array2
    
array2 = trim(array)

print(array2)