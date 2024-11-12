import pygame
import math

class Car:
    # constants
    carWidth = 20
    carHeight = 10

    def __init__(self, x, y, colour:str):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0

        # cosmetics
        self.colour = colour

    def changeSpeed(self, speedChange):
        self.speed += speedChange

    def steer(self, angleChange):
        self.angle += angleChange

    def move(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

    def draw(self, surface):
        # Create a rectangle representing the car
        car_surface = pygame.Surface((self.carWidth, self.carHeight))
        car_surface.fill(self.colour)
        car_surface.set_colorkey(("black"))

        # Rotate the rectangle
        rotated_car = pygame.transform.rotate(car_surface, -math.degrees(self.angle))
        rotated_rect = rotated_car.get_rect(center=(self.x, self.y))
        
        # Blit the rotated rectangle onto the display surface
        surface.blit(rotated_car, rotated_rect.topleft)
