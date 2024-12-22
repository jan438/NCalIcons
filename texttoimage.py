import os
import sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def merge(im1: Image.Image, im2: Image.Image):
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h))
    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))
    return im
    
if sys.platform[0] == 'l':
    path = '/home/jan/git/NCalIcons'
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/NCalIcons"
os.chdir(path)
numcols = 8
numrows = 9
entindexes = [[0 for i in range(numcols)] for j in range(numrows)]
entindexes = [["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"]]

fontsize = 75
fontcolor = (200, 200, 200)
startx = 0
starty = 0
width = 1537
height = 1536
deltax = width / 8
deltay = height / 8
 
img1 = Image.open('Icons/Ent1.png')
img2 = Image.open('Icons/Ent2.png')

img = merge(img1, img2)
 
I = ImageDraw.Draw(img)

if sys.platform[0] == 'l': 
    myFont = ImageFont.truetype('/home/jan/Fonts/Arial.ttf', fontsize)
if sys.platform[0] == 'w':
    myFont = ImageFont.truetype('C:/Users/janbo/Fonts/Arial.ttf', fontsize)

posy = starty
for i in range(numrows):
    posx = startx
    for j in range(numcols):
        I.text((posx, posy), entindexes[i][j], font = myFont, fill = fontcolor)
        posx = posx + deltax           
    posy = posy + deltay
 
img.save("Indexes/Ent.png")

key = input("Wait")
