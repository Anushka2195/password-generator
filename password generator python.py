import random
import array

MAX_LEN = 8

DIGITS = ['0', '1', '3', '4', '5', '6', '7', '8', '9']
CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', '*', '_']

COMBINED_LIST = DIGITS + CHARACTERS + SYMBOLS

rand_digit = random.choice(DIGITS)
rand_character = random.choice(CHARACTERS)
rand_symbol = random.choice(SYMBOLS)

temp_pass = rand_digit + rand_digit + rand_character + rand_character + rand_character + rand_symbol + rand_symbol

temp_pass = temp_pass + random.choice(COMBINED_LIST)

print(temp_pass)
