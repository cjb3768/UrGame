import logging
import sys
import SRC

####################
# Global variables #
####################
logger = logging.getLogger("urgame")

####################
#    Functions     #
####################

def main():
    #set logging level to output all messages of DEBUG level or higher
    logging.basicConfig(level=logging.DEBUG)

    #print hello world
    logger.debug("Hello world")


if __name__ == "__main__":
    main()
