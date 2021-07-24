from PyQt5.QtWidgets import QMessageBox
from function.CommonFunction import MSE, NCC, PSNR, rounding, saveImageAs, saveDcMatrix, fullStackTrace, VALIDATION_ERROR, ACTION_CANCELLED, validCriteria, validate
from function.PermutationBasedChaoticEncryption import encryption, decryption
from function.DctSteganography import steganography, extraction

def processEncryptionAndStegano(coverImgPath, messageImgPath, x0, y0):
    coverImage, messageImage, *_ = validate(coverImgPath, messageImgPath, x0, y0)

    cipherImage = encryption(messageImage, x0, y0)

    embeddedImage, dcCoefficientMatrix = steganography(coverImage, cipherImage)
    
    return embeddedImage, dcCoefficientMatrix, x0, y0

def processExtractAndDecrypt(steganoImgPath, dcMatrixPath):
    steganoImage, dcMatrix, x0, y0 = validate(steganoImgPath, dcMatrixPath)

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

def processSaveResult(embeddedImage, saveFileDialog, dcMatrix = None, x0 = 0, y0 = 0):
    filename = saveFileDialog()

    saveDcMatrix((dcMatrix, x0, y0), filename)

    saveImageAs(embeddedImage, filename)

    with open(filename + '.txt', 'w') as output:
        output.write('x0=' + str(x0) + ',y0=' + str(y0))

def handleException(e, showMessageBox):
    s = getattr(e, 'message', str(e))
    if s == VALIDATION_ERROR:
        showMessageBox('Warning', validCriteria(), QMessageBox.Icon.Warning)
    elif s != ACTION_CANCELLED:
        showMessageBox('Error', fullStackTrace(), QMessageBox.Icon.Critical)