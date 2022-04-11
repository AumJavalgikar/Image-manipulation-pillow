from PIL import Image

ImObj = Image.open('images/zophie.png')
ImObjCopy = ImObj.copy()
FaceIm = ImObjCopy.crop((335, 345, 565, 560))
FaceImWidth, FaceImHeight = FaceIm.size
CatImWidth, CatImHeight = ImObj.size
ImObjCopy2 = ImObj.copy()
for left in range(0, CatImWidth, FaceImWidth):
        for top in range(0, CatImHeight, FaceImHeight):
            print(left, top)
            ImObjCopy2.paste(FaceIm, (left, top))
ImObjCopy2.save('images/tiled_zophie.png')
