from config import CAR_STEER, ACCEL_RATE, DECEL_RATE

controls = {
    "accel" : ACCEL_RATE, 
    "steerLeft" : -CAR_STEER, 
    "steerRight" : CAR_STEER, 
    "gearUP" : 1, 
    "gearDown" : -1
    }

class CarController:
    def __init__(self, car):
        self.car = car

    def control(self, action:list):
        if "accel" in action:
            self.car.accelerate(controls["accel"])
        else:
            self.car.decelerate(DECEL_RATE )
        if "steerLeft" in action:
            self.car.steer(controls["steerLeft"])
        if "steerRight" in action:
            self.car.steer(controls["steerRight"])
        if "gearUp" in action:
            self.car.changeGear(controls["gearUP"])
        if "gearDown" in action:
            self.car.changeGear(controls["gearDown"])

    def update(self):
        self.car.move()
        self.car.draw()