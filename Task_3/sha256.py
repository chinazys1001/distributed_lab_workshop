# У якості завдання обрав реалізацію алгоритму SHA-256 (SHA другої версії, розміром 256 бітів)

# basic operations: XOR, sum, shiftRight, rotateRight

from os import system


def XOR(binary_string1, binary_string2):
    return format(int(binary_string1, 2) ^ int(binary_string2, 2), '032b')
def sum(binary_string1, binary_string2):
    number_of_bits = len(binary_string1)
    return format((int(binary_string1, 2) + int(binary_string2, 2)) % (2 ** number_of_bits), '032b')
def shiftRight(binary_string, shift_bits):
    return format(int(binary_string, 2) >> shift_bits, '032b') 
def rotateRight(binary_string, shift_bits):
    number_of_bits = len(binary_string)
    shift_bits %= number_of_bits

    value = int(binary_string, 2)
    body = value >> shift_bits
    tail = value << (number_of_bits - shift_bits)
 
    res = (body | tail) & (2 ** number_of_bits - 1) # merging shifted part and remainder in 32-bit length
    return format(res, '032b')

# functions: sigma0, sigma1, SIGMA0, SIGMA1

def sigma0(binary_string):
    rotatedRight7 = rotateRight(binary_string, 7)
    rotatedRight18 = rotateRight(binary_string, 18)
    shiftedRight3 = shiftRight(binary_string, 3)
    return XOR(XOR(rotatedRight7, rotatedRight18), shiftedRight3)
def sigma1(binary_string):
    rotatedRight17 = rotateRight(binary_string, 17)
    rotatedRight19 = rotateRight(binary_string, 19)
    shiftedRight10 = shiftRight(binary_string, 10)
    return XOR(XOR(rotatedRight17, rotatedRight19), shiftedRight10)
def SIGMA0(binary_string):
    rotatedRight2 = rotateRight(binary_string, 2)
    rotatedRight13 = rotateRight(binary_string, 13)
    shiftedRight22 = rotateRight(binary_string, 22)
    return XOR(XOR(rotatedRight2, rotatedRight13), shiftedRight22)
def SIGMA1(binary_string):
    rotatedRight6 = rotateRight(binary_string, 6)
    rotatedRight11 = rotateRight(binary_string, 11)
    shiftedRight25 = rotateRight(binary_string, 25)
    return XOR(XOR(rotatedRight6, rotatedRight11), shiftedRight25)
# if i-th bit of x-word equals to 0 -> take i-th bit of z-word, else take i-th bit of y-word
def choice(binary_string_x, binary_string_y, binary_string_z):
    choice = list(format(0, '032b'))
    for i in range(0, len(binary_string_x)):
        if binary_string_x[i] == '0':
            choice[i] = binary_string_z[i]
        if binary_string_x[i] == '1':
            choice[i] = binary_string_y[i]
    return "".join(choice)
# takes three binary strings as input. i-th bit of output is 1 if i-th bit of 
# at least two of three input strings is equal to 1, else i-th bit of output is 0
def majority(binary_string_x, binary_string_y, binary_string_z):
    majority = list(format(0, '032b'))
    for i in range(0, len(binary_string_x)):
        if binary_string_x[i] == '1' and binary_string_y[i] == '1':
            majority[i] = '1'
        if binary_string_x[i] == '1' and binary_string_z[i] == '1':
            majority[i] = '1'
        if binary_string_y[i] == '1' and binary_string_z[i] == '1':
            majority[i] = '1'
    return "".join(majority)

# getting 64 hard-coded contant values. technically, these constants are 
# the fractional parts of cubic roots of the first 64 primaries, written in 32-bit format
def getConstants():
    cbrt_fractional_values = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
    ]
    res = list()
    for value in cbrt_fractional_values:
        res.append(format(value, "032b"))
    return res

# getting 8 hard-coded contant values. technically, these constants are 
# the fractional parts of square roots of the first 64 primaries, written in 32-bit format
def getInitialBlocks():
    sqrt_fractional_values = [
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19,
    ]
    res = list()
    for value in sqrt_fractional_values:
        res.append(format(value, "032b"))
    return res

