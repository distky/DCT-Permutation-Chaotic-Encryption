from .CommonFunction import convertSubBlockToImage, convertImageToSubBlock, rounding
from .DiscreteCosineTransform import createDctSubBlock, createDcCoefficientMatrix, restoreDcCoefficientMatrixThenIdct

SUBBLOCK_WH = 16

def embedEncryptionMessageToDcCoefficientMatrix(encryptedImage, dccMatrix, alpha = 1/255):
    return dccMatrix + (encryptedImage * alpha)

def steganography(coverImage, encryptedImage):
    coverImageShape = coverImage.shape
    encryptedImageShape = encryptedImage.shape

    subBlock = convertImageToSubBlock(coverImage, SUBBLOCK_WH)

    dctSubBlock = createDctSubBlock(subBlock)

    dcCoefficientMatrix = createDcCoefficientMatrix(dctSubBlock, encryptedImageShape)

    embeddedMatrix = embedEncryptionMessageToDcCoefficientMatrix(encryptedImage, dcCoefficientMatrix)

    idctSubBlock = restoreDcCoefficientMatrixThenIdct(embeddedMatrix, dctSubBlock)

    steganoImage = convertSubBlockToImage(idctSubBlock, coverImageShape, SUBBLOCK_WH)

    return steganoImage, dcCoefficientMatrix

def recoverEncryptionMessageFromDcCoefficientMatrix(dccStego, dccCover, alpha = 255):
    return (dccStego - dccCover) * alpha, (dccStego - (dccStego - dccCover))

def extraction(steganoImage, dcMatrix):
    stegoSubBlock = convertImageToSubBlock(steganoImage, SUBBLOCK_WH)

    dctStegoSubBlock = createDctSubBlock(stegoSubBlock)

    stegoDcMatrix = createDcCoefficientMatrix(dctStegoSubBlock, dcMatrix.shape)
    
    encryptedMessage, extractedDct = recoverEncryptionMessageFromDcCoefficientMatrix(stegoDcMatrix, dcMatrix)

    coverSubBlock = restoreDcCoefficientMatrixThenIdct(extractedDct, dctStegoSubBlock)

    coverImage = convertSubBlockToImage(coverSubBlock, steganoImage.shape, SUBBLOCK_WH)

    return rounding(encryptedMessage,0).astype('uint8'), rounding(coverImage,0).astype('uint8')