import pygame

pygame.init()
surface = pygame.display.set_mode((HEIGHT, WIDTH))

# Main Loop
running = True
clock = pygame.time.Clock()
while running:
    pygame.event.pump()
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False

    surface.fill(WHITE)

    p1 = (19, 19)
    p2 = (19, 60)
    p3 = (200, 19)
    p4 = (19, 200)
    p5 = (200, 50)
    p6 = (200, 90)
    p7 = (200, 160)
    pygame.draw.line(surface, BLACK, p1, p2, 1)
    pygame.draw.line(surface, BLACK, p2, p3, 1)
    pygame.draw.line(surface, BLACK, p3, p1, 1)
    pygame.draw.line(surface, BLACK, p1, p4, 1)
    pygame.draw.line(surface, BLACK, p3, p5, 1)
    pygame.draw.circle(surface, BLACK, (200, 70), 20, 1)
    pygame.draw.line(surface, BLACK, p6, p7, 1)
    pygame.draw.line(surface, BLACK, (200, 160), (250, 190), 1)
    pygame.draw.line(surface, BLACK, (200, 160), (150, 190), 1)
    pygame.draw.line(surface, BLACK, (200, 90), (150, 110), 1)
    pygame.draw.line(surface, BLACK, (200, 90), (250, 110), 1)
    pygame.draw.line(surface, BLACK, (0, 300), (400, 300), 1)

    # Letter Keys
    # pygame.draw.rect(surface, BLACK, (10,310,30,20),1)
    # pygame.draw.rect(surface, BLACK, (50, 310,30,20),1)
    # pygame.draw.rect(surface, BLACK, (90, 310,30,20),1)
    # pygame.draw.rect(surface, BLACK, (130, 310,30,20),1)
    # pygame.draw.rect(surface, BLACK, (170, 310,30,20),1)
    # pygame.draw.rect(surface, BLACK, (210, 310,30,20),1)
    # pygame.draw.rect(surface, BLACK, (250, 310,30,20),1)
    # pygame.draw.rect(surface, BLACK, (290, 310,30,20),1)
    # pygame.draw.rect(surface, BLACK, (330, 310,30,20),1)

    # pygame.draw.rect(surface, BLACK, (10, 340,30,20),1)
    # pygame.draw.rect(surface, BLACK, (50, 340,30,20),1)
    # pygame.draw.rect(surface, BLACK, (90, 340,30,20),1)
    # pygame.draw.rect(surface, BLACK, (130, 340,30,20),1)
    # pygame.draw.rect(surface, BLACK, (170, 340,30,20),1)
    # pygame.draw.rect(surface, BLACK, (210, 340,30,20),1)
    # pygame.draw.rect(surface, BLACK, (250, 340,30,20),1)
    # pygame.draw.rect(surface, BLACK, (290, 340,30,20),1)
    # pygame.draw.rect(surface, BLACK, (330, 340,30,20),1)

    pygame.font.init()  # you have to call this at the start,



    # pygame.draw.rect(surface, BLACK, (25,370,30,20),1)

    b = Buttons(100, 100, "i")

    b.draw(surface)

    # pygame.draw.rect(surface, BLACK, (65,370,30,20),1)
    # pygame.draw.rect(surface, BLACK, (105,370,30,20),1)
    # pygame.draw.rect(surface, BLACK, (145,370,30,20),1)
    # pygame.draw.rect(surface, BLACK, (185,370,30,20),1)
    # pygame.draw.rect(surface, BLACK, (225,370,30,20),1)
    # pygame.draw.rect(surface, BLACK, (265,370,30,20),1)
    # pygame.draw.rect(surface, BLACK, (305,370,30,20),1)
    # pygame.draw.rect(surface, BLACK, (345,370,30,20),1)

    pygame.display.flip()
    clock.tick(60)