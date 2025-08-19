print("What's the length of your zander in centimeters?")
length = float(input())

if length < 42:
    print("Release the fish back into the lake. Zander is " + str(42 - length) + " centimeters below the size requirement." )
elif length >= 42:
    print("Zander meets size requirement.")