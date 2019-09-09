import logging
import board_space

####################
# Global variables #
####################
logger = logging.getLogger("urgame.space_type.unmarked")

class unmarked_space(board_space):
    def __init__(self):
        super().__init__(self, space_type.UNMARKED, "u")

    def set_next(self, next_space, piece):
        super().set_next(self, next_space, piece)

    def traverse_next(self, piece):
        super().traverse_next(self, piece)

    def place_piece(self, piece):
        #for unmarked spaces, a piece can move there if there is not a like colored piece in the way; additionally, if there is an enemy piece, that piece is removed
        if not self.stored_pieces:
            #there are no pieces in the spot; we can place the piece
            self.stored_pieces.append(piece)
            return true
        else:
            #there should only ever be one piece in an unmarked space; let's check it's color
            if self.stored_pieces[0].get_color == piece.get_color:
                #the two pieces match colors; we can't place here.
                return false
            else:
                #the two pieces are different colors; remove the other piece and place yours
                self.stored_pieces[0] = piece
                return true
