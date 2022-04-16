from PIL import Image

imOb = Image.open('images/wallpapers/chelsea.png')
width, height = imOb.size
# width = width - (width//6)
newimOb = imOb.resize((width, 1080))
# newimOb = newimOb.crop((10, 0, (width-10), height))
pixelColor = imOb.getpixel((10, 10))
bgIm = Image.new('RGBA', (1920, 1080), pixelColor)
bgIm.paste(newimOb, ((1920//2)-(width//2), 0))
bgIm.save('images/wallpapers/Newcheslea.png')
imOb.close()