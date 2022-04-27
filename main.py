import secrets
from time import sleep
from Crypto.Util.number import getPrime, GCD, getRandomInteger, inverse

#these two functions turn the message from ascii to decimal and then back to ascii again after decryption 
def buildMessage(message):
    asciiMessage = []
    for x in message:
        if len(str(ord(x))) == 2:
            asciiMessage.append(int("0"+str(ord(x))))
        else:
            asciiMessage.append(int(ord(x)))
    print(asciiMessage)
    return asciiMessage

def rebuildMessage(decrypted):
    message = ''
    for char in decrypted:
        message = message+chr(int(char))
    return message

#use the getPrime from Cryptodome to generate two prime numbers of N-bits
p = getPrime(8)
q = getPrime(8)

m = buildMessage(str(input("Message to Encrypt: ")))
n = p*q
euler = (p-1)*(q-1)


def findE(bits):
        num = getRandomInteger(bits)
        while GCD(euler,num) != 1:
            num = getRandomInteger(bits)
        return num




e = findE(5)
d = inverse(e,euler)


#key calculations, this is the most computationally expensive part
encrypted = []
for num in m:
    encrypted.append(num**e%n)
    #rudementary defense against timing attack
    sleep(secrets.randbelow(5))
print('Encryption Complete\n')
print('Encrypted Message: ',encrypted)

decrypted = []
for num in encrypted:
    #rudementary defense against timing attack
    sleep(secrets.randbelow(5))
    decrypted.append(num**d%n)

print('dec = ',decrypted)
print('Decrypted Message: ',rebuildMessage(decrypted))



#lots of print statements of every variable for debugging purposes

#print(euler)
#print('p = ',p)
#print('q = ',q,'\n')
#print ('e = ', e)
#print('d = ',d)
#print('euler = ', euler, '\n')
#print('m = ', m)
#print(decrypted)
