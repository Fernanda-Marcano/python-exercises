class Book:
    def __init__(self, titulo: str, autor: str, fecha_publicacion: str):
        self.titulo = titulo
        self.autor = autor
        self.fecha_publicacion = fecha_publicacion
        self.prestado = False  
        self.solicitante = None
        self.fecha_retiro = None
    
    def prestamo(self):
        if not self.prestado:
            self.solicitante = input('Ingrese el nombre del solicitante: ')
            self.fecha_retiro = input('Ingrese la fecha de retiro del libro: ')
            self.prestado = True
            return f'Libro prestado a {self.solicitante} el {self.fecha_retiro}'
        else:
            return f'El libro ya está prestado a {self.solicitante}. No está disponible.'
    
    def devolucion(self):
        if self.prestado:
            fecha_entrega = input('Ingrese la fecha de entrega: ')
            self.prestado = False
            self.solicitante = None
            self.fecha_retiro = None
            return f'Libro devuelto el {fecha_entrega}. Ahora está disponible.'
        else:
            return 'El libro no está prestado actualmente.'
    
    def __str__(self) -> str:
        estado = "Disponible" if not self.prestado else f'Prestado a {self.solicitante}'
        return f'Título: {self.titulo}\nAutor: {self.autor}\nFecha de publicación: {self.fecha_publicacion}\nEstado: {estado}'

def menu():
    print('''
    Simulación de libro:
    1.Información del libro
    2.Prestar libro
    3.Devolver libro
    q.Salir''')

book1 = Book('Harry Potter', 'J.K Rowling', '2007')

while True:
    menu()
    option = input('Seleccione una opcion: ')
    if option == '1':
        print('\n==============================')
        print(book1)
        print('==============================')
    elif option == '2':
        print(f'{book1.prestamo()}')
    elif option == '3':
        print(f'{book1.devolucion()}')
    else:
        break