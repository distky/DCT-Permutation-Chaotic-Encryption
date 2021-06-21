from .HenonMapGenerator import HenonMapGenerator as hmg
from .CommonFunction import np, deepCopy

def encryption(message_image, x = 0.1, y = 0.1):
    image_size = message_image.size

    henon_map = hmg.create_henon_map(x, y, size = image_size)

    X = henon_map[0]
    Y = henon_map[1]

    RK = []
    GK = []
    BK = []

    XS = []

    for i in range(len(Y)):
        XS.append(X[i] % image_size)
        binary_y = hmg.decimal_to_binary(Y[i])
        
        mid_arr = hmg.binary_to_7_byte(binary_y)

        RK.append(mid_arr[2])
        GK.append(mid_arr[3])
        BK.append(mid_arr[4])

    original_image = np.reshape(message_image, image_size)
    
    for i in range(image_size):
        temp_pixel = deepCopy(original_image[i])
        original_image[i] = deepCopy(original_image[XS[i]])
        original_image[XS[i]] = temp_pixel

    new_image = np.zeros(image_size, dtype = 'float32')
    for i in range(image_size):
        new_image[i] = int(original_image[i]) ^ ((int(GK[i]) + int(RK[i]) + int(BK[i]))//3)

    return np.reshape(new_image, (message_image.shape))

def decryption(encrypted_image, x = 0.1, y = 0.1):
    image_size = encrypted_image.size

    henon_map = hmg.create_henon_map(x, y, size = image_size)

    X = henon_map[0]
    Y = henon_map[1]

    RK = []
    GK = []
    BK = []

    XS = []

    for i in range(len(Y)):
        XS.append(X[i] % image_size)
        binary_y = hmg.decimalToBinary(Y[i])
        
        mid_arr = hmg.convertBinaryTo7Bytes(binary_y)

        RK.append(mid_arr[2])
        GK.append(mid_arr[3])
        BK.append(mid_arr[4])

    message_image = np.reshape(encrypted_image, image_size)
    new_image = np.zeros(image_size, dtype= 'float32')
    for i in range(image_size):
        new_image[i] = int(message_image[i]) ^ int(((RK[i]+ GK[i] + BK[i])//3))
    
    for i in range(image_size-1, -1, -1):
        temp_pixel = deepCopy(new_image[i])
        new_image[i] = deepCopy(new_image[XS[i]])
        new_image[XS[i]] = temp_pixel

    return np.reshape(new_image, (encrypted_image.shape))