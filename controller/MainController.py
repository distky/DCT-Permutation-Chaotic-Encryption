from function.CommonFunction import ACTION_CANCELLED, MSE, NCC, PSNR, rounding, saveImageAs, saveDcMatrix, validate
from function.PermutationBasedChaoticEncryption import encryption, decryption
from function.DctSteganography import steganography, extraction
import re

def processEncryptionAndStegano(coverImgPath, messageImgPath, x0, y0):
    coverImage, messageImage, *_ = validate(coverImgPath, messageImgPath, x0, y0)

    encryptedImage = encryption(messageImage, x0, y0)

    steganoImage, dcCoefficientMatrix = steganography(coverImage, encryptedImage)
    
    return steganoImage, dcCoefficientMatrix, x0, y0

def processExtractAndDecrypt(steganoImgPath, dcMatrixPath, x0, y0):
    steganoImage, dcMatrix, x0, y0 = validate(steganoImgPath, dcMatrixPath, x0=x0, y0=y0)

    encryptedImage = rounding(extraction(steganoImage, dcMatrix),0)

    decyptedImage = rounding(decryption(encryptedImage, x0, y0), 0).astype('uint8')

    return decyptedImage

def processMSE(img1Path, img2Path):
    validate(img1Path, img2Path, isCompare=True)
    return MSE(img1Path, img2Path)

def processPSNR(img1Path, img2Path):
    validate(img1Path, img2Path, isCompare=True)
    return PSNR(img1Path, img2Path)

def processNCC(img1Path, img2Path):
    validate(img1Path, img2Path, isCompare=True)
    return NCC(img1Path, img2Path)

def processSaveResult(image, saveFileDialog, showMessageBox, x0 = None, y0 = None, dcMatrix = []):
    filename = saveFileDialog()

    saveImageAs(image, filename)

    if len(dcMatrix) > 0:
        saveDcMatrix(dcMatrix, filename)

    if x0 and y0:
        processSaveKey(x0,y0, filename)
        
    showMessageBox()

def processSaveKey(x0, y0, filename):
    with open(filename + '.txt', 'w') as output:
        output.write('x0=' + str(x0) + ',y0=' + str(y0) + ';')

def processLoadKey(filepath):
    if filepath:
        keyRegex = re.compile(r'x0=(.*?),y0=(.*?);')
        with open(filepath, 'r') as output:
            keystring = output.read()
            result = keyRegex.search(keystring)
            x0, y0 = result.groups()
        return float(x0), float(y0)
    else:
        raise IOError(ACTION_CANCELLED)