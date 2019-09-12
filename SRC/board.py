import logging
import enum
import sys
import SPACES

####################
# Global variables #
####################
logger = logging.getLogger("urgame.board")

## Dev-Note: Currently thinking of the board as a matrix of board-spaces. The board_spaces would be responsible for knowing what's next on the board.
@unique
class path_type(Enum):
    SIMPLE = 0
    MEDIUM = 1
    ADVANCED = 2


class board_flags:
    def __init(self):
        self.foureyes = false
        self.passage = false
        self.foursquares = false
        self.conversion = false
        self.path_type = path_type.SIMPLE

    def toggle_foureyes(self):
        self.foureyes = not self.foureyes

    def toggle_passage(self):
        self.passage = not self.passage

    def toggle_foursquares(self):
        self.foursquares = not self.foursquares

    def toggle_conversion(self):
        self.conversion = not self.conversion

    def set_path_type(self, type):
        try:
            self.path_type = path_type(type)
        except Exception as e:
            logger.error("While trying to construct the board, an exception of type {} has occurred".format(type(e).__name__))
            logger.error(e)


class board_state:
    def __init__(self):
        #instantiate our 3x9 array of board_spaces; we will actually fill it with board_space data later
        self.board = [[0 for j in range(9)] for i in range(3)]

    def set_board_space(self, row, column, space):
        self.board[row][column] = space

    def construct_board(self, board_flags):
        pass
