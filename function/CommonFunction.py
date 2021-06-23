import numpy as np
import cv2
import copy

def resizeImage(image, shape = (512,512)):
   return cv2.resize(image, shape)

def bgr2gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def convertImageToSubBlock(coverImage, shape):
    tiles = [coverImage[x:x+shape,y:y+shape] for x in range(0,coverImage.shape[0],shape) for y in range(0,coverImage.shape[1],shape)]
    return tiles

def convertSubBlockToImage(subBlock, shape):
    images = np.zeros((512,512), dtype='float32')
    count = 0
    for i in range(0,images.shape[0], shape):
        for j in range(0, images.shape[1], shape):
            images[i:i+shape, j:j+shape] = subBlock[count]
            count +=1
    return images

def saveImageAsTiff(image, filename = 'result'):
    filename = filename + ".tiff"
    cv2.imwrite(filename, image)
    return filename

def saveImageAsJpeg(image, filename = 'result'):
    filename = filename + ".jpeg"
    cv2.imwrite(filename, image)
    return filename

def deepCopy(obj):
    return copy.deepcopy(obj)

def saveDcMatrixAndFloatingPoint(npArray, dcMatrix):
    intNpArray = deepCopy(npArray).astype('uint8')

    objectArr = np.ndarray(2, dtype=object)
    objectArr[0] = dcMatrix
    objectArr[1] = npArray - intNpArray

    np.save('dcmatrix.npy', objectArr)

def loadDcMatrixAndFloatingPoint(npyFile):
    return np.load(npyFile, allow_pickle=True)