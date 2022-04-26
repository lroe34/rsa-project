from random import randrange
from time import sleep
from Crypto.Util.number import getPrime, GCD, getRandomInteger, inverse

#the length of q,p, e, and d default to 16 bits for computational speed, but can be changed with this value:
bits = 16

#these two functions turn the message from ascii to decimal and then back to ascii again after decryption 
def buildMessage(message):
    asciiMessage = []
    for x in message:
        if len(str(ord(x))) == 2:
            asciiMessage.append(str("0"+str(ord(x))))
        else:
            asciiMessage.append(str(ord(x)))
    string = asciiMessage[0]
    asciiMessage.remove(string)
    for item in asciiMessage:
        string = string+item
    return int(string)

def rebuildMessage(decrypted):
    if len(decrypted)%2 != 0:
        decrypted = str('0'+decrypted)
    message = []
    letters = ''
    string = str(decrypted)
    i = 0
    while i < len(str(decrypted)):
        message.append(string[i:i+3])
        i+=3
    for x in message:
        num = chr(int(x))
        letters += num
    return letters

#use the getPrime from cryptodome to generate two prime numbers of N-bits
p = getPrime(bits)
q = getPrime(bits)

m = buildMessage(str(input("Message to Encrypt: ")))
n = p*q
euler = (p-1)*(q-1)


def findE(bits):
        num = getRandomInteger(bits)
        while GCD(euler,num) != 1:
            num = getRandomInteger(bits)
        return num

#rudementary defense againt timing attack
sleep(randrange(10))


e = findE(bits)
d = inverse(e,euler)

#key calculations, this is the most computationally expensive part
exp = m**e
encrypted = exp%n
dexp = encrypted**d
decrypted = dexp%n


#lots of print statements for every variable for debugging purposes, the important ones are un-commmented 
print('Encryption Complete\n')
#print(euler)
#print('p = ',p)
#print('q = ',q,'\n')
#print ('e = ', e)
#print('d = ',d)
#print('euler = ', euler, '\n')
#print('m = ', m)
print('Encrypted Message: ',encrypted)
#print('dec = ',decrypted)
#print(decrypted)
print('Decrypted Message: ',rebuildMessage(str(decrypted)))