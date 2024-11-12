import pygame
import math

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
        self.angle = 0
        self.speed = 0
        self.currentGear = 1

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

    def steer(self, angleChange):
        # keeps angle looping between 0 - 360 degrees (2pi radians)
        self.angle = (self.angle + angleChange) % (2 * math.pi)

    def move(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

    def draw(self, surface):
        # Create a rectangle representing the car
        car_surface = pygame.Surface((self.carWidth, self.carHeight))
        car_surface.fill(self.colour)
        car_surface.set_colorkey("black")

        # Rotate the rectangle
        rotated_car = pygame.transform.rotate(car_surface, -math.degrees(self.angle))
        rotated_rect = rotated_car.get_rect(center=(self.x, self.y))
        
        # Blit the rotated rectangle onto the display surface
        surface.blit(rotated_car, rotated_rect.topleft)

    def drawHud(self, surface, font):
        speedText = font.render(f'Speed: {self.speed:.2f}', True, (0, 0, 0))
        angleText = font.render(f'Angle: {math.degrees(self.angle):.2f}', True, (0, 0, 0))
        gearText = font.render(f"Gear: {self.currentGear}/10", True, (0, 0, 0))

        surface.blit(speedText, (10, 10))
        surface.blit(angleText, (10, 50))
        surface.blit(gearText, (10, 90))
