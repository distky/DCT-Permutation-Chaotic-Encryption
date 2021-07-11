import sys
from numpy import e
from .CommonFunction import imageio, deepCopy, bgr2gray, convertSubBlockToImage, convertImageToSubBlock, loadDcMatrix, saveImageAs, saveDcMatrix, loadDcMatrix
from .DiscreteCosineTransform import createDctSubBlock, createDcCoefficientMatrix, restoreDcCoefficientMatrixThenIdct
from .PermutationBasedChaoticEncryption import encryption, decryption

def embedEncryptionMessageToDcCoefficientMatrix(cipherImage, dccMatrix, alpha = 1):
    return dccMatrix + (cipherImage/255 * alpha)

def processEncryptionAndStegano(coverImgPath, messageImgPath, x0, y0, saveFileDialog):
    try:
        coverImage = bgr2gray(imageio.imread(coverImgPath))
        messageImage = bgr2gray(imageio.imread(messageImgPath))

        coverImageShape = coverImage.shape
        messageImageShape = messageImage.shape

        cipherImage = encryption(deepCopy(messageImage), x0, y0)

        subBlock = convertImageToSubBlock(deepCopy(coverImage), (coverImageShape[0]//messageImageShape[0]))

        dctSubBlock = createDctSubBlock(deepCopy(subBlock))

        dcCoefficientMatrix = createDcCoefficientMatrix(deepCopy(dctSubBlock), messageImageShape)

        embeddedMatrix = embedEncryptionMessageToDcCoefficientMatrix(deepCopy(cipherImage), deepCopy(dcCoefficientMatrix))

        idctSubBlock = restoreDcCoefficientMatrixThenIdct(deepCopy(embeddedMatrix), deepCopy(dctSubBlock))

        embeddedImage = convertSubBlockToImage(deepCopy(idctSubBlock), coverImageShape,  (coverImageShape[0]//messageImageShape[0]))
        
        fileName = saveFileDialog()

        saveDcMatrix(dcCoefficientMatrix, fileName)
    
        return saveImageAs(embeddedImage, fileName)
    except:
        print(sys.exc_info())
        return None

def recoverEncryptionMessageFromDcCoefficientMatrix(dccStego, dccCover, alpha = 1):
    return (dccStego - (dccCover * alpha)) * 255

def processExtractAndDecrypt(steganoImgPath, dcMatrixPath, x0, y0, saveFileDialog):
    try:
        steganoImage = bgr2gray(imageio.imread(steganoImgPath))

        dcMatrix = loadDcMatrix(dcMatrixPath)
        dctMatrixShape = dcMatrix.shape

        stegoSubBlock = convertImageToSubBlock(deepCopy(steganoImage), 16)

        dctStegoSubBlock = createDctSubBlock(deepCopy(stegoSubBlock))

        stegoDcCoefficient = createDcCoefficientMatrix(deepCopy(dctStegoSubBlock), dctMatrixShape)

        encryptedMessage = recoverEncryptionMessageFromDcCoefficientMatrix(deepCopy(stegoDcCoefficient), deepCopy(dcMatrix))

        decryptedMessage = decryption(deepCopy(encryptedMessage), x0, y0)

        fileName = saveFileDialog()

        return saveImageAs(decryptedMessage.astype('uint8'), fileName)
    except:
        print(sys.exc_info())
        return None