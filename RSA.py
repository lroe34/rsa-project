from Crypto.Util.number import getPrime, inverse

class rsaModule:
    def __init__(self):
        self.p = getPrime(8)
        self.q = getPrime(8)
        self.n = self.p*self.q
        self.euler = (self.p-1)*(self.q-1)
        self.e =  65537
        self.d = inverse(self.e,self.euler)
    def constructMessage(self, message):
        asciiMessage = []
        for x in message:
            if len(str(ord(x))) == 2:
                asciiMessage.append(int("0"+str(ord(x))))
            else:
                asciiMessage.append(int(ord(x)))
        print(asciiMessage)
        return asciiMessage


    def encrypt(self,m):
        encrypted = []

        for num in m:
            encrypted.append(num**self.e%self.n)
            #rudementary defense against timing attack

        print('Encryption Complete\n')
        print('Encrypted Message: ',encrypted)
        print('\nDecryption Key:', self.d)
        return encrypted

    def decrypt(self,encrypted):
        decrypted = []
        
        print(encrypted)
        for num in encrypted:
        #rudementary defense against timing attack

            decrypted.append(num**self.d%self.n)
        print('\ndec = ',decrypted)
        return decrypted

    def reconstructMessage(self,decrypted):
        message = ''
        for char in decrypted:
            message = message+chr(int(char))
        return message

