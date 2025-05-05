""" Eliminar líneas de archivo: 
	- Implementar un script que elimine líneas específicas de un archivo de texto. """

from pathlib import Path

def eliminar_linea():
    ruta = Path(input('\nIngrese la ruta, el nombre y sufijo del archivo: '))
    if ruta.exists() and ruta.is_file():
        try: 
            with ruta.open('r', encoding='utf-8') as archi:
                archivo = archi.readlines()
                if not archivo: 
                    print('\nEl archivo esta vacio, no hay lineas para eliminar')
                    return
                
                print(f'\nEste es el contenido del archivo: \n')
                for i, linea in enumerate(archivo):
                    print(f'{i+1}. {linea.strip()}')
                
                num_linea = int(input('\nIntroduzca el número de la linea que desea eliminar: ')) -1
                if 0 <= num_linea < len(archivo):
                    archivo.pop(num_linea)
                    with ruta.open('w', encoding='utf-8') as archi:
                        archi.writelines(archivo)
                    print(f'\nLa línea {num_linea + 1} ha sido eliminada correctamente.\n')
                else:
                    print("\nNúmero de línea fuera del rango. Inténtelo nuevamente.")
        except IOError as e:
            print(f'Error. No se pudo abrir el archivo. Detalles: {e}')
        except ValueError:
            print("\nError: La entrada debe ser un número válido.")
    else:
        print('La ruta ingresada no existe')

eliminar_linea()