import os
import hashlib
from pathlib import Path

#Clase que convierte los archivos en hash
class Hash:
    @staticmethod
    def calcular_hash_archivo(archivo, metodo='sha256'):
        try:
            hash_func = hashlib.new(metodo)
            with open(archivo, 'rb') as f:
                while chunk := f.read(8192):
                    hash_func.update(chunk)
        except Exception as e:
            print(f'Ha ocurrido un error. Detalles: {e}')
        return hash_func.hexdigest()

#Busca archivos duplicados en el directorio
def encontrar_duplicados(directorio):
    for arch in directorio.rglob('*.jpg'):
        hash_archivo = Hash.calcular_hash_archivo(arch)
        if hash_archivo in hashes:
            duplicados.append((hash_archivo, arch))
        else:
            hashes[hash_archivo] = arch

#Elimina los archivos duplicados
def eliminar_archivos_duplicados(duplicados: list):
    for archivo in duplicados:
        archivo[1].unlink()

def menu():
    print('\nSeleccione alguna de las siguientes opciones: ')
    print('1.Verificar si existen archivos duplicados en el directorio ingresado.')
    print('2.Eliminar archivos duplicados del directorio.')
    print('3.Salir\n')

def limpiar_consola():
    os.system('cls')

directorio = Path(input('Ingrese el directorio que desea examinar: '))

hashes = {}     #Almacena los hashes creados
duplicados = []     #Almacena los archivos duplicados

cent = True #Control del bucle
while cent:
    menu()
    
    opcion = input('Ingrese una opción: ')
    limpiar_consola()
    if opcion == '1':
        encontrar_duplicados(directorio)
        print('########################################')
        if duplicados:
            print(f'Se han encontrado {len(duplicados)} archivos duplicados')
            for dup in duplicados:
                print(f'\t{dup[1]}')
        else:
            print(f'No se han encontrado archivos duplicados')
        print('########################################')
    elif opcion == '2':
        print('########################################')
        if not duplicados:
            print('No hay archivos duplicados para eliminar')
        else:
            validar_respuesta = input('Está seguro que desea eliminar los archivos?(s/n): ').lower()
            if validar_respuesta == 's':
                eliminar_archivos_duplicados(duplicados)
                print('Archivos eliminados correctamente')
            else:
                continue
        print('########################################')
    elif opcion == '3':
        print('########################################')
        print('Nos vemos pronto')
        print('########################################')
        cent = False
    else:
        print('La opción ingresada no es válida')