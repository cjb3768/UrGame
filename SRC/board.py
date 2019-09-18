import logging
from enum import Enum, unique, auto
import sys
from src.spaces.board_space import *
from src.spaces.entry_space import *
from src.spaces.exit_space import *
from src.spaces.unmarked_space import *
from src.spaces.rosette_space import *
from src.spaces.conversion_space import *
from src.spaces.null_space import *


####################
# Global variables #
####################
logger = logging.getLogger("urgame.board")

## Dev-Note: Currently thinking of the board as a matrix of board-spaces. The board_spaces would be responsible for knowing what's next on the board.
@unique
class path_type(Enum):
    SIMPLE = 0
    MEDIUM = 1
    ADVANCED = 2


class board_flags:
    def __init__(self, foureyes = False, passage = False, foursquares = False, conversion = False, path = path_type.SIMPLE):
        self.foureyes = foureyes
        self.passage = passage
        self.foursquares = foursquares
        self.conversion = conversion
        self.path_type = path

    def toggle_foureyes(self):
        self.foureyes = not self.foureyes

    def toggle_passage(self):
        self.passage = not self.passage

    def toggle_foursquares(self):
        self.foursquares = not self.foursquares

    def toggle_conversion(self):
        self.conversion = not self.conversion

    def set_path_type(self, type):
        try:
            self.path_type = path_type(type)
        except Exception as e:
            logger.error("While trying to set the board's path type an exception of type {} has occurred".format(type(e).__name__))
            logger.error(e)


