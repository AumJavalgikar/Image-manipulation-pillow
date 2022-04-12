from PIL import Image
from PIL import ImageColor

imOb = Image.new('RGBA', (100, 100))
imOb.getpixel((0, 0))
for x in range(100):
    for y in range(50):
        imOb.putpixel((x, y), (210, 210, 210))

for x in range(100):
    for y in range(50, 100):
        imOb.putpixel((x,y), ImageColor.getcolor('darkgrey', 'RGBA'))

imOb.save('images/putpixel.png')
