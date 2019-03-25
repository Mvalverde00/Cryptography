def encode(message, a, b):
    cipher_text = ""
    for char in message:
        char = chr(((ord(char)-97)*a + b)%26 + 97)
        cipher_text += char
    return cipher_text

def restrict(message):
    return message.replace(" ", "").lower()

def print_stats(message, a, b):
    print("Original message: {} ".format(message))
    print("(a,b): ({},{})".format(a, b))
    print("Encoded message: {}".format(encode(restrict(message),a,b)))

print_stats("This is a secret message", 55, 77+15)
# a1 = 5, b1 = 7
# a2 = 11, b2 = 15

# a = 55, b = 77 + 15
