def main():
    x, y = 300, 200
    width, height = 200, 300

    draw_house(x, y, width, height)


def draw_house_foudation(x, y, width, height):
    """

    :param x:
    :param y:
    :param width:
    :param height:
    :return:
    """
    print('Типа рисую фундамент...', x, y, width, height)
    pass

def draw_house_walls(x, y, width, height):
    """

    :param x:
    :param y:
    :param width:
    :param height:
    :return:
    """
    print('Типа рисую стены...', x, y, width, height)
    pass

def draw_house_roof(x, y, width, height):
    """"""
    print('Типа рисую крышу...', x, y, width, height)
    pass


def draw_house(x, y, width, height):
    """
    House drawing function with width and height from base point x, y
    in the middle bottom of house
    :param x: coordinate x of middle of house
    :param y: coordinate y of bottom of house
    :param width: full width of house
    :param height: full height of house
    :return: None
    """
    print('Типа рисую дом...', x, y, width, height)
    foundation_height = 0.05 * height
    walls_height = 0.5 * width
    walls_width = 0.9 * width
    roof_height = height - foundation_height - walls_height
    draw_house_foudation(x, y, width, foundation_height)
    draw_house_walls(x, y - foundation_height, walls_width, walls_height)
    draw_house_roof(x, y - foundation_height - walls_height, width, roof_height)


main()
