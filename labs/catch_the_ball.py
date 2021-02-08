import pygame
from pygame.draw import *
from random import randint
from math import sqrt

pygame.init()

FPS = 2
screen = pygame.display.set_mode((400, 400))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    global x, y, r
    """
    Draws ball in random place with random color and size
    :return: None
    """
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click(event):
    mouse_x = event.pos[0]
    mouse_y = event.pos[1]
    print(x, y, r)
    if is_click_inside_ball(mouse_x, x, mouse_y, y, r):
        print('Catch it!')
    else:
        print('Oops! You are missed!')



def is_click_inside_ball(x1, x2, y1, y2, r) -> bool:
    distance = sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
    return distance <= r

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
            print('Click!')

    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
