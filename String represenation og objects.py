

class Car:
    speed = 0
    unit_of_speed = ""
    
    def __init__(self,speed,unit_of_speed):
        self.speed = speed
        self.unit_of_speed = unit_of_speed
    
    def __str__(self):
        return "Car with the maximum speed of "+str(self.speed)+" "+self.unit_of_speed

class Boat:
    speed = 0
    
    def __init__(self,speed):
        self.speed = speed
    
    def __str__(self):
        return "Boat with the maximum speed of "+str(self.speed)+" knots"
    
    