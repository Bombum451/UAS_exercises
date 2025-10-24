
class Building:
    def __init__(self, minfloor, maxfloor, elevators):
        self.minfloor = minfloor
        self.maxfloor = maxfloor
        self.elevators = elevators
        self.elevatorlist = []
        
        for x in range(elevators):
            self.elevatorlist.append(Elevator(minfloor, maxfloor))
            
    def run_elevator(self, elevator, floor):
        self.elevatorlist[elevator].go_to_floor(floor)
            

class Elevator:
    def __init__(self, minfloor, maxfloor):
        self.minfloor = minfloor
        self.maxfloor = maxfloor
        self.floor = minfloor
        
    def go_to_floor(self, floor):
        if (floor <= self.maxfloor) and (self.minfloor <= floor):
            print("Elevator at floor " + str(self.floor))
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
    
h = Building(0,5,3)

h.run_elevator(1,5)