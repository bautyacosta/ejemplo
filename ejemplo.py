import random 
import string

print("generador de claves!")

chars = string.ascii_letters + string.digits + string.punctuation
password = ""
lenght = 10

for _ in range(lenght):
    password = password + random.choice(chars)

print ("la contraseña es ", password)