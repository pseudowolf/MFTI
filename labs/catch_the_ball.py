import pygame
from pygame.draw import *
from random import randint
from math import sqrt

pygame.init()

FPS = 2
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Catch the ball!')


# Color variables
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, BLACK]

screen.fill(WHITE)

# Variable to store player's score
SCORE: int = 0

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font("freesansbold.ttf", 20)
# create a text suface object,
# on which text is drawn on it.
text = font.render('SCORE: ' + str(SCORE), True, BLUE, WHITE)
# create a rectangular object for the
# text surface object
textRect = text.get_rect()
# Set position of the textRect
textRect.topleft = (5, 5)


def new_ball():
    """
    Draws new ball with random size and color in random place
    """
    global x, y, r
    x = randint(100, 1000)
    y = randint(100, 800)
    r = randint(10, 100)
    color = COLORS[randint(0, 6)]
    circle(screen, color, (x, y), r)


def new_rect():
    """
    Draw new rectangle with random size and color
    :return: None
    """
    global size
    x = randint(100, 1000)
    y = randint(100, 800)
    size = randint(100, 300)
    color = COLORS[randint(0, 6)]
    rect(screen, color, (x, y, size, size))


def click(event):
    """
    Get click and check is click inside the ball or not.
    :param event: pygame.event
    :return: None
    """
    mouse_x = event.pos[0]
    mouse_y = event.pos[1]
    if is_click_inside_ball(mouse_x, x, mouse_y, y, r):
        print('Catch the ball!')
        update_score()
        print(SCORE)
    elif is_click_inside_rect(mouse_x, x, mouse_y, y, size):
        print('Catch the rect!')
        update_score()
        print(SCORE)
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


def is_click_inside_rect(x1, x2, y1, y2, s) -> bool:
    """
    Checks there is a mouse click inside the rectangle
    :param x1: x coordinate of the mouse click
    :param x2: x coordinate of the rect's origin
    :param y1: y coordinate of the mouse click
    :param y2: y coordinate of the rect's origin
    :param w: rect's width and height
    :return: Boolean
    """
    if x2 <= x1 and x1 <= x2 + s:
        if y2 <= y1 and y1 <= y2 + s:
            return True
    else:
        return False


def update_score():
    """
    Update SCORE variable
    :return: None
    """
    global text
    global SCORE
    SCORE += 1
    text = font.render('SCORE: ' + str(SCORE), True, BLUE, WHITE)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

# Game loop begins
while not finished:
    clock.tick(FPS)
    # copying the text surface object
    # to the display surface object
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    new_ball()
    new_rect()
    screen.blit(text, textRect)
    pygame.display.update()
    screen.fill(WHITE)

pygame.quit()
