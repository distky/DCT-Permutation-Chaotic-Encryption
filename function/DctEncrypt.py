from .CommonFunction import imageio, deepCopy, bgr2gray, convertSubBlockToImage, convertImageToSubBlock, loadDcMatrix, saveImageAs, saveDcMatrix, loadDcMatrix
from .DiscreteCosineTransform import createDctSubBlock, createDcCoefficientMatrix, restoreDcCoefficientMatrixThenIdct
from .PermutationBasedChaoticEncryption import encryption, decryption

def embedEncryptionMessageToDcCoefficientMatrix(cipherImage, dccMatrix, alpha = 1):
    return dccMatrix + (cipherImage/255 * alpha)

def processEncryptionAndStegano(coverImgPath, messageImgPath, x0, y0):
    coverImage = bgr2gray(imageio.imread(coverImgPath))
    messageImage = bgr2gray(imageio.imread(messageImgPath))

    cipherImage = encryption(deepCopy(messageImage), x0, y0)

    subBlock = convertImageToSubBlock(deepCopy(coverImage), 16)

    dctSubBlock = createDctSubBlock(deepCopy(subBlock))

    dcCoefficientMatrix = createDcCoefficientMatrix(deepCopy(dctSubBlock))

    embeddedMatrix = embedEncryptionMessageToDcCoefficientMatrix(deepCopy(cipherImage), deepCopy(dcCoefficientMatrix))

    idctSubBlock = restoreDcCoefficientMatrixThenIdct(deepCopy(embeddedMatrix), deepCopy(dctSubBlock))

    embeddedImage = convertSubBlockToImage(deepCopy(idctSubBlock), 16)
    
    saveDcMatrix(dcCoefficientMatrix)

    return saveImageAs(embeddedImage, 'stegano', '.tiff')

def recoverEncryptionMessageFromDcCoefficientMatrix(dccStego, dccCover, alpha = 1):
    return (dccStego - (dccCover * alpha)) * 255

def processExtractAndDecrypt(steganoImgPath, dcMatrixPath, x0, y0):
    steganoImage = bgr2gray(imageio.imread(steganoImgPath))

    dcMatrix = loadDcMatrix(dcMatrixPath)

    stegoSubBlock = convertImageToSubBlock(deepCopy(steganoImage), 16)

    dctStegoSubBlock = createDctSubBlock(deepCopy(stegoSubBlock))

    stegoDcCoefficient = createDcCoefficientMatrix(deepCopy(dctStegoSubBlock))

    encryptedMessage = recoverEncryptionMessageFromDcCoefficientMatrix(deepCopy(stegoDcCoefficient), deepCopy(dcMatrix))

    decryptedMessage = decryption(deepCopy(encryptedMessage), x0, y0)

    return saveImageAs(decryptedMessage.astype('uint8'), 'result', '.jpeg')