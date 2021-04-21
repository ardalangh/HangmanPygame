import pygame
from ButtonContainer import ButtonsContainer

class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.x, self.y = self.screen.get_size()
        self.buttonContainer = ButtonsContainer(self.x, self.y * 0.2)
        self.buttonContainer.initDraw(self.screen)


    def render(self):
        self.screen.fill((0, 0,0))










