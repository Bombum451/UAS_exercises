wage = float(input("How much do you get paid per hour? "))
time = int(input("How many hours do you work? "))
day = str(input("What's the day of the week? ")).lower()

if day == "sunday":
    wage = 2 * wage
    
print("Your daily wage for this day is " + str(wage * time))