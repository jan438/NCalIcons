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

fontsize = 60
fontcolor = (0, 0, 0)
startx = 100
starty = 300
numcols = 8
if sys.platform[0] == 'l':
    path = '/home/jan/git/NCalIcons'
    myFont = ImageFont.truetype('/home/jan/Fonts/Arial.ttf', fontsize)
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/NCalIcons"
    myFont = ImageFont.truetype('C:/Users/janbo/Fonts/Arial.ttf', fontsize)
os.chdir(path)
numrows = 10
entindexes = [[0 for i in range(numcols)] for j in range(numrows)]
entindexes = [["263","225","264","264","264","265","164","176"],
              ["152","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"]]
generalindexes = [[0 for i in range(numcols)] for j in range(numrows)]
generalindexes = [["263","225","264","264","264","265","164","176"],
              ["152","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"],
              ["164","164","164","164","164","164","164","164"]]
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
posy = starty
for i in range(numrows):
    posx = startx
    for j in range(numcols):
        I.text((posx, posy), entindexes[i][j], font = myFont, fill = fontcolor)
        posx = posx + deltax           
    posy = posy + deltay
img.save("Indexes/Ent.png")

width = 1400
height = 1536
deltax = width / numcols
deltay = height / numrows
img1 = Image.open('Icons/General1.png')
box1 = (0, 0, 1537, 1100)
img1 = img1.crop(box1)
img2 = Image.open('Icons/General2.png')
box2 = (0, 320, 1537, 1100)
img2 = img2.crop(box2)
img = merge(img1, img2)
I = ImageDraw.Draw(img)
posy = starty
for i in range(numrows):
    posx = startx
    for j in range(numcols):
        I.text((posx, posy), generalindexes[i][j], font = myFont, fill = fontcolor)
        posx = posx + deltax           
    posy = posy + deltay
img.save("Indexes/General.png")

key = input("Wait")
