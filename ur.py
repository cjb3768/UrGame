import logging
import sys
from src.board import *
from src.game import *

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

    game_board = board_state()
    game_board.construct_board()
    game_board.print_board()
    game_board.construct_path(0)
    game_board.print_path(True)
    game_board.print_path(False)
    #game_board.flags.set_path_type(board.path_type.ADVANCED)
    #game_board.construct_board()
    #game_board.print_board()

    ur_game = game_class()
    print("Rolling dice: {}".format(ur_game.roll_dice()))
    print("Rolling dice: {}".format(ur_game.roll_dice()))
    print("Rolling dice: {}".format(ur_game.roll_dice()))
    print("Rolling dice: {}".format(ur_game.roll_dice()))

if __name__ == "__main__":
    main()
