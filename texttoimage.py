import os
import sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

if sys.platform[0] == 'l':
    path = '/home/jan/git/NCalIcons'
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/NCalIcons"
os.chdir(path)

fontsize = 75
fontcolor = (200, 200, 200) 
 
# Open an Image
img = Image.open('Icons/Ent1.png')
 
# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

if sys.platform[0] == 'l': 
    myFont = ImageFont.truetype('C:/Fonts/Arial.ttf', fontsize)
if sys.platform[0] == 'w':
    myFont = ImageFont.truetype('C:/Users/janbo/Fonts/Arial.ttf', fontsize)
 
# Add Text to an image
I1.text((60, 600), "164", font=myFont, fill = fontcolor)
 
# Save the edited image
img.save("Ent1s.png")

key = input("Wait")
