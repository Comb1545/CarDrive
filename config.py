import pygame

trackName = "RaceTrack1"
ROAD_COLOUR = (0, 0, 255)
FPS = 60
FONT = "Arial"
HUD_SIZE = 30

CAR_COLOUR = "red"
CAR_STEER = 3   # degrees
ACCEL_RATE = 0.2
DECEL_RATE = 0.2

controls = {
    "accel" : ACCEL_RATE, 
    "steerLeft" : -CAR_STEER, 
    "steerRight" : CAR_STEER, 
    "gearUP" : 1, 
    "gearDown" : -1
    }


# loading background image and window
TrackBackground = pygame.image.load(f"raceMaps/{trackName}.png")
BACKGROUND = TrackBackground
WIDTH = TrackBackground.get_width()
HEIGHT = TrackBackground.get_height()
display = pygame.display.set_mode((WIDTH, HEIGHT))

# init fonts for HUD
pygame.font.init()
font = pygame.font.SysFont(FONT, HUD_SIZE)

# init pygame stuff
pygame.init
clock = pygame.time.Clock()