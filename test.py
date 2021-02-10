import pygame

pygame.init()

screen = pygame.display.set_mode((300, 300))

pygame.draw.rect(screen, (125, 125, 125,), (60, 60, 60, 60))

def click(event):
    print(event.pos[0], event.pos[1])

finished = False
while not finished:
    pygame.time.Clock().tick(30)
    # copying the text surface object
    # to the display surface object
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    pygame.display.update()
