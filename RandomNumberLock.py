import random

i = 0

threecode = ""
fourcode = ""

while i < 3:
    n = random.randint(0, 9)
    if str(n) not in threecode:
        threecode = threecode + str(n)
        i = i + 1
        
i = 0

while i < 4:
    n = random.randint(1, 6)
    if str(n) not in fourcode:
        fourcode = fourcode + str(n)
        i = i + 1
        
print(threecode)
print(fourcode)