# У якості завдання обрав реалізацію алгоритму шифрування Vigenere Cipher
# згідно з вказаним у описі до завдання прикладом https://cryptii.com/pipes/vigenere-cipher,
# алгоритм шифруватиме латинські обох регістрів літери (тобто, a-z та A-Z).
# Усі інші символи залишамутимуться без змін. 
# Ключ шифрування є регістро-незалежним, може включати лиже латинські літери 
 

# checking if the key contains only lowercase latin letters
def keyIsValid(key):
    for symb in key:
        if ord(symb) < ord('a') or ord(symb) > ord('z'):
            return False
    return True

# encrypting message with the key
def getCipher(message, key):
    cipher = ""
    runner = 0
    for symb in message:    
        shift = 0
        if ord('a') <= ord(key[runner % len(key)]) <= ord('z'):
            shift = ord(key[runner % len(key)]) - ord('a')
    
        if ord('a') <= ord(symb) <= ord('z'):
            ord_value = ord(symb) - ord('a') + shift
            cipher += chr(ord_value % 26 + ord('a'))
            runner += 1
            continue
        if ord('A') <= ord(symb) <= ord('Z'):
            ord_value = ord(symb) - ord('A') + shift
            cipher += chr(ord_value % 26 + ord('A'))
            runner += 1
            continue

        cipher += symb
    return cipher


print("Value to be encypted: ", end = "")
message = input()

print("Cipher key: ", end = "")
key = input()

# key uppercase letters get converted to lowercase
key = key.lower()

if keyIsValid(key) == False:
    print("The value contains forbidden character")
if keyIsValid(key) == True:
    print("Cipher:", getCipher(message, key))