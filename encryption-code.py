import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
keys = chars.copy()

random.shuffle(keys)
print(f"Chars: {chars}")
print(f"Keys : {keys}")

plain_text = input("Enter the message to encrypt: ")
cyper_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cyper_text += keys[index]

print(f"Plain Text: {plain_text}")
print(f"Cyper Text: {cyper_text}")