from PIL import Image

imObj = Image.open('images/zophie.png')
croppedIm = imObj.crop((335, 345, 565, 560))
croppedIm.save('images/cropped_zophie.png')
