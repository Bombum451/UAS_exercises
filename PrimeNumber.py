print("Enter a number.")

n = int(input())
divisors = 0

for x in range(1, n + 1):
    if n % x == 0:
        divisors = divisors + 1
        #print("divisible by " + str(x))

if divisors == 2:
    print("Prime number!")
else:
    print("Not a prime number.")
    
exit()