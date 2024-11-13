import math
import pygame

from config import display, ROAD_COLOUR

class Sensor:
    surface = display

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

    def detectColour(self, colour) -> bool:
        try:
            sensedColour = self.surface.get_at((int(self.x), int(self.y)))
            if sensedColour == colour:
                return True
            else: return False
        except IndexError:
            return False
    
    def draw(self):
        colour = "green" if self.detectColour(ROAD_COLOUR) else "red"
        pygame.draw.circle(self.surface, colour, (self.x, self.y), 2, 1)