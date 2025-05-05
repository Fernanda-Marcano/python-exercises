from pathlib import Path 

print('\n**********************************')
print('Contador de palabras en un archivo')
print('**********************************\n')

def count_word(text: str):
    return len(text.split())

ruta = Path(input('Ingrese la ruta completa del archivo: '))

if ruta.exists() and ruta.is_file:
    print('Se ha accedido al archivo correctamente')
    if ruta.stat().st_size == 0:
        print('El archivo se encuentra vacio')
    else:
        try:
            with ruta.open('r', encoding='utf-8') as file:
                reading = file.read()
                print(f'El archivo tiene {count_word(reading)} palabras')
        except IOError as e:
            print(f'Error. No se ha podido abrir el archivo. Detalles: {e}')
else:
    print('El archivo no se ha encontrado')