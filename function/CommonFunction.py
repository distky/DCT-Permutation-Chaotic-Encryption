import numpy as np
import cv2
import copy
import math
from PIL import Image, ImageQt

VALIDATION_ERROR = "VALIDATION_ERROR"
ACTION_CANCELLED = "ACTION_CANCELLED"

def resizeImage(image, shape = (512,512)):
   return cv2.resize(image, shape)

def bgr2gray(image):
    if len(image.shape) == 2:
        return image
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def rounding(npElement, dec):
    return np.round(npElement, dec)

def convertImageToSubBlock(coverImage, subBlockPixel):
    tiles = [coverImage[x:x+subBlockPixel,y:y+subBlockPixel] for x in range(0,coverImage.shape[0],subBlockPixel) for y in range(0,coverImage.shape[1],subBlockPixel)]
    return tiles

def convertSubBlockToImage(subBlock, imageShape, subBlockPixel):
    images = np.zeros(imageShape)
    count = 0
    for i in range(0,images.shape[0], subBlockPixel):
        for j in range(0, images.shape[1], subBlockPixel):
            images[i:i+subBlockPixel, j:j+subBlockPixel] = subBlock[count]
            count +=1
    return images

def openImageFromPath(path):
    return cv2.imread(path, cv2.IMREAD_ANYDEPTH)

def convertImageToPixmap(img, isPath = False):
    if isPath:
        img = bgr2gray(openImageFromPath(img))

    return ImageQt.toqpixmap(Image.fromarray(rounding(img,0).astype('uint8')))

def saveImageAs(image, filename = 'result'):
    cv2.imwrite(filename, image)

def deepCopy(obj):
    return copy.deepcopy(obj)

def saveDcMatrix(numpyObject, filename):
    np.save(filename + '.npy', np.array(numpyObject, dtype='object'))

def loadDcMatrix(npyFile):
    return np.load(npyFile, allow_pickle=True)

def PSNR(img1Path, img2Path):
    mse = MSE(img1Path, img2Path)
    if(mse == 0):
        return 100
    max_pixel = 255.0
    psnr = 20 * math.log10(max_pixel / math.sqrt(mse))
    return psnr

def MSE(img1Path, img2Path):
    return np.mean((bgr2gray(openImageFromPath(img1Path)) - bgr2gray(openImageFromPath(img2Path))) ** 2)

def NCC(img1Path, img2Path):
    psnr = PSNR(img1Path, img2Path)

    if(psnr == 100):
        return 1.0

    img1 = bgr2gray(openImageFromPath(img1Path)).astype('float32')
    img2 = bgr2gray(openImageFromPath(img2Path)).astype('float32')

    return cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)[0][0]

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

def validCriteria():
    return 'Periksa kembali apakah gambar telah diinput dan memenuhi kriteria:\n1. Pastikan path file pertama dan kedua valid\n2.Pastikan ukuran pesan merupakan kelipatan dari 8 dan memiliki width dan height yang sama\n3. Pastikan ukuran citra sampul merupakan 16 kali dari ukuran citra pesan\n4. Pastikan ukuran citra pesan NxN dimana N lebih besar sama dengan 32 dan N lebih kecil sama dengan 64'

def validate(filePath1, filePath2, x0 = 0, y0 = 0):
    if filePath1 == '' or filePath2 == '':
        raise IOError(VALIDATION_ERROR)

    file1 = bgr2gray(openImageFromPath(filePath1))

    height, width = file1.shape
    
    filePath2Split = filePath2.split('.')

    if filePath2Split[-1] != 'npy':
        file2 = bgr2gray(openImageFromPath(filePath2))
    else:
        file2, x0, y0 = loadDcMatrix(filePath2)

    height2, width2 = file2.shape

    if height2 != width2:
        raise IOError(VALIDATION_ERROR)
    elif height2 * 16 != height or width2 * 16 != width:
        raise IOError(VALIDATION_ERROR)
    elif height2 % 8 != 0:
        raise IOError(VALIDATION_ERROR)
    elif height2 < 32 and height2 > 64:
        raise IOError(VALIDATION_ERROR)
    
    if x0 == 0.0:
        raise IOError(VALIDATION_ERROR)
    elif y0 == 0.0:
        raise IOError(VALIDATION_ERROR)
    
    return file1, file2, x0, y0