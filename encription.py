import random
import string

chars = string.punctuation + string.ascii_letters + string.digits
chars = list(chars)
key = chars.copy()
random.shuffle(key)
crypted_text = ""

plain_text = input("message to encrypt")
for letter in plain_text:
    index = chars.index(letter)
    crypted_text += key[index]
print(crypted_text)



crypted_text = input("message to encrypt")
for letter in crypted_text:
    index = key.index(letter)
    plain_text += chars[index]
print(plain_text)










