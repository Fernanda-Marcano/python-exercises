#Usar pathlib para cambiar permisos de archivos a lectura/escritura.

from pathlib import Path
import os

def change_permission_file():
    ruta = Path(input('Ingrese la ruta completa del archivo: '))
    if ruta.exists() and ruta.is_file():
        try:
            os.chmod(ruta, 0o644)
            print(f'Permisos establecidos: {oct(ruta.stat().st_mode)}')
        except Exception as e:
            print(f'Ha ocurrido un error. Detalles: {e}')
    else:
        print('La ruta ingresada no existe')

change_permission_file()
