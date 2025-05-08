""" Generador de contraseñas:
    - Desarrolla una función que genere contraseñas seguras"""

import string
import random

def generator():
    letters = [random.choice(string.ascii_letters) for _ in range(6)]
    numbers = [random.choice(string.digits) for _ in range(2)]
    simbols = [random.choice(string.punctuation)]
    
    password = ''.join(letters + numbers + simbols)

    return password


print(generator())

