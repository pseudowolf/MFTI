import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Evil Smile")

# Drawing is here...

background_color = (150, 150, 150)
rect(screen, background_color, (0, 0, 400, 400))
border_color = (0, 0, 0)

# smile
smile_color = (250, 250, 100)
smile_radius = 100
circle(screen, smile_color, (200, 200), smile_radius)
# smile's border
circle(screen, color=border_color, center=(200, 200), radius=101, width=1)

# eyes
eye_color = (255, 0, 0)
eye1_radius = 20
eye2_radius = 17
u_radius = 10
circle(screen, color=eye_color, center=(150, 180), radius=eye1_radius)
circle(screen, color=eye_color, center=(250, 180), radius=eye2_radius)
circle(screen, color=border_color, center=(150, 180), radius=u_radius)
circle(screen, color=border_color, center=(250, 180), radius=u_radius)
circle(screen, color=border_color, center=(150, 180), radius=eye1_radius + 1, width=1)
circle(screen, color=border_color, center=(250, 180), radius=eye2_radius + 1, width=1)

# brows
polygon(screen, border_color, ((80, 80), (70, 95), (160, 165), (170, 175)))

# mouths
rect(screen, border_color, (150, 250, 100, 20))

# window cicle
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

quit()
