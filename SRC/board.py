import logging
from enum import Enum, unique, auto
import sys
from SRC.SPACES.board_space import *
from SRC.SPACES.entry_space import *
from SRC.SPACES.exit_space import *
from SRC.SPACES.unmarked_space import *
from SRC.SPACES.rosette_space import *
from SRC.SPACES.conversion_space import *
from SRC.SPACES.null_space import *



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
    def __init__(self):
        self.foureyes = False
        self.passage = False
        self.foursquares = False
        self.conversion = False
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
            logger.error("While trying to set the board's path type an exception of type {} has occurred".format(type(e).__name__))
            logger.error(e)


class board_state:
    def __init__(self):
        #instantiate our 3x9 array of board_spaces; we will actually fill it with board_space data later
        self.board = [[0 for j in range(9)] for i in range(3)]
        self.flags = board_flags()

    def set_board_space(self, row, column, space):
        self.board[row][column] = space

    def construct_board(self):
        #set entrance spaces
        self.set_board_space(0, 5, entry_space())
        self.set_board_space(2, 5, entry_space())

        #set exit spaces based on path
        if self.flags.path_type == path_type.ADVANCED:
            #has only one exit at (1,0) and two extra null spaces at (0,6) and (2,6)
            self.set_board_space(1, 0, exit_space())
            self.set_board_space(0, 6, null_space())
            self.set_board_space(2, 6, null_space())
        else:
            #both other paths have exits at (0,6) and (2,6) and an extra null space at (1,0)
            self.set_board_space(0, 6, exit_space())
            self.set_board_space(2, 6, exit_space())
            self.set_board_space(1, 0, null_space())

        #set remaining null spaces
        self.set_board_space(0, 0, null_space())
        self.set_board_space(2, 0, null_space())

        #set rosette spaces
        self.set_board_space(0, 1, rosette_space())
        self.set_board_space(0, 7, rosette_space())
        self.set_board_space(1, 4, rosette_space())
        self.set_board_space(2, 1, rosette_space())
        self.set_board_space(2, 7, rosette_space())

        #set foureyes spaces if enabled
        if self.flags.foureyes:
            #foureyes spaces at (0,2), (0,4), (1,7), (2,2), and (2,4)
            pass

        #set passage spaces if enabled
        if self.flags.passage:
            #passage spaces at (1,3) and (1,6)
            pass

        #set conversion spaces if enabled
        if self.flags.conversion:
            #conversion spaces at (0,8) and (2,8)
            pass

        #set foursquares space if enabled
        if self.flags.foursquares:
            #foursquares space at (1,1)
            pass

        #fill the rest of the board with unmarked spaces
        for j in range(9):
            for i in range(3):
                if self.board[i][j] == 0:
                    self.set_board_space(i, j, unmarked_space())

    def print_board(self):
        print("Current board path type is {}".format(self.flags.path_type.name))
        top_bottom_row_edge = "   -----------------       ---------"
        middle_row_edge = "   ---------------------------------"
        row_string = ""

        print(top_bottom_row_edge)
        for i in range(3):
            row_string = ""
            for j in range(9):
                row_string = row_string + " {} ".format(self.board[i][j].board_symbol)
                if self.board[i][j].space_type == space_type.ENTRY:
                    row_string = row_string + " "
                else:
                    row_string = row_string + "|"

            print(row_string)
            if i < 2:
                print(middle_row_edge)

        print(top_bottom_row_edge)
