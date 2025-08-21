print("Please enter numbers.")

numbers = []
n = input()

while n != "":
    numbers.append(n)
    n = input()
        
numbers.sort(reverse=True)

i = 5

length = len(numbers)

for x in range(0, 5):
    print(numbers[length - i])
    i = i - 1
    
exit()