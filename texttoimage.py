import os
import sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def merge(im1: Image.Image, im2: Image.Image):
    w = max(im1.size[0], im2.size[0])
    h = im1.size[1] + im2.size[1]
    im = Image.new("RGBA", (w, h))
    im.paste(im1)
    im.paste(im2, (0, im1.size[1]))
    return im
    
if sys.platform[0] == 'l':
    path = '/home/jan/git/NCalIcons'
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/NCalIcons"
os.chdir(path)
numcols = 8
numrows = 10
entindexes = [[0 for i in range(numcols)] for j in range(numrows)]
entindexes = [["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"]]

fontsize = 60
fontcolor = (200, 200, 200)
startx = 75
starty = 350
width = 1400
height = 1536
deltax = width / numcols
deltay = height / numrows
 
img1 = Image.open('Icons/Ent1.png')
box1 = (0, 0, 1537, 1100)
img1 = img1.crop(box1)
img2 = Image.open('Icons/Ent2.png')
box2 = (0, 320, 1537, 1100)
img2 = img2.crop(box2)

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