# getting binary representation of initial value
def getBinaryMessage(input_value):
    binary_string = ''.join(format(ord(symb), '008b') for symb in input_value)
    return binary_string

# the initial message gets spitted in 512-bit blocks. 
# if the message is not long enough to fit in 512-bit block, then it gets padded with zeros
# 448-th bit of the last block is a separator '1' between the message and its length value
# last 64 bits of the last block contain the message length in binary
def getMessageBlocks(binary_string):
    # separator
    separator = '1'
    
    # message length in binary
    binary_length = bin(len(binary_string)).lstrip("0b")
    
    # padding
    bits_to_pad = 512 - len(binary_string + separator + binary_length) % 512
    res_string = binary_string + separator + '0' * bits_to_pad + binary_length
    
    # splitting into blocks
    blocks = [ res_string [i:i + 512] for i in range(0, len(res_string), 512) ]
    return blocks

# splitting the message block into 64 32-bit values. initially, each 512-bit block
# contains 16 32-bit values, so the other 48 need to be generated from those 16
def getMessageSchedule(block):
    # initial 16 values
    schedule = [ block [i:i + 32] for i in range(0, len(block), 32) ]

    # generating additional 48 values: each i-th value is defined as 
    # sigma1(schedule[i - 2]) + schedule[i - 7] + sigma0(schedule[i - 15]) + schedule[i - 16] 
    for i in range(16, 64):
        sum1 = sum(sigma1(schedule[i - 2]), schedule[i - 7])
        sum2 = sum(sigma0(schedule[i - 15]), schedule[i - 16])
        schedule.append(sum(sum1, sum2))
    
    return schedule

def getCompressedBlocks(message_blocks):
    compressed_blocks = getInitialBlocks()
    
    # processing each block of a message
    for block in message_blocks:
        message_schedule = getMessageSchedule(block)

        initial_compressed_blocks = compressed_blocks
        
        # compressing block
        for i in range(0, len(message_schedule)):
            sum1 = sum(SIGMA1(compressed_blocks[4]), choice(compressed_blocks[4], compressed_blocks[5], compressed_blocks[6]))
            sum2 = sum(message_schedule[i], sum(compressed_blocks[7], constants[i]))
            temp_word1 = sum(sum1, sum2)    
            
            temp_word2 = sum(SIGMA0(compressed_blocks[0]), majority(compressed_blocks[0], compressed_blocks[1], compressed_blocks[2]))

            new_first_value = sum(temp_word1, temp_word2)
            compressed_blocks = [new_first_value] + compressed_blocks[:7]
            updated_fifth_value = sum(compressed_blocks[4], temp_word1)
            compressed_blocks[4] = updated_fifth_value
    
        # last step: summing each value of compressed blocks with its initial value.
        # initial value of the first block is generated with getInitialBlocks() func,
        # initial value of any following i-th block is the value of (i - 1)-th block
        for i in range(0, len(compressed_blocks)):
            compressed_blocks[i] = sum(compressed_blocks[i], initial_compressed_blocks[i])

    return compressed_blocks

def getHashValue(compressed_blocks):
    res_hex_string = ""
    
    for i in range(0, len(compressed_blocks)):
        res_hex_string += format(int(compressed_blocks[i], 2), '08x')

    return res_hex_string

# main func
def getSHA256(input_value):
    binary_message = getBinaryMessage(input_value)
    #print("Message in binary:\n", binary_message)

    message_blocks = getMessageBlocks(binary_message)
    #print("512-bit message blocks:\n", message_blocks)

    compressed_blocks = getCompressedBlocks(message_blocks)
    #print("Compressed blocks:\n", compressed_blocks)

    hash_value = getHashValue(compressed_blocks)
    
    return hash_value


# driver code:

constants = getConstants()
# print("Constants:\n", constants)

if __name__ == "__main__":
    print("Value to be hashed: ", end = "")
    input_value = input()

    print("Hash value:", getSHA256(input_value))