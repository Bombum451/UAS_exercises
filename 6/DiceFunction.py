import random

dice = 0

def rollthedice():
    return random.randint(1, 6)

while dice != 6:
    dice = rollthedice()
    print("Dice roll result: " + str(dice))
    