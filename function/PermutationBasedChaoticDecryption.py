import HenonMapGenerator as hmg
import numpy as np
import copy

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

        RK.append(mid_arr[3])
        GK.append(mid_arr[4])
        BK.append(mid_arr[5])

    message_image = np.reshape(encrypted_image, image_size)
    new_image = np.zeros(image_size, dtype= np.uint8)
    for i in range(image_size):
        # new_image[i] = int(message_image[i]) ^ int(((RK[i]+ GK[i] + BK[i])//3)) # Grayscale
        new_image[i][0] = message_image[i][0] ^ RK[i]
        new_image[i][1] = message_image[i][1] ^ GK[i]
        new_image[i][2] = message_image[i][2] ^ BK[i]
    
    for i in range(image_size-1, -1, -1):
        temp_pixel = copy.deepcopy(new_image[i])
        new_image[i] = copy.deepcopy(new_image[XS[i]])
        new_image[XS[i]] = temp_pixel

    return np.reshape(new_image, (encrypted_image.shape))