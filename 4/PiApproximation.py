import random
import time

print("Enter how many random points you want in the simulation.")

N = int(input())

n = 0

start_time = time.time()

i = 0

while i < N:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    # print (str(x) + ", " + str(y))
    if ((x * x) + (y * y)) <= 1:
        n = n + 1
    i = i + 1
    
print("")
print("Approximation for pi: " + str((4 * n)/N))


time_elapsed = time.time()

print(str(round(time_elapsed - start_time,3)) + " seconds elapsed.")