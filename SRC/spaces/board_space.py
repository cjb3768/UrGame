import logging
import enum

####################
# Global variables #
####################
logger = logging.getLogger("urgame.space_type")

class space_type(Enum):
    ENTRY = 0
    EXIT = 1
    UNMARKED = 2
    ROSETTE = 3
    FOUREYES = 4
    PASSAGE = 5
    FOURSQUARES = 6
    CONVERSION = 7

class piece_type:
    def __init__(self, is_light, is_blank):
        self.color = is_light
        self.state = is_blank

    def get_color(self):
        return color #returns true if this is a light piece and false if this is a dark piece

    def get_state(self):
        return state #returns true if blank, false if flipped

    def change_state(self)
        self.state = false

class board_space:
    def __init__(self, space_type, board_symbol):
        self.space_type = space_type
        self.stored_pieces = {}
        self.blank_next = None
        self.flipped_next = None
        self.board_symbol = board_symbol;

    def set_next(self, next_space, piece):
        try:
            if piece.get_state():
                self.blank_next = next_space
            else:
                self.flipped_next = next_space
        except Exception as e:
            logger.error("While trying to construct the board, an exception of type {} has occurred".format(type(e).__name__))
            logger.error(e)

    def traverse_next(self, piece):
        """Attempt to move to the next part of the board. Special space-specific rules may prevent this. Return the next board_space if possible, false if not."""
        try:
            if piece.get_state():
                return self.blank_next
            else:
                return self.flipped_next
        except Exception as e:
            logger.error("While trying to traverse the board, an exception of type {} has occurred".format(type(e).__name__))
            logger.error(e)
            return false

    def place_piece(self, piece):
        pass
