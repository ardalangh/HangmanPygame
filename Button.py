class Button:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.h = 20
        self.w = 30

    def draw(self, surface):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(self.letter, True, (255, 255, 255), (0,0,0))
        textRect = text.get_rect()
        textRect.center = (200 // 2, 200 // 2)
        pygame.draw.rect(surface, BLACK, (self.x, self.y, self.w, self.h), 1)
        surface.blit(text, textRect)
