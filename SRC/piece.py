import logging

####################
# Global variables #
####################
logger = logging.getLogger("urgame.piece_type")

class piece_type:
    def __init__(self, is_light, is_blank, board_pos):
        try:
            self.color = is_light
            self.state = is_blank
            self.must_convert = False
            self.row = board_pos[0] #this will let pieces know where they are
            self.column = board_pos[1]
        except Exception as e:
            logger.error("While trying to create a piece an exception of type {} has occurred".format(type(e).__name__))
            logger.error(e)

    def get_color(self):
        return self.color #returns true if this is a light piece and false if this is a dark piece

    def get_state(self):
        return self.state #returns true if blank, false if flipped

    def change_state(self):
        #flip the piece
        self.state = not self.state

    def update_position(self, new_pos):
        try:
            self.row = new_pos[0]
            self.col = new_pos[1]
        except Exception as e:
            logger.error("While trying to update a piece's position an exception of type {} has occurred".format(type(e).__name__))
            logger.error(e)

    def needs_converting(self):
        return self.must_convert #a piece must convert if it has passed, but has not landed on, a conversion space, and attempts to pass another

    def passed_conversion_space(self):
        self.must_convert = True

    def __str__(self):
        #return a symbol based on the color and state of the piece
        if self.get_color():
            if self.get_state():
                return "l"
            else:
                return "L"
        else:
            if self.get_state():
                return "d"
            else:
                return "D"
