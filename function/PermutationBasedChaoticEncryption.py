import HenonMapGenerator as hmg
import numpy as np
import copy

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

        RK.append(mid_arr[3])
        GK.append(mid_arr[4])
        BK.append(mid_arr[5])

    original_image = np.reshape(message_image, image_size)
    
    for i in range(image_size):
        temp_pixel = copy.deepcopy(original_image[i])
        original_image[i] = copy.deepcopy(original_image[XS[i]])
        original_image[XS[i]] = temp_pixel

    new_image = np.zeros(image_size, dtype = np.uint8)
    for i in range(image_size):
        new_image[i][0] = original_image[i][0] ^ RK[i]
        new_image[i][1] = original_image[i][1] ^ GK[i]
        new_image[i][2] = original_image[i][2] ^ BK[i]

    return np.reshape(new_image, (message_image.shape))