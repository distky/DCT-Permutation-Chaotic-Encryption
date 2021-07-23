from .CommonFunction import convertSubBlockToImage, convertImageToSubBlock
from .DiscreteCosineTransform import createDctSubBlock, createDcCoefficientMatrix, restoreDcCoefficientMatrixThenIdct

def embedEncryptionMessageToDcCoefficientMatrix(cipherImage, dccMatrix, alpha = 1):
    return dccMatrix + (cipherImage * alpha)

def steganography(coverImage, cipherImage):
    coverImageShape = coverImage.shape
    cipherImageShape = cipherImage.shape

    subBlock = convertImageToSubBlock(coverImage, 16)

    dctSubBlock = createDctSubBlock(subBlock)

    dcCoefficientMatrix = createDcCoefficientMatrix(dctSubBlock, cipherImageShape)

    embeddedMatrix = embedEncryptionMessageToDcCoefficientMatrix(cipherImage, dcCoefficientMatrix, 1/255)

    idctSubBlock = restoreDcCoefficientMatrixThenIdct(embeddedMatrix, dctSubBlock)

    embeddedImage = convertSubBlockToImage(idctSubBlock, coverImageShape, 16)

    return embeddedImage, dcCoefficientMatrix

def recoverEncryptionMessageFromDcCoefficientMatrix(dccStego, dccCover, alpha = 1):
    return (dccStego - dccCover) * alpha

def extraction(steganoImage, dcMatrix):
    stegoSubBlock = convertImageToSubBlock(steganoImage, 16)

    dctStegoSubBlock = createDctSubBlock(stegoSubBlock)

    stegoDcCoefficient = createDcCoefficientMatrix(dctStegoSubBlock, dcMatrix.shape)

    return recoverEncryptionMessageFromDcCoefficientMatrix(stegoDcCoefficient, dcMatrix, 255)