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

    def __str__(self):
        #define a string function for a given space to print what the space looks like
        if not len(self.stored_pieces):
            #there are no pieces here; return it's board symbol with spaces
            return " {} ".format(self.board_symbol)
        else:
            #entry spaces may potentially hold multiple pieces of the same type; print how many there are
            return "{}/{}".format(len(self.stored_pieces), self.stored_pieces[0])
