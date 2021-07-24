from PyQt5.QtWidgets import QMessageBox
from function.CommonFunction import MSE, NCC, PSNR, rounding, saveImageAs, saveDcMatrix, fullStackTrace, VALIDATION_ERROR, ACTION_CANCELLED, validCriteria, validate
from function.PermutationBasedChaoticEncryption import encryption, decryption
from function.DctSteganography import steganography, extraction
import re

def processEncryptionAndStegano(coverImgPath, messageImgPath, x0, y0):
    coverImage, messageImage, *_ = validate(coverImgPath, messageImgPath, x0, y0)

    cipherImage = encryption(messageImage, x0, y0)

    embeddedImage, dcCoefficientMatrix = steganography(coverImage, cipherImage)
    
    return embeddedImage, dcCoefficientMatrix, x0, y0

def processExtractAndDecrypt(steganoImgPath, dcMatrixPath, x0, y0):
    steganoImage, dcMatrix, x0, y0 = validate(steganoImgPath, dcMatrixPath, x0=x0, y0=y0)

    encryptedMessage = rounding(extraction(steganoImage, dcMatrix),0)

    decryptedMessage = rounding(decryption(encryptedMessage, x0, y0), 0).astype('uint8')

    return decryptedMessage

def processMSE(img1Path, img2Path):
    validate(img1Path, img2Path, isCompare=True)
    return MSE(img1Path, img2Path)

def processPSNR(img1Path, img2Path):
    validate(img1Path, img2Path, isCompare=True)
    return PSNR(img1Path, img2Path)

def processNCC(img1Path, img2Path):
    validate(img1Path, img2Path, isCompare=True)
    return NCC(img1Path, img2Path)

def processSaveResult(embeddedImage, saveFileDialog, dcMatrix = None):
    filename = saveFileDialog()

    saveDcMatrix(dcMatrix, filename)

    saveImageAs(embeddedImage, filename)

def processSaveKey(x0, y0, saveFileDialog):
    filename = saveFileDialog()

    with open(filename, 'w') as output:
        output.write('x0=' + str(x0) + ',y0=' + str(y0) + ';')

def processLoadKey(filepath):
    if filepath:
        keyRegex = re.compile(r'x0=(.*?),y0=(.*?);')
        with open(filepath, 'r') as output:
            keystring = output.read()
            result = keyRegex.search(keystring)
            x0, y0 = result.groups()
        return float(x0), float(y0)


def handleException(e, showMessageBox):
    s = getattr(e, 'message', str(e))
    if s == VALIDATION_ERROR:
        showMessageBox('Warning', validCriteria(), QMessageBox.Icon.Warning)
    elif s != ACTION_CANCELLED:
        showMessageBox('Error', fullStackTrace(), QMessageBox.Icon.Critical)