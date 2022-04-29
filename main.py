import secrets
from time import sleep
from RSA import rsaModule

rsa = rsaModule()
m = rsa.constructMessage("placeholder text")
x = rsa.encrypt(m)
sleep(secrets.randbelow(5))
y = rsa.decrypt(x)
print(rsa.reconstructMessage(y))