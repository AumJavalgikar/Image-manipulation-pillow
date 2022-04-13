import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILE_NAME = 'catlogo.png'

logoIm = Image.open('images/catlogo.png')
logoIm = logoIm.resize((50, 50))
logoWidth, logoHeight = logoIm.size

for filename in os.listdir('images'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILE_NAME:
        continue
    im = Image.open(f'images/{filename}')
    width, height = im.size
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        print(f'Resizing image {filename}  to {width},{height}')
        im = im.resize((width, height))

    print(f'pasting logo in {filename}')
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    im.save(f'images/with_logo_{filename}')

print('finished')
