import logging
from src.spaces.board_space import *

####################
# Global variables #
####################
logger = logging.getLogger("urgame.space_type.exit")

class exit_space(board_space):
    def __init__(self, board_position):
        super().__init__(space_type.EXIT, "f", board_position)

    def test_advancement(self, piece):
        #One cannot advance past an exit. Return false
        return False

    def test_placement(self, piece):
        #In all rulesets, pieces must land on an exit space to leave (it's one more than the last space on the board; landing on it is moving off), so return true
        return True

    def test_capture(self, piece):
        #There is no way to land on an opponent's piece off the board, so return false
        return False

    def count_pieces(self, piece_color):
        #count all the pieces of a given color
        piece_count = 0
        for i in range(len(self.stored_pieces)):
            if self.stored_pieces[i].get_color() == piece_color:
                piece_count = piece_count + 1
        return piece_count

    def __str__(self):
        #define a string function for a given space to print what the space looks like
        if not len(self.stored_pieces):
            #there are no pieces here; return it's board symbol with spaces
            return " {} ".format(self.board_symbol)
        else:
            #exit spaces may potentially hold multiple pieces of each color; print how many there are of each
            return "{}/{}".format(self.count_pieces(True), self.count_pieces(False))
