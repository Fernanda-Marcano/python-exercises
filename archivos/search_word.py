""" 	Buscar palabra en archivo: 
	- Crear un programa que busque una palabra específica en un archivo. """

from pathlib import Path

def buscar_palabra(palabra: str):
    archivo = Path(input('Introduzca la ruta y nombre del archivo: '))
    
    if archivo.exists() and archivo.is_file():
        try: 
            with archivo.open('r', encoding='utf-8') as archi:
                lineas = archi.readlines()
                coincidencias = [i + 1 for i, line in enumerate(lineas) if palabra.lower() in line.lower()]
                if coincidencias:
                    cantidad = sum(line.lower().count(palabra.lower()) for line in lineas)
                    print(f'La palabra "{palabra}" aparece {cantidad} veces en el archivo.')
                    print(f'Se encuentra en las líneas: {coincidencias}\n')
                else:
                    print(f'No se encontró la palabra "{palabra}" en el archivo\n')
        except IOError as e: 
            print(f'Error. No se pudo abrir el archivo. Detalles: {e}')

buscar_palabra(input('\nIngrese la palabra que desea buscar en el archivo: '))