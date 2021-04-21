import math

def decimal_to_binary(n): 
    binary = bin(n).replace("0b", "")
    for _ in range(56 - len(binary)):
        binary = "0" + binary
    return binary

def binary_to_decimal(bit_arr):
    decimal = 0
    for bit in bit_arr:
        decimal = decimal * 2 + int(bit)
    return decimal

def binary_to_7_byte(binary):
    bin_arr = list(binary);
    result = []
    binary_arr = []
    for i in range(len(bin_arr)):
        if i % 8 == 0:
            result.append(binary_to_decimal(binary_arr))
            binary_arr = []
        else:
            binary_arr.append(bin_arr[i])
    return result

def create_henon_map(xo, yo, a = 1.4, b = 0.3, size = 64):
    x = xo
    y = yo
    result = [[],[]]
    for i in range(size+100):
        x_n = y + 1 - a* x**2
        y_n = b * x

        x = x_n
        y = y_n

        if(i < 100): continue

        e_n = int(abs(x_n * math.pow(10,15)))
        f_n = int(abs(y_n * math.pow(10,15)))

        result[0].append(e_n)
        result[1].append(f_n)

    return result