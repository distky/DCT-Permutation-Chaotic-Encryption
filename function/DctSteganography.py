from .CommonFunction import convertSubBlockToImage, convertImageToSubBlock, rounding, saveImageAs
from .DiscreteCosineTransform import createDctSubBlock, createDcCoefficientMatrix, restoreDcCoefficientMatrixThenIdct

def embedEncryptionMessageToDcCoefficientMatrix(encryptedImage, dccMatrix, alpha = 1):
    return dccMatrix + (encryptedImage * alpha)

def steganography(coverImage, encryptedImage):
    coverImageShape = coverImage.shape
    encryptedImageShape = encryptedImage.shape

    subBlock = convertImageToSubBlock(coverImage, 16)

    dctSubBlock = createDctSubBlock(subBlock)

    dcCoefficientMatrix = createDcCoefficientMatrix(dctSubBlock, encryptedImageShape)

    embeddedMatrix = embedEncryptionMessageToDcCoefficientMatrix(encryptedImage, dcCoefficientMatrix, 1/255)

    idctSubBlock = restoreDcCoefficientMatrixThenIdct(embeddedMatrix, dctSubBlock)

    steganoImage = convertSubBlockToImage(idctSubBlock, coverImageShape, 16)

    return steganoImage, dcCoefficientMatrix

def recoverEncryptionMessageFromDcCoefficientMatrix(dccStego, dccCover, alpha = 1):
    return (dccStego - dccCover) * alpha, (dccStego - (dccStego - dccCover))

def extraction(steganoImage, dcMatrix):
    stegoSubBlock = convertImageToSubBlock(steganoImage, 16)

    dctStegoSubBlock = createDctSubBlock(stegoSubBlock)

    stegoDcMatrix = createDcCoefficientMatrix(dctStegoSubBlock, dcMatrix.shape)
    
    encryptedMessage, extractedDct = recoverEncryptionMessageFromDcCoefficientMatrix(stegoDcMatrix, dcMatrix, 255)

    coverSubBlock = restoreDcCoefficientMatrixThenIdct(extractedDct, dctStegoSubBlock)

    coverImage = convertSubBlockToImage(coverSubBlock, steganoImage.shape, 16)

    return rounding(encryptedMessage,0).astype('uint8'), rounding(coverImage,0).astype('uint8')