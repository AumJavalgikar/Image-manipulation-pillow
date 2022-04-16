from PIL import Image

catImageObj = Image.open('images/heisenberg.jpg')
imagewidth, imageheight = catImageObj.size
imageFormat = catImageObj.format
imageFormatDesc = catImageObj.format_description
catImageObj.save('images/heisenberg.png')
catImageObj.close()