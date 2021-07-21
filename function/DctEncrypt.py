from PyQt5.QtWidgets import QMessageBox
from .CommonFunction import imageio, bgr2gray, convertSubBlockToImage, convertImageToSubBlock, loadDcMatrix, saveImageAs, saveDcMatrix, loadDcMatrix, fullStackTrace, VALIDATION_ERROR, ACTION_CANCELLED, validCriteria, validate
from .DiscreteCosineTransform import createDctSubBlock, createDcCoefficientMatrix, restoreDcCoefficientMatrixThenIdct
from .PermutationBasedChaoticEncryption import encryption, decryption

def embedEncryptionMessageToDcCoefficientMatrix(cipherImage, dccMatrix, alpha = 1):
    return dccMatrix + (cipherImage/255 * alpha)

def processEncryptionAndStegano(coverImgPath, messageImgPath, x0, y0, saveFileDialog, showMessageBox):
    try:
        coverImage, messageImage = validate(coverImgPath, messageImgPath)

        coverImageShape = coverImage.shape
        messageImageShape = messageImage.shape

        cipherImage = encryption(messageImage, x0, y0)

        subBlock = convertImageToSubBlock(coverImage, (coverImageShape[0]//messageImageShape[0]))

        dctSubBlock = createDctSubBlock(subBlock)

        dcCoefficientMatrix = createDcCoefficientMatrix(dctSubBlock, messageImageShape)

        embeddedMatrix = embedEncryptionMessageToDcCoefficientMatrix(cipherImage, dcCoefficientMatrix)

        idctSubBlock = restoreDcCoefficientMatrixThenIdct(embeddedMatrix, dctSubBlock)

        embeddedImage = convertSubBlockToImage(idctSubBlock, coverImageShape,  (coverImageShape[0]//messageImageShape[0]))
        
        fileName = saveFileDialog()

        saveDcMatrix(dcCoefficientMatrix, fileName)
    
        return saveImageAs(embeddedImage, fileName)
    except Exception as e:
        s = getattr(e, 'message', str(e))
        if s == VALIDATION_ERROR:
            showMessageBox('Warning', validCriteria(), QMessageBox.Icon.Warning)
        elif s != ACTION_CANCELLED:
            showMessageBox('Error', fullStackTrace(), QMessageBox.Icon.Critical)
        
        return None

def recoverEncryptionMessageFromDcCoefficientMatrix(dccStego, dccCover, alpha = 1):
    return (dccStego - (dccCover * alpha)) * 255

def processExtractAndDecrypt(steganoImgPath, dcMatrixPath, x0, y0, saveFileDialog, showMessageBox):
    try:
        steganoImage, dcMatrix = validate(steganoImgPath, dcMatrixPath)

        dctMatrixShape = dcMatrix.shape

        stegoSubBlock = convertImageToSubBlock(steganoImage, 16)

        dctStegoSubBlock = createDctSubBlock(stegoSubBlock)

        stegoDcCoefficient = createDcCoefficientMatrix(dctStegoSubBlock, dctMatrixShape)

        encryptedMessage = recoverEncryptionMessageFromDcCoefficientMatrix(stegoDcCoefficient, dcMatrix)

        decryptedMessage = decryption(encryptedMessage, x0, y0)

        fileName = saveFileDialog()

        return saveImageAs(decryptedMessage.astype('uint8'), fileName)
    except Exception as e:
        s = getattr(e, 'message', str(e))
        if s == VALIDATION_ERROR:
            showMessageBox('Warning', validCriteria(), QMessageBox.Icon.Warning)
        elif s != ACTION_CANCELLED:
            showMessageBox('Error', fullStackTrace(), QMessageBox.Icon.Critical)
        return None