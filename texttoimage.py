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
 
# Open an Image
img = Image.open('Icons/Ent1.png')
 
# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

if sys.platform[0] == 'l': 
    myFont = ImageFont.truetype('C:/Fonts/Arial.ttf', 200)
if sys.platform[0] == 'w':
    myFont = ImageFont.truetyoe('C:/Users/janbo/Fonts/Arial.ttf', 200)
 
# Add Text to an image
I1.text((10, 10), "Nice Car", font=myFont, fill =(255, 0, 0))
 
# Save the edited image
img.save("Ent1s.png")

key = input("Wait")
