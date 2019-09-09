import logging
import enum
import sys
import SPACES

####################
# Global variables #
####################
logger = logging.getLogger("urgame.board")

## Dev-Note: Currently thinking of the board as a graph of board-spaces. The board_spaces would be responsible for knowing what's next on the board.
