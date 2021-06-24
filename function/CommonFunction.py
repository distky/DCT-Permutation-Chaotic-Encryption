import numpy as np
import cv2
import copy
import imageio
from math import log10, sqrt
from PyQt5 import QtWidgets

def resizeImage(image, shape = (512,512)):
   return cv2.resize(image, shape)

def bgr2gray(image):
    if len(image.shape) == 2:
        return image
    image32 = np.float32(image)
    return cv2.cvtColor(image32, cv2.COLOR_BGR2GRAY)

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

def saveImageAs(image, filename = 'result', fileext = '.jpeg'):
    imageRgb = np.zeros((image.shape[0], image.shape[1], 3))
    imageRgb[...,0] = copy.deepcopy(image)
    imageRgb[...,1] = copy.deepcopy(image)
    imageRgb[...,2] = copy.deepcopy(image)

    file = filename + fileext

    imageio.imwrite(file, imageRgb)
    return file

def deepCopy(obj):
    return copy.deepcopy(obj)

def saveDcMatrix(dcMatrix):
    np.save('dcmatrix.npy', dcMatrix)

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