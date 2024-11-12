import pygame
from car1 import Car


trackName = "RaceTrack1"
TrackBackground = pygame.image.load(f"raceMaps/{trackName}.png")

BACKGROUND = TrackBackground
WIDTH = TrackBackground.get_width()
HEIGHT = TrackBackground.get_height()

# init pygame stuff
pygame.init
clock = pygame.time.Clock()
display = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

# declaring a car
car = Car(WIDTH // 2, HEIGHT // 2, "red")
# car control variables
steerLeft = False
steerRight = False
accelerate = False
brake = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # car keys event handler
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                steerLeft = True
            elif event.key == pygame.K_RIGHT:
                steerRight = True
            elif event.key == pygame.K_UP:
                accelerate = True
            elif event.key == pygame.K_DOWN:
                brake = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                steerLeft = False
            elif event.key == pygame.K_RIGHT:
                steerRight = False
            elif event.key == pygame.K_UP:
                accelerate = False
            elif event.key == pygame.K_DOWN:
                brake = False


    # car movement logic
    if steerLeft:
        car.steer(-0.10)
    if steerRight:
        car.steer(0.10)
    if accelerate:
        car.changeSpeed(0.1)
    if brake:
        car.changeSpeed(-0.1)

    car.move()

    # render logic
    display.blit(BACKGROUND, (0, 0))
    car.draw(display)

    # pygame stuff
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()