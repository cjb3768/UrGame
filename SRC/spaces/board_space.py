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
    NULLSPACE = 8

class piece_type:
    def __init__(self, is_light, is_blank):
        self.color = is_light
        self.state = is_blank

    def get_color(self):
        return color #returns true if this is a light piece and false if this is a dark piece

    def get_state(self):
        return state #returns true if blank, false if flipped

    def change_state(self):
        self.state = false

class board_space:
    def __init__(self, space_type, board_symbol):
        self.space_type = space_type
        self.stored_pieces = {}
        self.blank_next = None
        self.flipped_next = None
        self.board_symbol = board_symbol;

    def set_next_space(self, next_space, blank_state):
        """Set the next space in the given path, based on the state of the piece"""
        try:
            if blank_state:
                self.blank_next = next_space
            else:
                self.flipped_next = next_space
        except Exception as e:
            logger.error("While trying to construct the board, an exception of type {} has occurred".format(type(e).__name__))
            logger.error(e)

    def get_next_space(self, piece):
        """Get the next space in the given path, based on the state of the piece"""
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
        """Place a piece in the space as part of a move"""
        self.stored_pieces.append(piece)

    def check_if_placeable(self, piece):
        """Verify whether or not a piece can be placed in the space."""
        #for default spaces, a piece can move there if there is not a like colored piece in the way; additionally, if there is an enemy piece, that piece is removed
        if not self.stored_pieces:
            #there are no pieces in the spot; we can place the piece
            return true
        else:
            #there should only ever be one piece in an unmarked space; let's check it's color
            if self.stored_pieces[0].get_color() == piece.get_color():
                #the two pieces match colors; we can't place here.
                return false
            else:
                #the two pieces are different colors; remove the other piece and place yours
                return true

    def remove_piece(self, piece):
        """Remove a piece from the space as part of a move"""
        #check to see if a matching piece exists in the space and then remove it
        try:
            self.stored_pieces.remove(piece)
            return true
        except Exception as e:
            logger.error("While attempting to remove a piece, an exception of type {} has occurred".format(type(e).__name__))
            return false

    def capture_opposite_piece(self,piece):
        """Remove an opposing piece from the space as part of a move"""
        #remove a piece of the opposite color of the current piece if one exists
        try:
            for stored in self.stored_pieces:
                if store.get_color() != piece.get_color():
                    self.stored_pieces.remove(stored)
                    break
            return true
        except Exception as e:
            logger.error("While attempting to remove an opposing piece, an exception of type {} has occurred".format(type(e).__name__))
            return false
