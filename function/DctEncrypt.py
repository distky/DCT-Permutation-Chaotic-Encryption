from function.CommonFunction import cv2, deepCopy, bgr2gray, convertSubBlockToImage, convertImageToSubBlock, saveImageAsTiff
import function.DiscreteCosineTransform as dct
import function.PermutationBasedChaoticEncryption as pbce

def embedEncryptionMessageToDcCoefficientMatrix(cipherImage, dccMatrix, alpha = 1):
    return dccMatrix + (cipherImage/255 * alpha)

def processEncryptionAndStegano(coverImgPath, messageImgPath, x0, y0):
    coverImage = bgr2gray(cv2.imread(coverImgPath)).astype('float32')
    messageImage = bgr2gray(cv2.imread(messageImgPath)).astype('float32')

    cipherImage = pbce.encryption(deepCopy(messageImage), x0, y0)

    subBlock = convertImageToSubBlock(deepCopy(coverImage), 16)

    dctSubBlock = dct.createDctSubBlock(deepCopy(subBlock))

    dcCoefficientMatrix = dct.createDcCoefficientMatrix(deepCopy(dctSubBlock))

    embeddedMatrix = embedEncryptionMessageToDcCoefficientMatrix(deepCopy(cipherImage), deepCopy(dcCoefficientMatrix))

    idctSubBlock = dct.restoreDcCoefficientMatrixThenIdct(deepCopy(embeddedMatrix), deepCopy(dctSubBlock))

    embeddedImage = convertSubBlockToImage(deepCopy(idctSubBlock), 16)

    return saveImageAsTiff(embeddedImage)