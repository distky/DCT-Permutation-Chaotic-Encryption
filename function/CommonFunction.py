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
    elif img is None:
        return None

    return ImageQt.toqpixmap(Image.fromarray(rounding(img,0).astype('uint8')))

def saveImageAs(image, filename = 'result'):
    cv2.imwrite(filename, image)

def deepCopy(obj):
    return copy.deepcopy(obj)

def saveDcMatrix(numpyObject, filename):
    np.save(filename + '.npy', numpyObject)

def loadDcMatrix(npyFile):
    return np.load(npyFile, allow_pickle=True)

def PSNR(img1, img2):
    mse = MSE(img1, img2)
    if(mse == 0):
        return 100
    max_pixel = 255.0
    psnr = 20 * math.log10(max_pixel / math.sqrt(mse))
    return psnr

def MSE(img1, img2):
    return np.mean((img1 - img2) ** 2)

def NCC(img1, img2):
    psnr = PSNR(img1, img2)

    if(psnr == 100):
        return 1.0

    return cv2.matchTemplate(img1.astype('float32'), img2.astype('float32'), cv2.TM_CCOEFF_NORMED)[0][0]

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

def validCriteria(isCompare):
    if isCompare:
        return 'Periksa kembali apakah input telah memenuhi kriteria berikut ini:\n1. Pastikan path file pertama dan kedua valid\n2. Pastikan ukuran gambar yang dibandingkan sesuai'
    else:
        return 'Periksa kembali apakah input telah memenuhi kriteria berikut ini:\n1. Pastikan path file pertama dan kedua valid\n2. Pastikan ukuran citra pesan NxN dimana N lebih besar sama dengan 32 dan N lebih kecil sama dengan 64 dan N merupakan kelipatan dari 8\n3. Pastikan ukuran citra sampul merupakan 16 kali dari ukuran citra pesan\n4. Pastikan nilai kunci X0 dan Y0 lebih besar dari 0'

def validateCrypto(file, x0, y0):
    if isinstance(file, str) and file:
        file = bgr2gray(openImageFromPath(file))
    elif isinstance(file, str) and file == '':
        raise IOError(VALIDATION_ERROR)

    height, width = file.shape

    if x0 == 0.0:
        raise IOError(VALIDATION_ERROR)
    if y0 == 0.0:
        raise IOError(VALIDATION_ERROR)

    if height != width:
        raise IOError(VALIDATION_ERROR)
    elif height < 32 or height > 64:
        raise IOError(VALIDATION_ERROR)
    elif height % 8 != 0:
        raise IOError(VALIDATION_ERROR)
    
    return file, x0, y0

def validateStegano(imgPath, message):
    if imgPath == '':
        raise IOError(VALIDATION_ERROR)
    
    img = bgr2gray(openImageFromPath(imgPath))

    height, width = img.shape

    if isinstance(message, str):
        message = loadDcMatrix(message)
    
    mHeight, mWidth = message.shape

    if mHeight*16 != height or mWidth*16 != width:
        raise IOError(VALIDATION_ERROR)
    elif mHeight != mWidth:
        raise IOError(VALIDATION_ERROR)
    
    return img, message


def validate(filePath1, filePath2):
    if filePath1 == '' or filePath2 == '':
        raise IOError(VALIDATION_ERROR)

    file1 = bgr2gray(openImageFromPath(filePath1))

    height, width = file1.shape
    
    file2 = bgr2gray(openImageFromPath(filePath2))

    height2, width2 = file2.shape

    if height != height2:
        raise IOError(VALIDATION_ERROR)
    elif width != width2:
        raise IOError(VALIDATION_ERROR)
    
    return file1, file2