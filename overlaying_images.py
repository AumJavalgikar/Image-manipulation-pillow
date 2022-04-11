from PIL import Image

catIm = Image.open('images/zophie.png')
catImCopy = catIm.copy()

# .crop() RETURNS AN OBJECT
faceIm = catImCopy.crop((335, 345, 565, 560))

# .paste() MODIFIES THE OBJECT IN PLACE
catImCopy.paste(faceIm, (0, 0))
catImCopy.paste(faceIm, (400, 500))

catImCopy.save('images/pasted.png')
catIm.close()