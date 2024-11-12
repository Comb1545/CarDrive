import pygame
from Car import Car


trackName = "RaceTrack1"
TrackBackground = pygame.image.load(f"raceMaps/{trackName}.png")

BACKGROUND = TrackBackground
WIDTH = TrackBackground.get_width()
HEIGHT = TrackBackground.get_height()

# init fonts for HUD
pygame.font.init()
font = pygame.font.SysFont("Arial", 30)

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

running = True
while running:
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
                car.changeGear(car.currentGear + 1)
            elif event.key == pygame.K_DOWN:
                car.changeGear(car.currentGear - 1)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                steerLeft = False
            elif event.key == pygame.K_RIGHT:
                steerRight = False
            elif event.key == pygame.K_SPACE:
                accelerate = False


    # Car movement logic
    if steerLeft:
        car.steer(-3, display)
    if steerRight:
        car.steer(3, display)
    car.accelerate(accelerate)

    car.move(display)

    # render logic
    display.blit(BACKGROUND, (0, 0))
    car.move(display)
    car.draw(display)
    car.drawHud(display, font)

    # pygame stuff
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()