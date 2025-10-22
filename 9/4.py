import random
from tabulate import tabulate

class Car:
    def __init__(self, regnum, maxv):
        self.regnum = regnum
        self.maxv = maxv
        self.v = 0
        self.travdist = 0
        
    def accelerate(self, delta):
        self.v = self.v + delta
        if self.v < 0:
            self.v = 0
        elif self.v > self.maxv:
            self.v = self.maxv
            
    def drive(self, time):
        self.travdist = self.travdist + (self.v * time)
    
for x in range(9):
    maxv = random.randint(100,200)
    globals()['car%s' % x] = Car("ABC-" + str(x + 1), maxv)
    
win = False

while win == False:
    for x in range(9):
        car = globals()['car%s' % x]
        delta = random.randint(-10,15)
        car.accelerate(delta)
        car.drive(1)
        print("ABC-" + str(x) + " accelerating by " + str(delta) + " and currently at " + str(car.travdist) + " km" )
    if car.travdist >= 10000:
        print("ABC-" + str(x) + " won the race")
        win = True
        
a = []
        
for x in range(9):
    car = globals()['car%s' % x]
    addition = (str(car.regnum), str(car.v), str(car.maxv), str(car.travdist))
    a.append(addition)

headers = ["Registration Number", "Current Speed", "Maximum Speed", "Traveled Distance"]

print(tabulate(a, headers = headers, tablefmt = "grid"))