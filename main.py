import secrets
from time import sleep
from RSA import rsaModule

for x in range(100):
    rsa = rsaModule()
    message = ('p')
    m = rsa.constructMessage(message)
    x = rsa.encrypt(m)
#    sleep(secrets.randbelow(5))
    y = rsa.decrypt(x)
    print(rsa.reconstructMessage(y))