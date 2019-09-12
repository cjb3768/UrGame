import logging
import sys
from SRC import board

####################
# Global variables #
####################
logger = logging.getLogger("urgame")

####################
#    Functions     #
####################

def main():
    #set logging level to output all messages of DEBUG level or higher
    logging.basicConfig(level=logging.DEBUG)

    #print hello world
    logger.debug("Hello world")

    game_board = board.board_state()
    game_board.construct_board()
    game_board.print_board()
    game_board.flags.set_path_type(board.path_type.ADVANCED)
    game_board.construct_board()
    game_board.print_board()

if __name__ == "__main__":
    main()
