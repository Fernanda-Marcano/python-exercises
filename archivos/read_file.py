from pathlib import Path

try:
    filename = Path(input('Ingrese la ruta y nombre del archivo: ')) 
    if filename.exists() and filename.is_file(): #Valida si el archivo existe y si es un file
        if filename.stat().st_size == 0: #Para verificar si el archivo esta vacio
            print('El archivo se encuentra vacio')
        else:
            print('La ruta del archivo es correcta')
            with filename.open('r', encoding='utf-8') as file:
                lectura = file.read()
                print(f'\n{lectura} \n')
    else:
        print(f'Error: La ruta "{filename}" no existe')
except IOError as e:
    print(f"Error: Hubo un problema al leer el archivo. Detalles {e}")

