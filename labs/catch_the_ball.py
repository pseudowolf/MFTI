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
    """
    Get click and check is click inside the ballor not
    :param event: pygame.event
    :return: None
    """
    mouse_x = event.pos[0]
    mouse_y = event.pos[1]
    print(x, y, r)
    if is_click_inside_ball(mouse_x, x, mouse_y, y, r):
        print('Catch it!')
    else:
        print('Oops! You are missed!')


def is_click_inside_ball(x1, x2, y1, y2, r) -> bool:
    """
    Calculates the distance between two points and
    returns True if is smaller than ball's radius.
    :param x1: first point's x-coordinate
    :param x2: second point's x-coordinate'
    :param y1: first point's y-coordinate'
    :param y2: second point's y-coordinate'
    :param r: ball's radius'
    :return: bool
    """
    distance = sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)
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

    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
