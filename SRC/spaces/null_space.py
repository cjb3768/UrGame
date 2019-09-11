import logging
import board_space

####################
# Global variables #
####################
logger = logging.getLogger("urgame.space_type.null")

class NULL_SPACE_EXCEPTION(Exception):
    pass

class null_space(board_space):
    def __init__(self):
        super().__init__(self, space_type.NULLSPACE, "X")

    def set_next_space(self, next_space, blank_state):
        #Null spaces should be inaccessible; throw an error
        raise NULL_SPACE_EXCEPTION

    def get_next_space(self, piece):
        #Null spaces should be inaccessible; throw an error
        raise NULL_SPACE_EXCEPTION

    def test_placement(self, piece):
        #Null spaces should be inaccessible; throw an error
        raise NULL_SPACE_EXCEPTION

    def test_capture(self, piece):
        #Null spaces should be inaccessible; throw an error
        raise NULL_SPACE_EXCEPTION
