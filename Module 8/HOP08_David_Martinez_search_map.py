# David Martinez

import webbrowser
import sys

place = ''
if len(sys.argv)>1:
    # Get address from the command line
    place = ''.join(sys.argv[1:])   # use '+' for addresses

webbrowser.open("https://google.com/maps/search/"+place)
