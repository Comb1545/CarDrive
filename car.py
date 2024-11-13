import pygame
import math

from config import display, ROAD_COLOUR, WIDTH
from Sensor import Sensor
from CarController import CarController

class Car:
    # Constants
    carWidth = 20
    carHeight = 10
    topSpeed = 10
    gears = {1: 0.1, 2: 0.2, 3: 0.3, 4: 0.4, 5: 0.5, 6: 0.6, 7: 0.7, 8: 0.8, 9: 0.9, 10: 1.0}
    surface = display

    def __init__(self, x, y, colour: str):
        self.x = x
        self.y = y
        self.angle = 0 # degrees
        self.speed = 0
        self.currentGear = 1
        self.controller = CarController(self)
        self.sensors = [Sensor(self, 50, 0),    # out front
                        Sensor(self, 25, 30),   # front right
                        Sensor(self, 25, -30),  # front left
                        Sensor(self, 15, 90),   # right
                        Sensor(self, 15, 270)   # left
                    ]
        # Cosmetics
        self.colour = colour

    def changeGear(self, gear):
        if self.currentGear + gear in self.gears:
            self.currentGear += gear

    def accelerate(self, accelRate):
        if self.speed < self.topSpeed * self.gears[self.currentGear]:
            self.speed += accelRate
    
    def decelerate(self, decelRate):
        if self.speed > 0:
            self.speed -= decelRate
            if self.speed < 0:
                self.speed = 0

    def steer(self, angleChange):
        self.angle = (self.angle + angleChange) % 360
        self._manageSensors()

    def move(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))

        self._manageSensors()

    def _manageSensors(self):
        for sensor in self.sensors:
            sensor.updateLocation()
            sensor.draw()

    def draw(self):
        # Create a rectangle representing the car
        car_surface = pygame.Surface((self.carWidth, self.carHeight))
        car_surface.fill(self.colour)
        car_surface.set_colorkey("black")

        # Rotate the rectangle
        rotated_car = pygame.transform.rotate(car_surface, -self.angle)
        rotated_rect = rotated_car.get_rect(center=(self.x, self.y))
        
        # Blit the rotated rectangle onto the display surface
        self.surface.blit(rotated_car, rotated_rect.topleft)

    def drawHud(self, font):
        speedText = font.render(f"Speed: {self.speed:.2f}", True, (0, 0, 0))
        angleText = font.render(f"Angle: {self.angle:.2f}", True, (0, 0, 0))
        gearText = font.render(f"Gear: {self.currentGear}/10", True, (0, 0, 0))

        self.surface.blit(speedText, (10, 10))
        self.surface.blit(angleText, (10, 50))
        self.surface.blit(gearText, (10, 90))

        for i, sensor in enumerate(self.sensors):
            if sensor.detectColour(ROAD_COLOUR):
                onTrack = True
            else:
                onTrack = False
            sensorText = font.render(f"Sensor {i}: {onTrack}", True, (0, 0, 0))

            self.surface.blit(sensorText, (WIDTH - 200, 10 + (i * 30)))