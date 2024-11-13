import pygame
from config import font

def userDriver(car, events):
    actions = []
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        actions.append("steerLeft")
    if keys[pygame.K_RIGHT]:
        actions.append("steerRight")
    if keys[pygame.K_SPACE]:
        actions.append("accel")

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                actions.append("gearUp")
            elif event.key == pygame.K_DOWN:
                actions.append("gearDown")

    car.controller.control(actions)
    car.controller.update()
    car.drawHud(font)
    car.controller.displaymoves(actions)

    return actions
