# David Martinez

import pyautogui

print('Press control + C to terminate.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x) + ' Y: ' + str(y)
        print(positionStr,end='\r')
except KeyboardInterrupt:
    print('\nDone')


   # 0,0      X increases -->
    # +---------------------------+
    # |                           | Y increases
    # |                           |     |
    # |    1920 x 1080 screen     |     |
    # |                           |     V
    # |                           |
    # |                           |
    # +---------------------------+ 1919, 1079
