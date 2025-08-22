import random

print("How many sides on the dice?")

n = int(input())

dice = 0

def rollthedice():
    return random.randint(1, n)

while dice != n:
    dice = rollthedice()
    print("Dice roll result: " + str(dice))
    