import os
import sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def merge2(im1: Image.Image, im2: Image.Image):
    w = max(im1.size[0], im2.size[0])
    h = im1.size[1] + im2.size[1]
    im = Image.new("RGBA", (w, h))
    im.paste(im1)
    im.paste(im2, (0, im1.size[1]))
    return im
    
def merge3(im1: Image.Image, im2: Image.Image, im3: Image.Image):
    w = max(im1.size[0], im2.size[0], im3.size[0])
    h = im1.size[1] + im2.size[1] + im3.size[1]
    im = Image.new("RGBA", (w, h))
    im.paste(im1)
    im.paste(im2, (0, im1.size[1]))
    im.paste(im3, (0, im1.size[1] + im2.size[1]))
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
entindexes = [["263","225","171","266","264","265","153","176"], #1
              ["152","164","183","160","157","063","182","191"], #2
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"], #3
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"], #4
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"], #5
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"], #6
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"], #7
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"], #8
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"], #9
              ["XXX","XXX","237","208","189"]] #10
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
img = merge2(img1, img2)
I = ImageDraw.Draw(img)
posy = starty
for i in range(numrows - 1):
    posx = startx
    for j in range(numcols):
        I.text((posx, posy), entindexes[i][j], font = myFont, fill = fontcolor)
        posx = posx + deltax           
    posy = posy + deltay
    posx = startx
for j in range(5):
    I.text((posx, posy), entindexes[9][j], font = myFont, fill = fontcolor)
    posx = posx + deltax
img.save("Indexes/Ent.png")

numrows = 8
generalindexes = [[0 for i in range(numcols)] for j in range(numrows)]
generalindexes = [["112","001","002","140","022","020","027","062"], #1
              ["023","024","008","009","010","011","013","019"], #2
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"], #3
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"], #4
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"], #5
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"], #6
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"], #7
              ["XXX","277","278","279"]] #8
height = 1260
deltax = width / numcols
deltay = height / numrows
img1 = Image.open('Icons/General1.png')
box1 = (0, 0, 1537, 1100)
img1 = img1.crop(box1)
img2 = Image.open('Icons/General2.png')
box2 = (0, 600, 1537, 1100)
img2 = img2.crop(box2)
img = merge2(img1, img2)
I = ImageDraw.Draw(img)
posy = starty
for i in range(numrows - 1):
    posx = startx
    for j in range(numcols):
        I.text((posx, posy), generalindexes[i][j], font = myFont, fill = fontcolor)
        posx = posx + deltax           
    posy = posy + deltay
posx = startx
for j in range(4):
    I.text((posx, posy), generalindexes[7][j], font = myFont, fill = fontcolor)
    posx = posx + deltax  
img.save("Indexes/General.png")

numrows = 7
othersindexes = [[0 for i in range(numcols)] for j in range(numrows)]
othersindexes = [["214","215","216","217","218","219","220","221"], #1
              ["222","223","005","006","018","043","044","066"],  #2
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"],  #3
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"],  #4
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"],  #5
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"],  #6
              ["XXX","XXX","XXX","212","213","224"]]  #7
height = 1080
deltax = width / numcols
deltay = height / numrows
img1 = Image.open('Icons/Others1.png')
box1 = (0, 0, 1537, 1100)
img1 = img1.crop(box1)
img2 = Image.open('Icons/Others2.png')
box2 = (0, 780, 1537, 1100)
img2 = img2.crop(box2)
img = merge2(img1, img2)
I = ImageDraw.Draw(img)
posy = starty
for i in range(numrows - 1):
    posx = startx
    for j in range(numcols):
        I.text((posx, posy), othersindexes[i][j], font = myFont, fill = fontcolor)
        posx = posx + deltax           
    posy = posy + deltay
posx = startx
for j in range(6):
    I.text((posx, posy), othersindexes[6][j], font = myFont, fill = fontcolor)
    posx = posx + deltax 
img.save("Indexes/Others.png")

numrows = 11
workindexes = [[0 for i in range(numcols)] for j in range(numrows)]
workindexes = [["030","031","014","032","033","034","088","089"], #1
              ["152","XXX","XXX","XXX","XXX","XXX","XXX","XXX"],  #2
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"],  #3
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"],  #4
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"],  #5
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"],  #6
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"],  #7
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"],  #8
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"],  #9
              ["XXX","XXX","XXX","XXX","XXX","XXX","XXX","XXX"],  #10
              ["XXX","XXX","XXX","259","267","268"]]  #11
height = 1700
deltax = width / numcols
deltay = height / numrows
img1 = Image.open('Icons/Work1.png')
box1 = (0, 0, 1537, 1100)
img1 = img1.crop(box1)
img2 = Image.open('Icons/Work2.png')
box2 = (0, 360, 1537, 1100)
img2 = img2.crop(box2)
img3 = Image.open('Icons/Work3.png')
box3 = (0, 900, 1537, 1100)
img3 = img3.crop(box3)
img = merge3(img1, img2, img3)
I = ImageDraw.Draw(img)
posy = starty
for i in range(numrows - 1):
    posx = startx
    for j in range(numcols):
        I.text((posx, posy), workindexes[i][j], font = myFont, fill = fontcolor)
        posx = posx + deltax           
    posy = posy + deltay
posx = startx
for j in range(6):
    I.text((posx, posy), workindexes[10][j], font = myFont, fill = fontcolor)
    posx = posx + deltax  
img.save("Indexes/Work.png")

key = input("Wait")
