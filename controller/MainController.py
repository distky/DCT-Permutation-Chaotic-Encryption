from function.CommonFunction import ACTION_CANCELLED, MSE, NCC, PSNR, saveImageAs, saveDcMatrix, validate, validateCrypto, validateStegano
from function.PermutationBasedChaoticEncryption import encryption, decryption
from function.DctSteganography import steganography, extraction
import re

def processEncryption(messageImgPath, x0, y0):
    messageImage, x0, y0 = validateCrypto(messageImgPath, x0, y0)
    return encryption(messageImage, x0, y0).astype('uint8'), x0, y0

def processStegano(coverImgPath, encryptedImage):
    coverImage, encryptedImage = validateStegano(coverImgPath, encryptedImage)
    return steganography(coverImage, encryptedImage)

def processExtraction(steganoImgPath, dcMatrixPath):
    steganoImage, dcMatrix = validateStegano(steganoImgPath, dcMatrixPath)
    return extraction(steganoImage, dcMatrix)

def processDecryption(encryptedImage, x0, y0):
    encryptedImage, x0, y0 = validateCrypto(encryptedImage, x0, y0)
    return decryption(encryptedImage, x0, y0).astype('uint8')

def processMSE(img1Path, img2Path):
    validate(img1Path, img2Path)
    return MSE(img1Path, img2Path)

def processPSNR(img1Path, img2Path):
    validate(img1Path, img2Path)
    return PSNR(img1Path, img2Path)

def processNCC(img1Path, img2Path):
    validate(img1Path, img2Path)
    return NCC(img1Path, img2Path)

def processSaveResult(saveFileDialog, showMessageBox, imgList = [], x0 = None, y0 = None, dcMatrix = []):
    filename = saveFileDialog()

    for img, extra in imgList:
        splittedPath = filename.split('.')
        splittedPath[-2] = splittedPath[-2] + extra
        saveImageAs(img, '.'.join(splittedPath))

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