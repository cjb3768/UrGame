import logging
from SRC.SPACES.board_space import *

####################
# Global variables #
####################
logger = logging.getLogger("urgame.space_type.conversion")

class conversion_space(board_space):
    def __init__(self):
        super().__init__(space_type.CONVERSION, "c")

    def test_advancement(self, piece):
        #When a conversion space is on the board, a player must land on one conversion space before advancing past a second.
        #Blank pieces are allowed to pass a conversion once, but not twice. Flipped pieces can pass unabated.
        if piece.get_state():
            #piece is blank, check to see if it can pass
            if not piece.needs_converting():
                #piece has not passed a conversion space yet; set it's must_convert flag
                piece.passed_conversion_space()
                return True
            else:
                #piece has passed a conversion space but hasn't converted; return False
                return False
        else:
            #piece is flipped, check to see if it can pass
            return True


    def test_placement(self, piece):
        #A piece can land on a conversion space if it is unoccupied (theoretically, it could land on an unflipped opposing piece, but landing on a conversion space flips one's piece, so this isn't possible.)
        if self.stored_pieces:
            #the space has a piece in it, so we can't land
            return False
        else:
            #the space is unoccupied, so obviously you can land
            return True


    def test_capture(self, piece):
        #theoretically, you could capture an unflipped opposing piece on the space, but that should never occur (landing on a conversion space flips a blank piece). We will program for this impossible possibility.
        if self.stored_pieces:
            if self.stored_pieces[0].get_color() != piece.get_color():
                if self.stored_pieces[0].get_state() != True:
                    #the piece in the space already is an opposing color and blank; return True
                    return True
                else:
                    #the piece already there is flipped; you can't cap it, flipped pieces are safe on conversion spaces
                    return False
            else:
                #the two pieces share the same color; can't capture, return false
                return False
        else:
            #there's nothing here; return false
            return False
