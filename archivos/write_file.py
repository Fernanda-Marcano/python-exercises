""" Escribir en un archivo:  
	- Implementar un programa que escriba datos en un archivo nuevo. """

from pathlib import Path 

def write_file(ruta: str, name_file: str):
    file_path = ruta / name_file
    if ruta.exists() and ruta.is_dir():
        print('La ruta ingresada es correcta')
        if file_path.exists():
            print('El archivo ya existe. Se agregará contenido adicional.')
        else:
            print('Creando un nuevo archivo...')
        try: 
            with file_path.open('a', encoding='utf-8') as file:
                while True:
                    texto = input('Escriba los datos en el archivo (o escriba "q" para salir): ')
                    if texto.lower() == 'q':
                        break
                    file.write(texto + '\n')
        except IOError as e:
            print(f'Error. Ha ocurrido un error al abrir el archivo. Detalles: {e}')
    else:
        print('Error en la ruta ingresada')

ruta = Path(input('Ingrese la ruta de destino del archivo: '))
name_file = input('Ingrese el nombre del archivo: ')
write_file(ruta, name_file)