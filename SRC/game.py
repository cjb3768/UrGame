import logging
import random
from src.board import *

####################
# Global variables #
####################
logger = logging.getLogger("urgame.game")

class game_flags:
    def __init__(self, n_dice = 4, brd_flags = board_flags()):
        self.num_dice = n_dice
        self.board_flags = brd_flags

class game_class:
    def __init__(self, flags=game_flags()):
        self.flags = flags

    def run_turn(self, player_color):
        """Handle the process of a turn in the game"""
        #roll dice, sum up total
        #scan board for pieces that match player_color, construct list
        #check to see which of those pieces can move, add to another sub-list
            #for each piece in list
                #for i in range(dice_score)
                    #if i < dice_score-1, check to see if a piece can advance
                    #when i == dice_score-1, check if piece can land
                    #if ever the answer is no, return False
                    #else pass
                #return True
            #if above returns true, add to sublist
        #select a move from the sublist of pieces that can move (needs to wait for user input)
        #advance dice_score-1 spaces
        #check to see if landing would cause a capture
            #if so, remove opposing piece, add a new piece to it's starting space
        #determine who gets next turn (typically other player, but in some cases a player gets an extra turn)
        pass

    def roll_dice(self):
        dice_score = 0

        #seed random number generator
        random.seed()
        for i in range(self.flags.num_dice):
            dice_score = dice_score + random.randint(0,1)
        return dice_score
