import pygame
from screeninfo import get_monitors


class Buttons:
    def __init__(self):
        alphabet_string = string.ascii_lowercase
        self.letters = list(alphabet_string)
        self.h = 20
        self.w = 30

















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