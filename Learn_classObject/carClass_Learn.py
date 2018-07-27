class Car:
    speed=0
    def driveTime(self,distance):
        time = distance/self.speed
        print time


oldCar = Car()
oldCar.speed = 60.0
oldCar.driveTime(100.0)
oldCar.driveTime(200.0)

newCar = Car()
newCar.speed = 150.0
newCar.driveTime(100.0)
newCar.driveTime(200.0)