def base(message, passphrase, mode):
    if mode == 'e':
        mult = 1
    elif mode == 'd':
        mult = -1
    else:
        raise Error
    
    key = [ord(char)-97 for char in passphrase]
    
    new = ""
    
    for i, char in enumerate(message):
        char = chr((ord(char)-97 + mult*key[i%len(key)])%26 + 97)
        new += char

    return new

def restrict(message):
    return message.lower().replace(" ", "")

def encode(message, passphrase):
    return base(restrict(message), restrict(passphrase), 'e')
def decode(message, passphrase):
    return base(restrict(message), restrict(passphrase), 'd')

def print_stats(message, key):
    print("Original message: {} ".format(restrict(message)))
    print("key: {}".format(restrict(key)))
    print("Encoded message: {}".format(encode(restrict(message),restrict(key))))

def print_stats_decode(message, key):
    print("Encoded message: {} ".format(restrict(message)))
    print("key: {}".format(restrict(key)))
    print("Decoded message: {}".format(decode(restrict(message),restrict(key))))
    
print_stats("Math seminar is the best", "Valve")
