from .CommonFunction import cv2, deepCopy, bgr2gray, convertSubBlockToImage, convertImageToSubBlock, saveImageAsTiff, saveImageAsJpeg
from .DiscreteCosineTransform import createDctSubBlock, createDcCoefficientMatrix, restoreDcCoefficientMatrixThenIdct
from .PermutationBasedChaoticEncryption import encryption, decryption

def embedEncryptionMessageToDcCoefficientMatrix(cipherImage, dccMatrix, alpha = 1):
    return dccMatrix + (cipherImage/255 * alpha)

def processEncryptionAndStegano(coverImgPath, messageImgPath, x0, y0):
    coverImage = bgr2gray(cv2.imread(coverImgPath)).astype('float32')
    messageImage = bgr2gray(cv2.imread(messageImgPath)).astype('float32')

    cipherImage = encryption(deepCopy(messageImage), x0, y0)

    subBlock = convertImageToSubBlock(deepCopy(coverImage), 16)

    dctSubBlock = createDctSubBlock(deepCopy(subBlock))

    dcCoefficientMatrix = createDcCoefficientMatrix(deepCopy(dctSubBlock))

    embeddedMatrix = embedEncryptionMessageToDcCoefficientMatrix(deepCopy(cipherImage), deepCopy(dcCoefficientMatrix))

    idctSubBlock = restoreDcCoefficientMatrixThenIdct(deepCopy(embeddedMatrix), deepCopy(dctSubBlock))

    embeddedImage = convertSubBlockToImage(deepCopy(idctSubBlock), 16)

    return saveImageAsTiff(embeddedImage)

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