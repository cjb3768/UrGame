import logging
import random
from src.board import *

####################
# Global variables #
####################
logger = logging.getLogger("urgame.game")

class game_flags:
    def __init__(self, n_dice = 4, n_pieces = 7, brd_flags = board_flags()):
        self.num_dice = n_dice
        self.num_pieces= n_pieces
        self.board_flags = brd_flags

class game_class:
    def __init__(self, flags=game_flags(), board = board_state()):
        self.flags = flags
        self.board_state = board

    def instantiate_board(self):
        #set a board's flags, construct the board, construct paths, and add pieces to the starting point of the board
        self.board_state.set_flags(self.flags.board_flags)
        self.board_state.construct_board()
        self.board_state.construct_path()
        #load starting points with num_pieces blank pieces
        for i in range(self.flags.num_pieces):
            #create blank pieces and store them in the board_state's piece lists
            self.board_state.light_piece_list.append(piece_type(True,True,self.board_state.get_player_entry(True).get_board_position()))
            self.board_state.dark_piece_list.append(piece_type(False,True,self.board_state.get_player_entry(False).get_board_position()))
            #append the pieces to the starting space's stored_pieces list
            self.board_state.get_player_entry(True).stored_pieces.append(self.board_state.light_piece_list[-1])
            self.board_state.get_player_entry(False).stored_pieces.append(self.board_state.dark_piece_list[-1])

        # #for print testing purposes, load pieces into other board_spaces
        # #testing exit spaces
        # self.board_state.board[0][6].stored_pieces.append(piece_type(True,True))
        # self.board_state.board[0][6].stored_pieces.append(piece_type(True,True))
        # self.board_state.board[0][6].stored_pieces.append(piece_type(False,True))
        #
        # #adding a flipped dark piece to (1,2)
        # self.board_state.board[1][2].stored_pieces.append(piece_type(False,False))
        # #adding a blank light piece to (1,4)
        # self.board_state.board[1][4].stored_pieces.append(piece_type(True,True))
        # #print board
        # self.board_state.print_board()

    def run_turn(self, player_color):
        """Handle the process of a turn in the game"""
        #roll dice, sum up total
        dice_score = self.roll_dice()
        #scan board for pieces that match player_color, construct list
            #created lists for this in the board_state; can update them as pieces move
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
