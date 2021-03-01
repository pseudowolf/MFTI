from enum import Enum
import pygame

FPS = 60
CELL_SIZE = 50


class Cell(Enum):
    VOID = 0
    CROSS = 1
    ZERO = 2


class Player:
    """
    Player class, consists type of sign
    """

    def __init__(self, name, cell_type):
        self.name = name
        self.cell_type = cell_type


class Gameboard:
    def __init__(self):
        self.height = 3
        self.width = 3
        self.cells = [[Cell.VOID] * self.width for i in range(self.height)]


class GameboardView:
    """
    Gameboard's widget, shows board on the screen, and checks mouse's click's place in the board
    """

    def __init__(self, board):
        # download cells sprites
        # show board's initial state
        self._board = board
        self._height = board.height * CELL_SIZE
        self._width = board.width * CELL_SIZE

    def draw(self):
        pass

    def check_coords_correct(self, x, y):
        # TODO: self._height учесть
        return True

    def get_coords(self, x, y):
        return 0, 0  # TODO: реально вычислить


class GameRoundManager:
    """
    Game manager
    """

    def __init__(self, player1: Player, player2: Player):
        self._players = [player1, player2]
        self._current_player = 0
        self.board = Gameboard()

    def handle_click(self, i, j):
        player = self._players[self._current_player]
        # player turn, clicks on the screen
        print('mouse click handled', i, j)


class GameWindow:
    """
    Include board's widget
    and game round manager
    """

    def __init__(self):
        # pygame initialization
        pygame.init()

        # window initialization
        self._width = 800
        self._height = 600
        self._title = 'Tic Tac Toe'
        self._screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption(self._title)

        self._board = Gameboard()
        self._board_widget = GameboardView(self._board)
        player1 = Player('Petya', Cell.CROSS)
        player2 = Player('Vasya', Cell.ZERO)
        # game manager initialization
        self._game_manager = GameRoundManager(player1, player2)
        self._board_widget = GameboardView(self._game_manager.board)

    def main_loop(self):
        finished = False
        clock = pygame.time.Clock()
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    x, y = mouse_pos
                    if self._board_widget.check_coords_correct(x, y):
                        i, j = self._board_widget.get_coords(x, y)
                        self._game_manager.handle_click(i, j)
            pygame.display.flip()
            clock.tick(FPS)


def main():
    window = GameWindow()
    window.main_loop()
    print('Game over!')


if __name__ == '__main__':
    main()
