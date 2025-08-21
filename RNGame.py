import random

print("Guess the number.")

number = random.randint(1, 10)

n = input()

while n != number:
    if float(n) < number:
        print("Too low.")
    elif float(n) > number:
        print("Too high.")
    else:
        print("Correct!")
        exit()
    n = input()