# David Martinez

# Follow the “eyes_cropped.py” in the HOP09 Manipulating Images
#     and GUI Automation. In the similar way use the image which
#     was used in the previous question and create a program which
#     displays image in the similar pattern of “eyes_cropped.png”
#     and “four_eyes_bulldog.png”.

from PIL import Image

# character.jpg is W:817 x H:427, save as png
img = Image.open('character.jpg')
img.save('character.png')

# open character.png for cropping
img = Image.open('character.png')
cropped = img.crop((0,162,817,215)) # crop the eyes
cropped.save('c_eyes_cropped.png')  # save the crop
copy_img = img.copy()               # make a copy of character.png
copy_img.paste(cropped, (0,0))      # paste crop at (0,0) on image copy
copy_img.save('c_four_eyes.png')    # save pasted crop
