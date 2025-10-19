import math

base_the_tuple = ["xvalue", "yvalue"]
base_the_elput = ["xvalue", "yvalue"]

base_the_tuple[0] = int(input("What is the X value? "))
base_the_tuple[1] = int(input("What is the Y value? "))

the_tuple = tuple(base_the_tuple)

def swap():
    base_the_elput[0] = the_tuple[1]
    base_the_elput[1] = the_tuple[0]
    return tuple(base_the_elput)

the_elput = swap()
print(the_elput)

distance = math.sqrt( math.pow( (the_elput[0] - the_tuple[0]), 2) + math.pow( (the_elput[1] - the_tuple[1]), 2) )

print("The distance between is " + str(distance))