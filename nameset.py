
names = {}
names = set(names)

def insert():
    prompt = input()
    
    if prompt == "":
        for x in names:
            print(x)
        quit()
    else:
        if prompt in names:
            print("Existing name")
        else:
            print("New name")
        
    names.add(prompt)
    insert()
    
insert()