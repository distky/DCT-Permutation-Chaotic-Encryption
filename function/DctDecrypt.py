from .CommonFunction import cv2, bgr2gray, deepCopy, convertImageToSubBlock, saveImageAsJpeg
from .DiscreteCosineTransform import createDctSubBlock, createDcCoefficientMatrix
from .PermutationBasedChaoticEncryption import decryption

def recoverEncryptionMessageFromDcCoefficientMatrix(dccStego, dccCover, alpha = 1):
    return (dccStego - (dccCover * alpha) * 255)

def processExtractAndDecrypt(coverImgPath, steganoImgPath, x0, y0):
    coverImage = bgr2gray(cv2.imread(coverImgPath)).astype('float32')
    steganoImage = bgr2gray(cv2.imread(steganoImgPath)).astype('float32')

    coverSubBlock = convertImageToSubBlock(deepCopy(coverImage), 16)
    stegoSubBlock = convertImageToSubBlock(deepCopy(steganoImage), 16)

    dctCoverSubBlock = createDctSubBlock(deepCopy(coverSubBlock))
    dctStegoSubBlock = createDctSubBlock(deepCopy(stegoSubBlock))

    coverDcCoefficient = createDcCoefficientMatrix(deepCopy(dctCoverSubBlock))
    stegoDcCoefficient = createDcCoefficientMatrix(deepCopy(dctStegoSubBlock))

    encryptedMessage = recoverEncryptionMessageFromDcCoefficientMatrix(deepCopy(stegoDcCoefficient), deepCopy(coverDcCoefficient))

    decryptedMessage = decryption(deepCopy(encryptedMessage), x0, y0)

    return saveImageAsJpeg(decryptedMessage)