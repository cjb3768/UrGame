import logging
import board_space

####################
# Global variables #
####################
logger = logging.getLogger("urgame.space_type.rosette")

class rosette_space(board_space):
    def __init__(self):
        super().__init__(self, space_type.ROSETTE, "r")

    def check_if_placeable(self, piece):
        #In all rulesets, a rosette space is "safe"; you cannot capture a piece on one, which in simplified Finkle rules means you cannot land on one if it is occupied.
        return not self.stored_pieces

    # def capture_opposite_piece(self, piece):
    #     #In all rulesets we will support, one cannot capture a piece on a rosette.
    #     logger.error("Attempted to capture a piece on a rosette. This is not possible.")
    #     return false
