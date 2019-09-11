import logging
import board_space

####################
# Global variables #
####################
logger = logging.getLogger("urgame.space_type.entry")

class entry_space(board_space):
    def __init__(self):
        super().__init__(self, space_type.ENTRY, "e")

    def test_placement(self, piece):
        #In all rulesets, pieces do not land on entry spaces; return false
        return false

    def test_capture(self, piece):
        #There is no way to land on an entry space, so capture is not possible; return false
        return false
