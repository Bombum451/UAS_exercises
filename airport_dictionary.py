
airports = {
"EFHK" : "HELSINKI-VANTAA AIRPORT"
}

def interface():
    print("")
    print("1. Enter New Airport")
    print("2. Fetch Existing Airport")
    print("3. Quit")
    print("")
    
    prompt = input()
    prompt = prompt.upper()
    print("")
    
    if prompt == "1" or prompt == "ENTER" or prompt == "ENTER NEW" or prompt == "ENTER NEW AIRPORT":
        enter()
    elif prompt == "2" or prompt == "FETCH" or prompt == "FETCH EXISTING" or prompt == "FETCH EXISTING AIRPORT":
        fetch()
    elif prompt == "3" or prompt == "QUIT" or prompt == "EXIT":
        quit()
    else:
        error()
        
        
def error():
    print("This command is not recognized. Please try again.")
    interface()
    
def enter():
    name = input("Please enter airport name: ")
    code = input("Please enter airport code: ")
    name = name.upper()
    code = code.upper()
    airports[code] = name
    interface()
    
def fetch():
    code = input("Please enter airport code: ")
    code = code.upper()
    if code in airports:
        print(airports[code])
        interface()
    else:
        error()
        
interface()