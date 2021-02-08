def main():
    x, y = 300, 200
    width, height = 200, 300

    draw_house(x, y, width, height)


def draw_house_foudation(x, y, width, height):
    """
    House foundation's drawing function with with and height and
    coordinates of point x middle bottom and y bottom of foundation
    :param x: middle point of foundation's bottom'
    :param y: foundation's bottom
    :param width: width of foundation
    :param height: height of foundation
    :return: None
    """
    print('Типа рисую фундамент...', x, y, width, height)
    pass


def draw_house_walls(x, y, width, height):
    """
    House wall's drawing function with with and height and
    coordinates of point x middle bottom and y bottom of walls
    :param x: middle bottom of walls
    :param y: bottom of walls
    :param width: width of walls
    :param height: height of walls
    :return: None
    """
    print('Типа рисую стены...', x, y, width, height)
    pass


def draw_house_roof(x, y, width, height):
    """
    House roof's drawing function with with and height and
    coordinates of point x middle bottom and y bottom of roof
    :param x: middle bottom of roof
    :param y: bottom of roof
    :param width: width of roof
    :param height: height of roof
    :return: None
    """
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
