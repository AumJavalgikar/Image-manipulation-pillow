from PIL import Image

imOb = Image.open('images/wallpaper4.png')
width, height = imOb.size
width = width - (width//10)
newimOb = imOb.resize((width, 1080))
bgimage = Image.open('images/bgimage.png')
bgimage.paste(newimOb, (((1920//2)-(width//2)), 0))
bgimage.save('images/newfinalwallpaper.png')
imOb.close()
bgimage.close()
