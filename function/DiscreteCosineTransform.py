from scipy.fftpack import dct, idct
from .CommonFunction import np, math
import numba as nb

def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')

def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')

@nb.njit()
def discreteCosineTransform(image):
    dctArr = np.zeros(image.shape, dtype='float32')
    
    I, J = image.shape[0], image.shape[1]
    for p in range(image.shape[0]):
        for q in range(image.shape[1]):
            ap = 1/math.sqrt(I) if p == 0 else math.sqrt(2)/math.sqrt(I)
            aq = 1/math.sqrt(J) if q == 0 else math.sqrt(2)/math.sqrt(J)

            cos = np.array([image[i][j]*math.cos((math.pi * (2 * i + 1) * p) / (2 * I)) * math.cos((math.pi * (2 * j + 1) * q) / (2 * J)) for i in range(I) for j in range(J)])
    
            dctArr[p][q] = ap * aq * np.sum(cos)
    
    return dctArr

@nb.njit()
def inverseDiscreteCosineTransform(image):
    dctArr = np.zeros(image.shape, dtype='float32')

    I, J = image.shape[0], image.shape[1]

    for p in range(I):
        for q in range(J):
            ap = 1/math.sqrt(I) if p == 0 else math.sqrt(2)/math.sqrt(I)
            aq = 1/math.sqrt(J) if q == 0 else math.sqrt(2)/math.sqrt(J)

            cos = np.array([image[p][q] * ap * aq * math.cos((math.pi * (2 * i + 1) * p) / (2 * I)) * math.cos((math.pi * (2 * j + 1) * q) / (2 * J)) for i in range(I) for j in range(J)])

            dctArr[p][q] =  np.sum(cos)
    
    return dctArr

def createDctSubBlock(subBlock):
    return [dct2(subBlock[i]) for i in range(len(subBlock))]

def createDcCoefficientMatrix(dctSubBlock, shape):
    return np.reshape(np.array([(dctSubBlock[i])[0][0] for i in range(len(dctSubBlock))]), shape)

def restoreDcCoefficientMatrixThenIdct(embeddedMatrix, dctSubBlock):
    embeddedList = embeddedMatrix.reshape(-1)
    idctSB = list()
    for i in range(len(embeddedList)):
        dctSubBlock[i][0][0] = embeddedList[i]
        idctSB.append(idct2(dctSubBlock[i]))
    return idctSB