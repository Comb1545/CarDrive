from config import DECEL_RATE, controls, ROAD_COLOUR, display, font

class CarController:
    def __init__(self, car):
        self.car = car

    def getAttributes(self) -> list:
        attributes = []

        speed = self.car.speed
        angle = self.car.angle
        gearTopSpeed = self.car.topSpeed * self.car.gears[self.car.currentGear]
        sensors = [sensor.detectColour(ROAD_COLOUR) for sensor in self.car.sensors]

        attributes.append(speed)
        attributes.append(angle)
        attributes.append(gearTopSpeed)
        [attributes.append(sensor) for sensor in sensors] # append each sensor from list

        return attributes

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

    def displaymoves(self, action):
        for i, action in enumerate(action):
            text = font.render(f"{action=}", True, (0, 0, 0))

            display.blit(text, (180, 10 + i * 30))

    def update(self):
        self.car.move()
        self.car.draw()