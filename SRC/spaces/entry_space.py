import logging
from src.spaces.board_space import *

####################
# Global variables #
####################
logger = logging.getLogger("urgame.space_type.entry")

class entry_space(board_space):
    def __init__(self, board_position):
        super().__init__(space_type.ENTRY, "e", board_position)

    def test_placement(self, piece):
        #In all rulesets, pieces do not land on entry spaces; return false
        return False

    def test_capture(self, piece):
        #There is no way to land on an entry space, so capture is not possible; return false
        return False
