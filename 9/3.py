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
    
car1 = Car("ABC-1", 142)

print(car1.regnum, car1.maxv, car1.v, car1.travdist)

print(car1.v)
car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
print(car1.v)
car1.accelerate(-200)
print(car1.v)