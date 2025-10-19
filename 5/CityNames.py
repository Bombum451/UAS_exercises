print("Enter the names of 5 cities.")
print("* * *")

cities = []
city = input()

for x in range(1,5):
    cities.append(city)
    city = input()
    
cities.append(city)

print("* * *")
    
for x in cities:
    print(x)