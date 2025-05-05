""" Copiar contenido de archivos: 
	- Escribir un script para copiar contenido de un archivo a otro.
    Agregue interacción con el usuario y las validaciones necesarias 
    para su correcta ejecución"""

from pathlib import Path
import shutil

def copiar_archivo():
    ruta_original = Path(input('Ingrese la ruta completa del archivo: '))
    ruta_copia = Path(input('Ingrese la ruta donde desea copiar el archivo: '))
    
    if ruta_original.exists() and ruta_original.is_file():
        if ruta_copia.is_dir():
            ruta_copia = ruta_copia / ruta_original.name
        try:
            shutil.copy(ruta_original, ruta_copia)
            print('Archivo copiado correctamente')
            
            with ruta_copia.open('r', encoding='utf-8') as archivo:
                print(f'\nContenido del archivo copiado: \n{archivo.read()}\n')
        except shutil.Error as e:
            print(f'Error en al copiar el archivo: {e}')
        except IOError as e:
            print(f'Error en la entrada/salida del archivo: {e}')
    else:
        print('No se pudo copiar el archivo, la ruta de origen no existe o el archivo no es válido')

copiar_archivo()