import logging
from SRC.spaces.board_space import *

####################
# Global variables #
####################
logger = logging.getLogger("urgame.space_type.unmarked")

class unmarked_space(board_space):
    def __init__(self, board_position):
        super().__init__(space_type.UNMARKED, "-", board_position)
