import random
import time

print("How many dice do you wish to roll?")

dice = int(input())
sum = 0

for x in range(0, dice):
    sum = sum + random.randint(1, 6)
    
print("Sum: " + str(sum))