from PIL import Image

catImageObj = Image.open('images/zophie.png')
imagewidth, imageheight = catImageObj.size
imageFormat = catImageObj.format
imageFormatDesc = catImageObj.format_description
catImageObj.save('images/zophie.jpg')
catImageObj.close()