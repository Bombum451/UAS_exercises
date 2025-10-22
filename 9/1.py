class Car:
    def __init__(self, regnum, maxv):
        self.regnum = regnum
        self.maxv = maxv
        self.v = 0
        self.travdist = 0
    
car1 = Car("ABC-1", 142)

print(car1.regnum, car1.maxv, car1.v, car1.travdist)