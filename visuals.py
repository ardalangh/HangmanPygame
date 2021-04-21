import pygame
from screeninfo import get_monitors



# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
HEIGHT = get_monitors()[0].height
WIDTH = get_monitors()[0].width


pygame.init()
surface = pygame.display.set_mode((HEIGHT, WIDTH)))


running = True
clock = pygame.time.Clock()
while running:
    pygame.event.pump()
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False