import numpy as np
import cv2
from function.CommonFunction import openImageFromPath, saveImageAs, bgr2gray

def sp_noise(image, prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    black = 0
    white = 255            
    probs = np.random.random(image.shape[:2])
    image[probs < (prob / 2)] = black
    image[probs > 1 - (prob / 2)] = white
    return image


def convertImageToBlackAndWhite():
    citraSampul = openImageFromPath('F:/Pictures/Testing/lena 512 x 512.tiff')
    
    citraSampul = bgr2gray(citraSampul)

    thresh = 127
    citraSampul = cv2.threshold(citraSampul, thresh, 255, cv2.THRESH_BINARY)[1]
    saveImageAs(citraSampul.astype('uint8'), 'F:/Pictures/Testing/lena 512 x 512 bnw.tiff')

def randomNumber():
    import random 
    print(random.uniform(0, 1))
    print(random.uniform(0, 1))

def template_matching(path1, path2):
    citra1 = bgr2gray(openImageFromPath(path1))
    citra2 = bgr2gray(openImageFromPath(path2))
    result = cv2.matchTemplate(citra1, citra2, cv2.TM_CCOEFF_NORMED)
    print(result[0][0])

def equalizeHistogram(path1, intensity):
    image = openImageFromPath(path1)
    imgSize = image.size
    colors, counts = np.unique(image.reshape(-1), return_counts = True, axis = 0)
    cumProb = []
    for i in range(len(counts)):
        prob = counts[i] / imgSize
        if i == 0:
            cumProb.append(prob)
        else:
            cumProb.append(cumProb[i-1] + prob)
    
    newImg = [(cumProb[np.where(colors == image[i][j])[0][0]] * intensity) for i in range(image.shape[1]) for j in range(image.shape[0])]
    saveImageAs(np.reshape(newImg, image.shape), 'equalizedHist' + str(intensity) + '.tiff')




# template_matching('F:/Pictures/Testing/result arctichare 32 x 32.tiff', 'F:/Pictures/Pengujian citra pesan/arctichare 32 x 32.tiff')
# equalizeHistogram('D:/Projects/Python Projects/DCT-Permutation-Chaotic-Encryption/test.tif', 255)
# saveImageAs(sp_noise(bgr2gray(openImageFromPath('D:/Projects/Python Projects/DCT-Permutation-Chaotic-Encryption/test.tiff')), 0.0001), 'salted_image.tiff')