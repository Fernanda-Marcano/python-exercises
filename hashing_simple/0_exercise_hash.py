""" Crear un script que calcule el hash de un archivo """

import hashlib
from pathlib import Path

def calculator_hash(archivo):
    hash_func = hashlib.sha256() #Indica el tipo de algoritmo de hash
    with open(archivo, 'rb') as f: #Leer el archivo de forma binaria
        while chunk := f.read(8192): #Lee 8192 bytes del archivo en cada iteración. 
            hash_func.update(chunk)
    return hash_func.hexdigest()

archivo = Path('Ingrese la ruta del archivo que desea hashear')

print(calculator_hash(archivo))
