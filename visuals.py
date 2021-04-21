import pygame
from screeninfo import get_monitors


class Buttons:
    def __init__(self):
        alphabet_string = string.ascii_lowercase
        self.letters = list(alphabet_string)
        self.h = 20
        self.w = 30



class Button:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(self.letter, True, (255, 255, 255), (0,0,0))
        textRect = text.get_rect()
        textRect.center = (200 // 2, 200 // 2)
        pygame.draw.rect(surface, BLACK, (self.x, self.y, self.w, self.h), 1)
        surface.blit(text, textRect)














# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

HEIGHT = get_monitors()[0].height
WIDTH = get_monitors()[0].width




dic = {
    "a" : (10, 10),
    "b" : (20, 10),
    "d" : (30, 10),
    "e" : (10, 10),
    "r" : (10, 10),
    "a" : (10, 10),
}



buttons = Buttons()