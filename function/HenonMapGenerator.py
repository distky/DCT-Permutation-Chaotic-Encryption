import math

def decimalToBinary(n): 
    binary = bin(n).replace("0b", "")
    for _ in range(56 - len(binary)):
        binary = "0" + binary
    return binary

def binaryToDecimal(bit_arr):
    decimal = 0
    for bit in bit_arr:
        decimal = decimal * 2 + int(bit)
    return decimal

def binaryTo7byte(binary):
    bin_arr = list(binary)
    result = []
    binary_arr = []
    for i in range(len(bin_arr)):
        binary_arr.append(bin_arr[i])
        if len(binary_arr) == 8:
            result.append(binaryToDecimal(binary_arr))
            binary_arr = []
    return result

def createHenonMap(xo, yo, a = 1.4, b = 0.3, size = 0):
    x0 = xo
    y0 = yo
    result = [[],[]]
    for i in range(size+100):
        x = y0 + 1 - a*x0**2
        y = b * x0

        x = x % 10 if x > 0 else x % -10
        y = y % 10 if y > 0 else y % -10

        x0 = x
        y0 = y

        if(i < 100): continue
        result[0].append(int(abs(x * math.pow(10,15))))
        result[1].append(int(abs(y * math.pow(10,15))))

    return result