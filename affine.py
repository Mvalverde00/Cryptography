def encode(message, a, b):
    cipher_text = ""
    for char in message:
        char = chr(((ord(char)-97)*a + b)%26 + 97)
        cipher_text += char
    return cipher_text

def decode(cipher_text, ai, b):
    message = ""
    for char in cipher_text:
        char = chr( ((ord(char)-97 - b)*ai)%26 + 97 )
        message += char
    return message

def restrict(message):
    return message.replace(" ", "").lower()

def print_stats(message, a, b):
    print("Original message: {} ".format(message))
    print("(a,b): ({},{})".format(a, b))
    print("Encoded message: {}".format(encode(restrict(message),a,b)))
def print_stats_decode(cipher, ai, b):
    print("Encoded message: {} ".format(cipher))
    print("(a inverse, b): ({},{})".format(ai, b))
    print("Decoded message: {}".format(decode(restrict(cipher),ai,b)))

## Consecutive Affine demonstration
print_stats("This is a secret message", 5, 7)
print_stats("yqvtvthtbrobypbtthlb", 11, 15)
print_stats("This is a secret message", 55, 77+15)

## Sample decode
print_stats_decode("pshxapuexcgapuspexcgolsqpehbooh", 9, 2)

print_stats("Hows it goi never gonna give you up",5,11) # A proper rick roll

# a1 = 5, b1 = 7
# a2 = 11, b2 = 15

# a = 55, b = 77 + 15
