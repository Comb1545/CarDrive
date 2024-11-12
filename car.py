import pygame
import math

from Sensor import Sensor

class Car:
    # Constants
    carWidth = 20
    carHeight = 10
    topSpeed = 10
    accelRate = 0.2
    decelRate = 0.1
    gears = {1: 0.1, 2: 0.2, 3: 0.3, 4: 0.4, 5: 0.5, 6: 0.6, 7: 0.7, 8: 0.8, 9: 0.9, 10: 1.0}

    def __init__(self, x, y, colour: str):
        self.x = x
        self.y = y
        self.angle = 0 # degrees
        self.speed = 0
        self.currentGear = 1
        self.sensors = [Sensor(self, 0, 0),     # center of car
                	    Sensor(self, 50, 0),    # out front
                        Sensor(self, 25, 30),   # front right
                        Sensor(self, 25, -30),  # front left
                        Sensor(self, 15, 90),   # right
                        Sensor(self, 15, 270)]  # left

        # Cosmetics
        self.colour = colour

    def changeGear(self, gear):
        if gear in self.gears:
            self.currentGear = gear

    def accelerate(self, isAccelerating):
        if isAccelerating:
            if self.speed < self.topSpeed * self.gears[self.currentGear]:
                self.speed += self.accelRate
        elif self.speed > 0:
            self.speed -= self.decelRate
            if self.speed < 0:
                self.speed = 0

    def steer(self, angleChange, surface):
        self.angle = (self.angle + angleChange) % 360
        self._manageSensors(surface)

    def move(self, surface):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))

        self._manageSensors(surface)

    def _manageSensors(self, surface):
        for sensor in self.sensors:
            sensor.updateLocation()
            sensor.draw(surface)

    def draw(self, surface):
        # Create a rectangle representing the car
        car_surface = pygame.Surface((self.carWidth, self.carHeight))
        car_surface.fill(self.colour)
        car_surface.set_colorkey("black")

        # Rotate the rectangle
        rotated_car = pygame.transform.rotate(car_surface, -self.angle)
        rotated_rect = rotated_car.get_rect(center=(self.x, self.y))
        
        # Blit the rotated rectangle onto the display surface
        surface.blit(rotated_car, rotated_rect.topleft)

    def drawHud(self, surface, font):
        speedText = font.render(f'Speed: {self.speed:.2f}', True, (0, 0, 0))
        angleText = font.render(f'Angle: {self.angle:.2f}', True, (0, 0, 0))
        gearText = font.render(f"Gear: {self.currentGear}/10", True, (0, 0, 0))

        surface.blit(speedText, (10, 10))
        surface.blit(angleText, (10, 50))
        surface.blit(gearText, (10, 90))
