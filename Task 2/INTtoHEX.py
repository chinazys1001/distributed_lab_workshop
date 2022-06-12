# converting decimal remainder to hex digit 
def decToHex (dec_value):
    if (dec_value > 9): return chr(55 + dec_value)
    return  chr(48 + dec_value)

# converting big-endien to little-endien
def getReversedBytes (hex_value):
    reversed_bytes = ""
    number_of_bytes = int(len(hex_value) / 2)
    for i in range(0, number_of_bytes):
        reversed_bytes += hex_value[2 * (number_of_bytes - i) - 2] + hex_value[2 * (number_of_bytes - i) - 1]
    return reversed_bytes

print("Value: ", end = "")
dec_value = int(input()) # replace with large integer manually if needed
hex_value = ""

# converting input dec value to hex
while dec_value > 0:
    hex_value = decToHex(int(dec_value % 16)) + hex_value
    dec_value = dec_value // 16

# case the input value was written in little-endian order
print("Hex value of little-endian value: ", end = "0x")
if (len(hex_value) % 2 != 0): hex_value = '0' + hex_value # adding leading zero to pad last byte
print(getReversedBytes(hex_value))

# case the input value was written in big-endian order
print("Hex value of big-endian value: ", end = "0x")
print(hex_value)