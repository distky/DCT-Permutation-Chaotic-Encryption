from PyQt5.QtWidgets import QMessageBox
from .CommonFunction import convertImageToPixmap, imageio, bgr2gray, convertSubBlockToImage, convertImageToSubBlock, loadDcMatrix, saveImageAs, saveDcMatrix, loadDcMatrix, fullStackTrace, VALIDATION_ERROR, ACTION_CANCELLED, validCriteria, validate
from .DiscreteCosineTransform import createDctSubBlock, createDcCoefficientMatrix, restoreDcCoefficientMatrixThenIdct
from .PermutationBasedChaoticEncryption import encryption, decryption
import pandas as pd

def embedEncryptionMessageToDcCoefficientMatrix(cipherImage, dccMatrix, alpha = 1):
    return dccMatrix + (cipherImage / alpha)

def processEncryptionAndStegano(coverImgPath, messageImgPath, x0, y0, saveFileDialog, showMessageBox):
    try:
        coverImage, messageImage = validate(coverImgPath, messageImgPath)

        coverImageShape = coverImage.shape
        messageImageShape = messageImage.shape

        df = pd.DataFrame(messageImage)
        df.to_csv('file_messageImage.csv',index=False)

        cipherImage = encryption(messageImage, x0, y0)

        subBlock = convertImageToSubBlock(coverImage, (coverImageShape[0]//messageImageShape[0]))

        dctSubBlock = createDctSubBlock(subBlock)

        dcCoefficientMatrix = createDcCoefficientMatrix(dctSubBlock, messageImageShape)

        embeddedMatrix = embedEncryptionMessageToDcCoefficientMatrix(cipherImage, dcCoefficientMatrix, 255)

        idctSubBlock = restoreDcCoefficientMatrixThenIdct(embeddedMatrix, dctSubBlock)

        embeddedImage = convertSubBlockToImage(idctSubBlock, coverImageShape,  (coverImageShape[0]//messageImageShape[0]))
        
        fileName = saveFileDialog()

        saveDcMatrix(dcCoefficientMatrix, fileName)
    
        saveImageAs(embeddedImage, fileName)

        return convertImageToPixmap(embeddedImage)
    except Exception as e:
        s = getattr(e, 'message', str(e))
        if s == VALIDATION_ERROR:
            showMessageBox('Warning', validCriteria(), QMessageBox.Icon.Warning)
        elif s != ACTION_CANCELLED:
            showMessageBox('Error', fullStackTrace(), QMessageBox.Icon.Critical)
        
        return None

def recoverEncryptionMessageFromDcCoefficientMatrix(dccStego, dccCover, alpha = 1):
    return (dccStego - dccCover) * alpha

def processExtractAndDecrypt(steganoImgPath, dcMatrixPath, x0, y0, saveFileDialog, showMessageBox):
    try:
        steganoImage, dcMatrix = validate(steganoImgPath, dcMatrixPath)

        dctMatrixShape = dcMatrix.shape

        stegoSubBlock = convertImageToSubBlock(steganoImage, 16)

        dctStegoSubBlock = createDctSubBlock(stegoSubBlock)

        stegoDcCoefficient = createDcCoefficientMatrix(dctStegoSubBlock, dctMatrixShape)

        encryptedMessage = recoverEncryptionMessageFromDcCoefficientMatrix(stegoDcCoefficient, dcMatrix, 255)

        decryptedMessage = decryption(encryptedMessage, x0, y0)

        df = pd.DataFrame(decryptedMessage)
        df.to_csv('file_decryptedMessage.csv',index=False)

        fileName = saveFileDialog()

        saveImageAs(decryptedMessage.astype('uint8'), fileName)

        return convertImageToPixmap(decryptedMessage.astype('uint8'))
    except Exception as e:
        s = getattr(e, 'message', str(e))
        if s == VALIDATION_ERROR:
            showMessageBox('Warning', validCriteria(), QMessageBox.Icon.Warning)
        elif s != ACTION_CANCELLED:
            showMessageBox('Error', fullStackTrace(), QMessageBox.Icon.Critical)
        return None