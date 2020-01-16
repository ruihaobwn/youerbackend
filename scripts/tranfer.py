from PIL import Image
import os
import glob


def convertjpg(jpgfile, savedir, width=500, height=400):
    img = Image.open(jpgfile)
    (x, y) = img.size
    y_s = 720
    x_s = x * y_s / y
    new_img = img.resize((int(x_s), int(y_s)), Image.BILINEAR)
    new_img.save(os.path.join(savedir, os.path.basename(jpgfile)))


def modifyjpgSize(file, saveDir):
    for jpgfile in glob.glob(file):
        convertjpg(jpgfile, saveDir)


file = r'E:\youershuo\jpg\*.jpg'
saveDir = r'E:\youershuo\outImage'
modifyjpgSize(file, saveDir)
