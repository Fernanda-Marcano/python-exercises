import hashlib
from pathlib import Path

#Funcion que calcula el hash de un archivo
def calculator_hash(archivo, metodo='sha256'):
    hash_func = hashlib.new(metodo)
    with open(archivo, 'rb') as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()

#Guarda la ruta del directorio
directorio = Path(input('Ingrese la ruta del directorio que desea examinar: '))

#Diccionario que almacenara los hashes como clave y las rutas como valor
hashes = {}
duplicados = []

for arch in directorio.iterdir():
    #Le calculamos el hash a cada uno de los archivos
    hash_cal = calculator_hash(arch)
    if hash_cal in hashes: 
        duplicados.append((hash_cal, arch))
    else:
        hashes[hash_cal] = arch

while True:
    print('Seleccione una de las siguientes opciones: ')
    print('1. Verificar si hay archivos duplicados')
    print('2. Eliminar archivos duplicados')
    print('3. Salir')
    option = int(input(''))
    
    if option == 1:
        print(f'\nSe han encontrado {len(duplicados)} archivos duplicados\n')
        for dup in duplicados:
            print(f'Hash: {dup[0]} - Ubicacion: {dup[1]}')
        print()
    elif option == 2:
        for dup in duplicados:
                dup[1].unlink()
        print(f'Se han eliminado {len(duplicados)} archivos duplicados')
    else:
        break