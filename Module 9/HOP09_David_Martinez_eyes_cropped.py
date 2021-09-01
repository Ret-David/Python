# David Martinez

from PIL import Image

# Example: 10x10 pixel grid, top left (0,0), bottom right (9,9)
# Across the top 0-9, down the side 0-9
# Crop area is a tuple (top,left,top,right), example: (3,1,9,6)

img = Image.open('bulldog2.png')
# eyes captured from these pixels
cropped = img.crop((0,150,590,235)) # position of the eyes
cropped.save('eyes_cropped.png')
# paste eye cropped into the bulldog2.png
copy_img = img.copy()
copy_img.paste(cropped, (0,0)) # paste it at 0,0 or top left
copy_img.save('four_eyes_bulldog.png')
