import logging
import board_space

####################
# Global variables #
####################
logger = logging.getLogger("urgame.space_type.unmarked")

class unmarked_space(board_space):
    def __init__(self):
        super().__init__(self, space_type.UNMARKED, "u")
