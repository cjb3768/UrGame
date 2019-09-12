import logging
from SRC.SPACES.board_space import *

####################
# Global variables #
####################
logger = logging.getLogger("urgame.space_type.rosette")

class rosette_space(board_space):
    def __init__(self):
        super().__init__(space_type.ROSETTE, "r")

    def test_placement(self, piece):
        #In all rulesets, a rosette space is "safe"; you cannot capture a piece on one, which in simplified Finkle rules means you cannot land on one if it is occupied.
        return not self.stored_pieces

    def test_capture(self, piece):
        #In all rulesets, a rosette space is "safe"; you cannot capture a piece on one, so we return false.
        return False

    # def capture_opposite_piece(self, piece):
    #     #In all rulesets we will support, one cannot capture a piece on a rosette.
    #     logger.error("Attempted to capture a piece on a rosette. This is not possible.")
    #     return false
