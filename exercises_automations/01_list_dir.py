#Crear un script que liste todos los archivos .txt de un directorio.

from pathlib import Path

def list_file_dir():
    name_dir = Path(input('Ingrese la ruta del directorio: '))
    exten = input('Ingrese la extencion de los archivos que desea listar: ')
    if name_dir.exists() and name_dir.is_dir():
        try:
            for file in name_dir.glob('*'+exten):
                print(f'\t{file}')
            else:
                print(f'No hay archivos con la extension {exten} en este directorio')
        except Exception as e:
            print(f'Se ha producido un error en la ejecucion. Detalles {e}')
        except FileNotFoundError:
            print('No se ha encontrado')
    else:
        print('No se pudo acceder a la ruta indicada')

print('\n==========================================')
print('Programa que lista e indica la cantidad de archivos con la extension indicada')
print('==========================================\n')

list_file_dir()