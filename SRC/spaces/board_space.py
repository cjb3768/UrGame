import logging
import enum


class space_type(Enum):
    ENTRY = 0
    EXIT = 1
    UNMARKED = 2
    ROSETTE = 3
    FOUREYES = 4
    PASSAGE = 5
    FOURSQUARES = 6
    CONVERSION = 7

class board_space:
    def __init__(self, light_space_type, dark_space_type):
        self.space_type = space_type
        self.stored_pieces = {}
        self.blank_next = None
        self.flipped_next = None
        self.board_symbol = " ";

    def set_next(self, next_space, blank_piece):
        if blank_piece:
            self.blank_next = next_space
        else:
            self.flipped_next = next_space

    def evaluate_space(self):
        pass
