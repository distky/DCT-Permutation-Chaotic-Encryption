import math
import numpy as np
import cv2
from function.CommonFunction import openImageFromPath, rounding, saveImageAs, bgr2gray
from function.DctSteganography import steganography, extraction
from function.PermutationBasedChaoticEncryption import encryption, decryption
from function.DiscreteCosineTransform import discreteCosineTransform, inverseDiscreteCosineTransform, dct2, idct2

def sp_noise(image, prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    black = 0
    white = 255            
    probs = np.random.random(image.shape[:2])
    print(probs)
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

randomMessage = rounding(np.random.rand(2,2) * 255,0).astype('uint8')

randomCover = rounding(np.random.rand(32,32) * 255, 0).astype('uint8')

def CLAHE(path1):
    img = openImageFromPath(path1)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl1 = clahe.apply(img)
    cl1 = cl1.astype('uint8')

def clahe():
    citraSampul = openImageFromPath('D:/DCT_Permutation_Skripsi/DCT-Permutation-Chaotic-Encryption/lena_gray.jpeg')
    
    citraSampul = bgr2gray(citraSampul)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    citraSampul= clahe.apply(citraSampul)
    saveImageAs(citraSampul.astype('uint8'), 'D:/DCT_Permutation_Skripsi/DCT-Permutation-Chaotic-Encryption/lena_gray-contrast.jpeg')
    

clahe()
# print(randomMessage)

# dct = discreteCosineTransform(randomMessage)

# dct2 = dct2(randomMessage)

# print(dct)
# print(dct2)

# idct = inverseDiscreteCosineTransform(dct)

# inverseDct = idct2(dct2)
# idct3 = idct2(dct)

# print(idct[0][0])
# print(inverseDct[0][0])
# print(idct3[0][0])

# print(math.pi)

# print("==Source==")
# print(randomMessage)
# print(randomCover)

# encryptedRandomMessage = encryption(randomMessage)

# print('==Encrypted==')
# print(encryptedRandomMessage)

# stegoImage, dcMatrix = steganography(randomCover, encryptedRandomMessage)

# print('==After stego==')
# print(stegoImage)
# print(dcMatrix)

# extractedImage, _ = extraction(stegoImage, dcMatrix)

# print('==After extract==')
# print(extractedImage)

# decryptedImage = decryption(extractedImage)

# print('==After decrypt==')
# print(decryptedImage)

# template_matching('F:/Pictures/Testing/result arctichare 32 x 32.tiff', 'F:/Pictures/Pengujian citra pesan/arctichare 32 x 32.tiff')
# equalizeHistogram('D:/Projects/Python Projects/DCT-Permutation-Chaotic-Encryption/test.tif', 255)
#saveImageAs(sp_noise(bgr2gray(openImageFromPath('D:/Projects/Python Projects/DCT-Permutation-Chaotic-Encryption/test.tif')), 0.01), 'salted_image.tiff')
#saveImageAs(CLAHE(bgr2gray(openImageFromPath('D:/DCT_Permutation_Skripsi/DCT-Permutation-Chaotic-Encryption/lena_gray.jpeg'))), 'contrast.tiff')