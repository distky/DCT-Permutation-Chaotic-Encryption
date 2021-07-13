import numpy as np
import cv2
import copy
import imageio
from math import log10, sqrt
from PIL import Image, ImageQt

VALIDATION_ERROR = "VALIDATION_ERROR"
ACTION_CANCELLED = "ACTION_CANCELLED"

def resizeImage(image, shape = (512,512)):
   return cv2.resize(image, shape)

def bgr2gray(image):
    if len(image.shape) == 2:
        return image
    image32 = np.float32(image)
    return cv2.cvtColor(image32, cv2.COLOR_BGR2GRAY)

def convertImageToSubBlock(coverImage, subBlockPixel):
    tiles = [coverImage[x:x+subBlockPixel,y:y+subBlockPixel] for x in range(0,coverImage.shape[0],subBlockPixel) for y in range(0,coverImage.shape[1],subBlockPixel)]
    return tiles

def convertSubBlockToImage(subBlock, imageShape, subBlockPixel):
    images = np.zeros(imageShape, dtype='float32')
    count = 0
    for i in range(0,images.shape[0], subBlockPixel):
        for j in range(0, images.shape[1], subBlockPixel):
            images[i:i+subBlockPixel, j:j+subBlockPixel] = subBlock[count]
            count +=1
    return images

def openImageFromPath(path):
    return imageio.imread(path)

def convertImageToPixmap(img, isPath = False):
    if isPath:
        img = bgr2gray(openImageFromPath(img))

    return ImageQt.toqpixmap(Image.fromarray(img.astype('uint8')))

def saveImageAs(image, filename = 'result'):
    imageRgb = np.zeros((image.shape[0], image.shape[1], 3))
    imageRgb[...,0] = copy.deepcopy(image)
    imageRgb[...,1] = copy.deepcopy(image)
    imageRgb[...,2] = copy.deepcopy(image)

    file = filename

    imageio.imwrite(file, imageRgb)

    return convertImageToPixmap(image)

def deepCopy(obj):
    return copy.deepcopy(obj)

def saveDcMatrix(dcMatrix, filename):
    np.save(filename + '.npy', dcMatrix)

def loadDcMatrix(npyFile):
    return np.load(npyFile, allow_pickle=True)

def PSNR(img1Path, img2Path):
    mse = MSE(img1Path, img2Path)
    if(mse == 0):
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr

def MSE(img1Path, img2Path):
    img1 = bgr2gray(imageio.imread(img1Path))
    img2 = bgr2gray(imageio.imread(img2Path))

    return np.mean((img1 - img2) ** 2)

def fullStackTrace():
    import traceback, sys
    exc = sys.exc_info()[0]
    if exc is not None:
        f = sys.exc_info()[-1].tb_frame.f_back
        stack = traceback.extract_stack(f)
    else:
        stack = traceback.extract_stack()[:-1]
    trc = 'Traceback (most recent call last):\n'
    stackstr = trc + ''.join(traceback.format_list(stack))
    if exc is not None:
        stackstr += '  ' + traceback.format_exc().lstrip(trc)
    return stackstr