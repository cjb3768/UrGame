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
