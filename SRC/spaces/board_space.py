import logging
from enum import Enum, unique, auto

####################
# Global variables #
####################
logger = logging.getLogger("urgame.space_type")

@unique
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
        self.must_convert = False

    def get_color(self):
        return color #returns true if this is a light piece and false if this is a dark piece

    def get_state(self):
        return state #returns true if blank, false if flipped

    def change_state(self):
        #flip the piece
        self.state = not self.state

    def needs_converting(self):
        return self.must_convert #a piece must convert if it has passed, but has not landed on, a conversion space, and attempts to pass another

    def passed_conversion_space(self):
        self.must_convert = True


class board_space:
    def __init__(self, space_type, board_symbol, board_position):
        self.space_type = space_type
        self.stored_pieces = {}
        self.dark_blank_next = None
        self.light_blank_next = None
        self.dark_flipped_next = None
        self.light_flipped_next = None
        self.board_symbol = board_symbol
        self.board_position = board_position

    def set_next_space(self, next_space, path_color, blank_state, flipped_state):
        """Set the next space in the given path, based on the color and state of the piece"""
        try:
            #construct light path
            if path_color:
                if blank_state:
                    self.light_blank_next = next_space
                else:
                    pass

                if flipped_state:
                    self.light_flipped_next = next_space
                else:
                    pass
            #construct dark path
            else:
                if blank_state:
                    self.dark_blank_next = next_space
                else:
                    pass

                if flipped_state:
                    self.dark_flipped_next = next_space
                else:
                    pass
            return True
        except Exception as e:
            logger.error("While trying to construct the path, an exception of type {} has occurred".format(type(e).__name__))
            logger.error(e)
            return False

    def get_next_space(self, piece):
        """Get the next space in the given path, based on the color and state of the piece"""
        try:
            #traverse light path
            if piece.get_color():
                if piece.get_state():
                    return self.light_blank_next
                else:
                    return self.light_flipped_next
            #traverse dark path
            else:
                if piece.get_state():
                    return self.dark_blank_next
                else:
                    return self.dark_flipped_next
        except Exception as e:
            logger.error("While trying to traverse the path, an exception of type {} has occurred".format(type(e).__name__))
            logger.error(e)
            return false

    def test_advancement(self, piece):
        """Verify whether or not a piece can advance beyond this space."""
        #for default spaces, there is no limitation preventing a piece from passing the space; return true
        return True

    def test_placement(self, piece):
        """Verify whether or not a piece can be placed in the space."""
        #for default spaces, a piece can move there if there is not a like colored piece in the way; additionally, if there is an enemy piece, that piece is removed
        if not self.stored_pieces:
            #there are no pieces in the spot; we can place the piece
            return True
        else:
            #there should only ever be one piece in a default space; return false if its the same color as piece (can't land there), and true if it isn't (can capture opponent)
            return self.stored_pieces[0].get_color() != piece.get_color()

    def test_capture(self, piece):
        """Verify if a capture is possible in the space."""
        #for default spaces, one may capture an opposing piece if it occupies the space where one lands.
        if not self.stored_pieces:
            #there are no pieces in the spot; we can't capture here
            return False
        else:
            #there is a piece in the space; return false if it is the same color as piece (can't capture own piece), and true if it is not (can capture)
            return self.stored_pieces[0].get_color() != piece.get_color()


    # def place_piece(self, piece):
    #     """Place a piece in the space as part of a move"""
    #     self.stored_pieces.append(piece)

    # def remove_piece(self, piece):
    #     """Remove a piece from the space as part of a move"""
    #     #check to see if a matching piece exists in the space and then remove it
    #     try:
    #         self.stored_pieces.remove(piece)
    #         return true
    #     except Exception as e:
    #         logger.error("While attempting to remove a piece, an exception of type {} has occurred".format(type(e).__name__))
    #         return false

    # def capture_opposite_piece(self,piece):
    #     """Remove an opposing piece from the space as part of a move"""
    #     #remove a piece of the opposite color of the current piece if one exists
    #     try:
    #         for stored in self.stored_pieces:
    #             if store.get_color() != piece.get_color():
    #                 self.stored_pieces.remove(stored)
    #                 break
    #         return true
    #     except Exception as e:
    #         logger.error("While attempting to remove an opposing piece, an exception of type {} has occurred".format(type(e).__name__))
    #         return false