class board_state:
    def __init__(self, board=[[0 for j in range(9)] for i in range(3)], flags=board_flags()):
        #instantiate our 3x9 array of board_spaces; we will actually fill it with board_space data later
        self.board = board
        self.flags = flags
        self.light_entry = None
        self.light_exit = None
        self.dark_entry = None
        self.dark_exit = None
        self.light_piece_list = []
        self.dark_piece_list = []

    def set_board_space(self, row, column, space):
        self.board[row][column] = space

    def set_player_entry(self, row, column, color):
        if color:
            self.light_entry = self.board[row][column]
        else:
            self.dark_entry = self.board[row][column]

    def set_player_exit(self, row, column, color):
        if color:
            self.light_exit = self.board[row][column]
        else:
            self.dark_exit = self.board[row][column]

    def get_player_entry(self, color):
        if color:
            return self.light_entry
        else:
            return self.dark_entry

    def get_player_exit(self, color):
        if color:
            return self.light_exit
        else:
            return self.dark_exit

    def set_flags(self, flags):
        self.flags = flags

    def construct_board(self):
        #set entrance spaces
        self.set_board_space(0, 5, entry_space((0,5)))
        self.set_board_space(2, 5, entry_space((2,5)))
        #tag entrance spaces
        self.set_player_entry(0, 5, True)
        self.set_player_entry(2, 5, False)

        #set exit spaces based on path
        if self.flags.path_type == path_type.ADVANCED:
            #has only one exit at (1,0) and two extra null spaces at (0,6) and (2,6)
            self.set_board_space(1, 0, exit_space((1,0)))
            self.set_board_space(0, 6, null_space((0,6)))
            self.set_board_space(2, 6, null_space((2,6)))
            #tag exit space
            self.set_player_exit(1, 0, True)
            self.set_player_exit(1, 0, False)
        else:
            #both other paths have exits at (0,6) and (2,6) and an extra null space at (1,0)
            self.set_board_space(0, 6, exit_space((0,6)))
            self.set_board_space(2, 6, exit_space((2,6)))
            self.set_board_space(1, 0, null_space((1,0)))
            #tag exit spaces
            self.set_player_exit(0, 6, True)
            self.set_player_exit(2, 6, False)

        #set remaining null spaces
        self.set_board_space(0, 0, null_space((0,0)))
        self.set_board_space(2, 0, null_space((2,0)))

        #set rosette spaces
        self.set_board_space(0, 1, rosette_space((0,1)))
        self.set_board_space(0, 7, rosette_space((0,7)))
        self.set_board_space(1, 4, rosette_space((1,4)))
        self.set_board_space(2, 1, rosette_space((2,1)))
        self.set_board_space(2, 7, rosette_space((2,7)))

        #set foureyes spaces if enabled
        if self.flags.foureyes:
            #foureyes spaces at (0,2), (0,4), (1,7), (2,2), and (2,4)
            pass

        #set passage spaces if enabled
        if self.flags.passage:
            #passage spaces at (1,3) and (1,6)
            pass

        #set conversion spaces if enabled
        if self.flags.conversion:
            #conversion spaces at (0,8) and (2,8)
            self.set_board_space(0, 8, conversion_space((0,8)))
            self.set_board_space(2, 8, conversion_space((2,8)))

        #set foursquares space if enabled
        if self.flags.foursquares:
            #foursquares space at (1,1)
            pass

        #fill the rest of the board with unmarked spaces
        for j in range(9):
            for i in range(3):
                if self.board[i][j] == 0:
                    self.set_board_space(i, j, unmarked_space((i,j)))

    def construct_path(self):
        try:
            if self.flags.path_type == path_type.SIMPLE:
                path_file = open("src/simple.txt","r")
            elif self.flags.path_type == path_type.MEDIUM:
                path_file = open("src/medium.txt","r")
            elif self.flags.path_type == path_type.ADVANCED:
                path_file = open("src/advanced.txt","r")
            else:
                pass
        except Exception as e:
            logger.error("While trying to open the file for a given path type an exception of type {} has occurred".format(type(e).__name__))
            logger.error(e)
            return

        try:
            num_path_steps = int(path_file.readline())
            #iterate over the next num_path_steps lines of file, constructing light paths
            for i in range(num_path_steps):
                next_line = path_file.readline()
                start_row, start_col, next_row, next_col, color, blank_link, flipped_link = next_line.split(",")
                self.board[int(start_row)][int(start_col)].set_next_space(self.board[int(next_row)][int(next_col)], eval(color), eval(blank_link), eval(flipped_link))
        except Exception as e:
            logger.error("While trying to load a path from file an exception of type {} has occurred".format(type(e).__name__))
            logger.error(e)
            return

    def print_board(self):
        print("Current board path type is {}".format(self.flags.path_type.name))
        top_bottom_row_edge = "   -----------------       ---------"
        middle_row_edge = "   ---------------------------------"
        row_string = ""

        print(top_bottom_row_edge)
        for i in range(3):
            row_string = ""
            for j in range(9):
                current_space = self.board[i][j]
                row_string = row_string + "{}".format(current_space)

                #print the right edge of the space
                if current_space.space_type == space_type.ENTRY:
                    row_string = row_string + " "
                else:
                    row_string = row_string + "|"

            print(row_string)
            if i < 2:
                print(middle_row_edge)

        print(top_bottom_row_edge)

    def print_path(self, path_color):
        if path_color:
            print("Light paths")

            #we are on a light path; all light blank paths start at (0,5)
            blank_starting_space = self.board[0][5]
            flipped_starting_space = None
            blank_step = blank_starting_space
            path_string = ""

            #print both light paths, starting with the blank one
            try:
                while blank_step:
                    #use this same loop to find the start of the flipped path
                    if not flipped_starting_space:
                        if blank_step.light_flipped_next and not blank_step.light_blank_next:
                            #flipped_starting_space = self.board[blank_step.board_position[0]][blank_step.board_position[1]]
                            flipped_starting_space = blank_step
                        else:
                            pass
                    else:
                        pass

                    #add current space to path string
                    path_string = path_string + "{} ".format(blank_step.board_position)
                    #add an arrow if there is a next space
                    if blank_step.light_blank_next:
                        path_string = path_string + "-> "
                    else:
                        pass

                    blank_step = blank_step.light_blank_next
            except Exception as e:
                logger.error("While trying to print the board's light blank path type an exception of type {} has occurred".format(type(e).__name__))
                logger.error(e)

            print("Blank path")
            print(path_string)
            path_string = ""

            #now print the flipped path
            if not flipped_starting_space:
                flipped_starting_space = blank_starting_space
            flipped_step = flipped_starting_space

            try:
                while flipped_step:
                    #add current space to path string
                    path_string = path_string + "{} ".format(flipped_step.board_position)
                    #add an arrow if there is a next space
                    if flipped_step.light_flipped_next:
                        path_string = path_string + "-> "
                    else:
                        pass

                    flipped_step = flipped_step.light_flipped_next
            except Exception as e:
                logger.error("While trying to print the board's light flipped path type an exception of type {} has occurred".format(type(e).__name__))
                logger.error(e)

            print("Flipped Path")
            print(path_string)
            path_string = ""

        else:
            #handle dark paths
            print("Dark paths")

            #we are on a light path; all dark blank paths start at (2,5)
            blank_starting_space = self.board[2][5]
            flipped_starting_space = None
            blank_step = blank_starting_space
            path_string = ""

            #print both light paths, starting with the blank one
            try:
                while blank_step:
                    #use this same loop to find the start of the flipped path
                    if not flipped_starting_space:
                        if blank_step.dark_flipped_next and not blank_step.dark_blank_next:
                            flipped_starting_space = blank_step
                        else:
                            pass
                    else:
                        pass

                    #add current space to path string
                    path_string = path_string + "{} ".format(blank_step.board_position)
                    #add an arrow if there is a next space
                    if blank_step.dark_blank_next:
                        path_string = path_string + "-> "
                    else:
                        pass

                    blank_step = blank_step.dark_blank_next
            except Exception as e:
                logger.error("While trying to print the board's dark blank path type an exception of type {} has occurred".format(type(e).__name__))
                logger.error(e)

            print("Blank path")
            print(path_string)
            path_string = ""

            #now print the flipped path
            if not flipped_starting_space:
                flipped_starting_space = blank_starting_space
            flipped_step = flipped_starting_space

            try:
                while flipped_step:
                    #add current space to path string
                    path_string = path_string + "{} ".format(flipped_step.board_position)
                    #add an arrow if there is a next space
                    if flipped_step.dark_flipped_next:
                        path_string = path_string + "-> "
                    else:
                        pass

                    flipped_step = flipped_step.dark_flipped_next
            except Exception as e:
                logger.error("While trying to print the board's dark flipped path type an exception of type {} has occurred".format(type(e).__name__))
                logger.error(e)

            print("Flipped Path")
            print(path_string)
            path_string = ""
