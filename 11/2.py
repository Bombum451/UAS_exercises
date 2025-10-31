import random
from tabulate import tabulate

class Race:
    def __init__(self, name, cars):
        self.name = name
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
        
        
class Electric(Car):
    def __init__(self, regnum, maxv, battery):
        super().__init__(regnum, maxv)
        self.battery = battery
        
class Gasoline(Car):
    def __init__(self, regnum, maxv, fuel):
        super().__init__(regnum, maxv)
        self.fuel = fuel
    
    
thecars = []
carnum = 2

thecars.append(Electric("ABC-15", 180, "52.5 kWh"))
thecars.append(Gasoline("ACD-123", 165, "32.3 l"))

therace = Race("Electricity vs. Gasoline", thecars)

for x in range(3):
    therace.hour_passes()
    
therace.print_status()