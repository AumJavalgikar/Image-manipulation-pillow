from PIL import Image

imOb = Image.open('images/zophie.png')
imOb.rotate(90).save('images/rotated_1.png')
imOb.rotate(180).save('images/rotated_2.png')
imOb.rotate(270).save('images/rotated_3.png')
imOb.transpose(Image.FLIP_LEFT_RIGHT).save('images/flipped_left.png')
imOb.transpose(Image.FLIP_TOP_BOTTOM).save('images/flipped_top.png')

