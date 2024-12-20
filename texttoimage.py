from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
 
# Open an Image
img = Image.open('Ent1.png')
 
# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

# Custom font style and font size
myFont = ImageFont.truetype('FreeMono.ttf', 200)
 
# Add Text to an image
I1.text((10, 10), "Nice Car", font=myFont, fill =(255, 0, 0))
 
# Save the edited image
img.save("Ent1s.png")

key = input("Wait")
