from PyQt5.QtWidgets import QMessageBox
from .CommonFunction import convertImageToPixmap, rounding, saveImageAs, saveDcMatrix, fullStackTrace, VALIDATION_ERROR, ACTION_CANCELLED, validCriteria, validate
from .PermutationBasedChaoticEncryption import encryption, decryption
from .DctSteganography import steganography, extraction

def processEncryptionAndStegano(coverImgPath, messageImgPath, x0, y0, saveFileDialog, showMessageBox):
    try:
        coverImage, messageImage = validate(coverImgPath, messageImgPath)

        cipherImage = encryption(messageImage, x0, y0)

        embeddedImage, dcCoefficientMatrix = steganography(coverImage, cipherImage)
        
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

def processExtractAndDecrypt(steganoImgPath, dcMatrixPath, x0, y0, saveFileDialog, showMessageBox):
    try:
        steganoImage, dcMatrix = validate(steganoImgPath, dcMatrixPath)

        encryptedMessage = rounding(extraction(steganoImage, dcMatrix),0)

        decryptedMessage = rounding(decryption(encryptedMessage, x0, y0), 0).astype('uint8')

        fileName = saveFileDialog()

        saveImageAs(decryptedMessage, fileName)

        return convertImageToPixmap(decryptedMessage)
    except Exception as e:
        s = getattr(e, 'message', str(e))
        if s == VALIDATION_ERROR:
            showMessageBox('Warning', validCriteria(), QMessageBox.Icon.Warning)
        elif s != ACTION_CANCELLED:
            showMessageBox('Error', fullStackTrace(), QMessageBox.Icon.Critical)
        return None