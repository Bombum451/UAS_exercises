seasons = ("Winter", "Spring", "Summer", "Autumn")
numbered_months = ( ("12", "1", "2"), ("3", "4", "5"), ("6", "7", "8"), ("9", "10", "11") )
# ( ("December", "January", "February"), ("March", "April", "May"), ("June", "July", "August"), ("September", "October", "November") )

def prompt():
    month = int(input("Please provide the number of a month: "))
    
    if month < 1 or month > 12:
        print("Invalid number value")
        exit()
        
    
    for x in range(len(numbered_months)):
        for y in range(len(numbered_months[x])):
            if numbered_months[x][y] == str(month):
                season = x
    
    print(seasons[season])
    print("")
    prompt()
    
prompt()