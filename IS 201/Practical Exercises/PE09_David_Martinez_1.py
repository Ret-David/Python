# David Martinez

# Follow the “multi_face.py” in the HOP09 Manipulating Images and
#     GUI Automation. In the similar way download any image of your
#     choice and create a program which displays image in the similar
#     pattern of “multi_face.png”.

from PIL import Image

img = Image.open('character.png')   # character.jpg is W:817 x H:427
width, height = img.size
resize = img.resize((int(width//3), int(height//3))) # resize to 1/3rd

# establish height/width variables
fwidth, fheight = resize.size

# create a new blank image, Image.new(_Mode, size, color)
pattern = Image.new('RGBA', (817, 427), 'black') 
# _Mode: RGBA (4x8-bit pixels, true color with transparency mask)
#  size: tuple[int(width), int(height)]
# color: When creating RGB images, you can also use color strings.

# add the resized image into the blank image
w, h = pattern.size
# step through starting at 0,0
for left in range(0, w, fwidth):            # start at point 0 (width)
    for top in range(0, h, fheight):        # start at point 0 (height)
       pattern.paste(resize, (left, top))   # paste the resized image
pattern.save('c_multi_face.png')
