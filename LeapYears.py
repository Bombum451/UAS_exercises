print("Enter the year you want checked.")

year = int(input())
year = round(year,0)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(str(year) + " is a leap year.")
        else:
            print(str(year) + " is NOT a leap year.")
    else:
        print(str(year) + " is a leap year.")
else:
    print(str(year) + " is NOT a leap year.")