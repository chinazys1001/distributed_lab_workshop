# converting hex digit to decimal number 
def hexToDec (hex_value):
    ascii_value = ord(hex_value)
    if ascii_value < 58: return ascii_value - 48
    if ascii_value < 71: return ascii_value - 55
    return ascii_value - 87

# converting 1 byte (<=> 2 hex) to decimal number
def getByteDecValue(hex1, hex2):
    value1 = hexToDec(hex1)
    value2 = hexToDec(hex2)
    return 16 * value1 + value2

print("Value: ", end = "")
# if value is too large for console input, paste it below manually instead of "input()" 
hex_string = input() # "large string goes here"
hex_string = hex_string[2:] # removing 0x identifier
if (len(hex_string) % 2 > 0):
    hex_string = '0' + hex_string # adding leading zero if needed
number_of_bytes = int(len(hex_string) / 2)
little_endian = 0    
big_endian = 0

print("Number of bytes: ", end = "")
print(number_of_bytes)

# processing each byte
for i in range (0, number_of_bytes):
    ltr_byte_dec_value = getByteDecValue(hex_string[2 * i], hex_string[2 * i + 1])
    little_endian += ltr_byte_dec_value * pow(256, i)
    rtl_byte_dec_value = getByteDecValue(hex_string[2 * number_of_bytes - 2 * i - 2], hex_string[2 * number_of_bytes - 2 * i - 1])
    big_endian += rtl_byte_dec_value * pow(256, i)

print("Little-endian: ", end = "")
print(little_endian)
print("Big-endian: ", end = "")
print(big_endian)