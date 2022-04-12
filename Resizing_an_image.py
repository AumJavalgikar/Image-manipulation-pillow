from PIL import Image

imOb = Image.open('images/zophie.png')
width, height = imOb.size
ResizedOb = imOb.resize((int(width/2), int(height/2)))
ResizedOb.save('images/resized.png')
svelteIm = imOb.resize((int(width), int(height) + 300))
svelteIm.save('images/svelte.png')
imOb.close()