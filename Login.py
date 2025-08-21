username = "python"
password = "rules"

status = 1

while status < 6:
    print("")
    print("")
    print("Enter the username.")
    UN = input()
    print("Enter the password.")
    PW = input()
    
    if UN != username or PW != password:
        status = status + 1
        if status < 5:
            print("Wrong credentials. Please try again. " + str(6 - status) + " attempts remaining.")
        elif status == 5:
            print("Wrong credentials. Please try again. 1 attempt remaining.")
        else:
            print("Access denied.")
    else:
        status = 6
        print("Welcome!")
    
exit()