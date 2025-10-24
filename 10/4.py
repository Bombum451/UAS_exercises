import random
from tabulate import tabulate

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
        
    def hour_passes(self):
        for x in range(carnum):
            car = self.cars[x]
            delta = random.randint(-10,15)
            car.accelerate(delta)
            car.drive(1)
            
    def print_status(self):
        a = []
        
        for x in range(carnum):
            car = self.cars[x]
            addition = (str(car.regnum), str(car.v), str(car.maxv), str(car.travdist))
            a.append(addition)
            
        headers = ["Registration Number", "Current Speed", "Maximum Speed", "Traveled Distance"]
        print(tabulate(a, headers = headers, tablefmt = "grid"))
        
    def race_finished(self):
        win = False
        for x in range(carnum):
            car = self.cars[x]
            if car.travdist >= self.distance:
              win = True
        return win
        
    def wincar(self):
        for x in range(carnum):
            car = self.cars[x]
            if car.travdist >= self.distance:
              return str(car.regnum)
                
    
        
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
    
    
thecars = []
hour = 0
carnum = 10

for x in range(carnum):
    maxv = random.randint(100,200)
    thecars.append(Car("ABC-" + str(x + 1), maxv))
    
therace = Race("Grand Demolition Derby", 8000, thecars)

while therace.race_finished() != True:
    therace.hour_passes()
    hour = hour + 1
    if hour == 10:
        therace.print_status()
        hour = 0

therace.print_status()

print(therace.wincar() + " wins the " + str(therace.name))