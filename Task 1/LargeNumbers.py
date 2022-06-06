from random import randint
from datetime import datetime

# Part 1. Calculating & printing number of keys set as a bit sequence
for length in range (3, 13):
    # current length
    print(2 ** length, end="-bit sequence: ")
    print(2 ** (2 ** length))
    print('\n')
    
# Testing lengths are 3, 4, 5, 6, 7, 8 for Part 2 & 3 
for length in range (3, 13):
    # Part 2. Generating & printing random hex value of given length
    print('\n')
    print("Random ", end = "")
    print(2 ** length, end = "-bit key: ")
    str_length = int((2 ** length) / 4)
    # Random hex in range 0x10...0 -> 0xF...F
    rand_suffix = hex(randint(16 ** (str_length - 1), 16 ** str_length - 1))
    # Random symbol in range 0x0 -> 0xF
    rand_prefix = hex(randint(0, 15))
    # Merging to get key in range 0x0...0 -> 0xF...F
    rand_hex_key = rand_prefix
    for i in range (3, len(rand_suffix)):
        rand_hex_key = rand_hex_key + rand_suffix[i]
    print(rand_hex_key)

    # Part 3. Brute forcing hex values to find a match to rand_hex_key 
    start_time = datetime.now()
    for runner in range (16 ** (str_length - 1), 16 ** str_length):
        if hex(runner) == rand_hex_key:
            print("Execution time: ", end = "")
            print((datetime.now() - start_time).microseconds / 1000 + (datetime.now() - start_time).seconds * 1000, end = "ms")
    if str_length == 8:
        print('\n')