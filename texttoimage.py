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
startx = 0
starty = 0
width = 1537
height = 1536
deltax = width / 8
deltay = height / 8
 
img = Image.open('Icons/Ent1.png')
 
I1 = ImageDraw.Draw(img)

if sys.platform[0] == 'l': 
    myFont = ImageFont.truetype('C:/Fonts/Arial.ttf', fontsize)
if sys.platform[0] == 'w':
    myFont = ImageFont.truetype('C:/Users/janbo/Fonts/Arial.ttf', fontsize)
 
I1.text((startx + deltax, starty + deltay), "164", font=myFont, fill = fontcolor)
I1.text((startx + 2 * deltax, starty + deltay), "164", font=myFont, fill = fontcolor)
I1.text((startx + deltax, starty + 2 * deltay), "164", font=myFont, fill = fontcolor)
 
img.save("Indexes/Ent1s.png")

key = input("Wait")
