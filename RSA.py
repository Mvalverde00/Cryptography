"""
This project was built specifically for class, and does not meet normal RSA requirements.
The charset is restricted to a-z (0-25), and the blocksize is 3 characters
"""

class RSA():

    BLOCKSIZE = 4 # Number of chars in a given block

    
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def encrypt(message, e, n):
        bin_e = str(bin(e))[2:]
        M = RSA.message_to_int(message) # array of ints

        cipher_text = []

        # Split our message up into block
        full_blocks = len(M) // RSA.BLOCKSIZE
        remainder = len(M) % RSA.BLOCKSIZE

        for i in range(full_blocks):
            m = int("".join([str(M[i*RSA.BLOCKSIZE+j]).zfill(2) for j in range(RSA.BLOCKSIZE) ]))
            
            C = 1
            for j in range(len(bin_e)):
                C = ((C*C) % n)
                if int(bin_e[j]) == 1:
                    C = ((C*m)%n)
            cipher_text.append(C)
            
        if remainder != 0:
            m = [str(M[RSA.BLOCKSIZE*full_blocks+j]).zfill(2) for j in range(remainder)]
            for j in range(RSA.BLOCKSIZE-remainder):
                m.append("00")
            m = int("".join(m))

            C = 1
            for j in range(len(bin_e)):
                C = ((C*C) % n)
                if int(bin_e[j]) == 1:
                    C = ((C*m)%n)
            cipher_text.append(C)
            
        return cipher_text
    
    def decrypt(self, cipher_text):
        message = []
    
        for j, block in enumerate(cipher_text):
            
            bin_d = str(bin(self.d))[2:]
            M = 1

            for i in range(len(bin_d)):
                M = ((M*M) % self.n)
                if int(bin_d[i]) == 1:
                    M = ((M*block)%self.n)
                    
            message.append(str(M).zfill(self.BLOCKSIZE*2))

        return RSA.int_to_message(message)
        
    def message_to_int(message):
        message = message.replace(" ", "")
        message = message.lower() # We will only be dealing with charset (a-z)

        M = [(ord(char)-97) for char in message] # Convert to int, scale range to 0-25
    
        return M
        
    def int_to_message(M):
        message = ""

        for block in M:
            for i in range(0,RSA.BLOCKSIZE*2,2):
                the_int = int(block[i] + block[i+1])
                message += chr(the_int + 97)
        return message

if __name__ == "__main__":

    ints = """1096437423 0767457076 1935664384 0720266424 0258812901 0444046729 1785741988 0861588844 1076149385 0519431291 0444046729 1785741988 1118762727 0923933524 0854697562 0928218436 1297924026""".replace("\n", " ").split()
    
    ints = [int(i) for i in ints]

    a = RSA(2219818109, 468418285)
    print(a.decrypt(ints))

