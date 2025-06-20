#Contar cuántos archivos tienen permisos de solo lectura.

from pathlib import Path

def read_permission_file():
    dir = Path(input('Ingrese la ruta del directorio: '))
    count = 0
    if dir.exists() and dir.is_dir():
        for file in dir.iterdir():
            if oct(file.stat().st_mode) == '0o100644':
                count += 1
        return count
    else:
        return 'La ruta indicada no existe'

print('\n===============================================')
print('Contador de archivos con permisos de solo lectura')
print('===============================================\n')

print(f'Existen ({read_permission_file()}) archivos con el permiso de solo lectura en este directorio\n')

