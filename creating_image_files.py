
from PIL import Image

newIm = Image.new('RGBA', (100, 200), 'Blue')
newIm.save('images/Blue.png')
newIm2 = Image.new('RGBA', (100, 200))
newIm2.save('images/transparentImage.png')
newIm.close()
newIm2.close()
