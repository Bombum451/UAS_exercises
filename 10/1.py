
class Elevator:
    def __init__(self, minfloor, maxfloor):
        self.minfloor = minfloor
        self.maxfloor = maxfloor
        self.floor = minfloor
        
    def go_to_floor(self, floor):
        if (floor <= self.maxfloor) and (self.minfloor <= floor):
            while self.floor != floor:
                if self.floor < floor:
                    self.floor_up()
                if self.floor > floor:
                    self.floor_down()
                print("Elevator at floor " + str(self.floor))
            
    def floor_up(self):
        self.floor = self.floor + 1
        
    def floor_down(self):
        self.floor = self.floor - 1
    
h = Elevator(0,5)

h.go_to_floor(5)