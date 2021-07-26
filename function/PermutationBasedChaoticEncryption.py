from .HenonMapGenerator import decimalToBinary, binaryTo7byte, createHenonMap
from .CommonFunction import np, deepCopy

def encryption(messageImage, x = 0.1, y = 0.1):
    imageSize = messageImage.size

    henonMap = createHenonMap(x, y, size = imageSize)

    X = henonMap[0]
    Y = henonMap[1]
    
    encryptedImage = np.zeros(imageSize)

    RK = []
    GK = []
    BK = []

    XS = []

    for i in range(len(Y)):
        XS.append(X[i] % imageSize)
        binaryY = decimalToBinary(Y[i])
        
        midArr = binaryTo7byte(binaryY)

        RK.append(midArr[2])
        GK.append(midArr[3])
        BK.append(midArr[4])

    originalImage = np.reshape(messageImage, imageSize)
    
    for i in range(imageSize):
        tempPixel = deepCopy(originalImage[i])
        originalImage[i] = deepCopy(originalImage[XS[i]])
        originalImage[XS[i]] = tempPixel

    for i in range(imageSize):
        encryptedImage[i] = int(originalImage[i]) ^ ((int(GK[i]) + int(RK[i]) + int(BK[i]))//3)

    return np.reshape(encryptedImage, (messageImage.shape))

def decryption(encryptedImage, x = 0.1, y = 0.1):
    imageSize = encryptedImage.size

    henonMap = createHenonMap(x, y, size = imageSize)
    
    messageImage = np.zeros(imageSize)

    X = henonMap[0]
    Y = henonMap[1]

    RK = []
    GK = []
    BK = []

    XS = []

    for i in range(len(Y)):
        XS.append(X[i] % imageSize)
        binaryY = decimalToBinary(Y[i])
        
        midArr = binaryTo7byte(binaryY)

        RK.append(midArr[2])
        GK.append(midArr[3])
        BK.append(midArr[4])

    EI = np.reshape(encryptedImage, imageSize)
    for i in range(imageSize):
        messageImage[i] = int(EI[i]) ^ int(((RK[i]+ GK[i] + BK[i])//3))
    
    for i in range(imageSize-1, -1, -1):
        temp_pixel = deepCopy(messageImage[i])
        messageImage[i] = deepCopy(messageImage[XS[i]])
        messageImage[XS[i]] = temp_pixel

    return np.reshape(messageImage, (encryptedImage.shape))