from scipy.fftpack import dct, idct
from function.CommonFunction import np

# implement 2D DCT
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')

# implement 2D IDCT
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')

def createDctSubBlock(subBlock):
    dctSB = list()
    for i in range(len(subBlock)):
        dctSB.append(dct2(subBlock[i]))
    return dctSB

def createDcCoefficientMatrix(dctSubBlock):
    dcCoefficientMatrix = np.zeros(len(dctSubBlock), dtype='float32')

    for i in range(len(dctSubBlock)):
        dcCoefficientMatrix[i] = (dctSubBlock[i])[0][0]

    return np.reshape(dcCoefficientMatrix, (32,32))

def restoreDcCoefficientMatrixThenIdct(embeddedMatrix, dctSubBlock):
    embeddedList = embeddedMatrix.reshape(-1)
    idctSB = list()
    for i in range(len(embeddedList)):
        dctSubBlock[i][0][0] = embeddedList[i]
        idctSB.append(idct2(dctSubBlock[i]))
    return idctSB