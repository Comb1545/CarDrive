import pygame
from config import *
from Car import Car
from drivers import userDriver

# declaring a car
car = Car(WIDTH // 2, HEIGHT // 2, CAR_COLOUR)

running = True
while running:
    display.blit(BACKGROUND, (0, 0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False


    userDriver(car, events)

    # pygame stuff
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()