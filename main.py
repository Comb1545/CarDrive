import pygame
from config import *
from Car import Car

# declaring a car
car = Car(WIDTH // 2, HEIGHT // 2, CAR_COLOUR)

# car control variables
steerLeft = False
steerRight = False
accelerate = False

running = True
while running:
    actions = []

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Car keys event handler
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                steerLeft = True
            elif event.key == pygame.K_RIGHT:
                steerRight = True
            elif event.key == pygame.K_SPACE:
                accelerate = True
            elif event.key == pygame.K_UP:
                actions.append("gearUp")
            elif event.key == pygame.K_DOWN:
                actions.append("gearDown")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                steerLeft = False
            elif event.key == pygame.K_RIGHT:
                steerRight = False
            elif event.key == pygame.K_SPACE:
                accelerate = False

    # Car movement logic
    if steerLeft:
        actions.append("steerLeft")
    if steerRight:
        actions.append("steerRight")
    if accelerate:
        actions.append("accel")

    # render logic
    display.blit(BACKGROUND, (0, 0))
    car.controller.control(actions)
    car.controller.update()
    car.drawHud(font)

    # pygame stuff
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()