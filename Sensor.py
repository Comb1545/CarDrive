import math
import pygame

class Sensor:
    def __init__(self, car, distance:int, angleOffset):
        self.car = car
        self.distance = distance
        self.angleOffset = angleOffset
        self.updateLocation()
    
    def updateLocation(self):
        # car angle plus sensor from car angle totaled
        angle = math.radians(self.car.angle + self.angleOffset)
        # vector changes into euclideiun
        self.x = self.car.x + self.distance * math.cos(angle)   # distance in x direction
        self.y = self.car.y + self.distance * math.sin(angle)   # distance in y direction

    def detectColour(self, surface, colour) -> bool:
        try:
            sensedColour = surface.get_at((int(self.x), int(self.y)))
            if sensedColour == colour:
                return True
            return False
        except IndexError:
            return False
    
    def draw(self, surface):
        #colour = "green" if self.detectColour(surface, "blue") else "red"
        if self.detectColour(surface, (0, 0, 255)):
            colour = "green"
        else:
            colour = "red"
        pygame.draw.circle(surface, colour, (self.x, self.y), 2)