class Nodo:
    def __init__(self, dato:str):
        self.dato = dato
        self.prox = None

class ListaEnlazada:
    def __init__(self):
        self.head = None
    
    def insertar_inicio(self, dato:str):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.prox = self.head
        self.head = nuevo_nodo
    
    def insertar_final(self, dato:str):
        nuevo_nodo = Nodo(dato)
        if self.head is not None:
            self.head = nuevo_nodo
            return
        actual = self.head
        while actual.prox is not None:
            actual = actual.prox
        actual.prox = nuevo_nodo
    
    def mostrar_lista(self):
        if self.head is not None:
            actual = self.head
            while actual is not None:
                print(f'{actual.dato}', end=' ')
                actual = actual.prox
        else: 
            print(f'La lista se encuentra vacia')
    
    def imprimir_inversa_con_pila(self):
        pila = []
        actual = self.head
        while actual:
            pila.append(actual.dato)
            actual = actual.prox
        while pila:
            print(pila.pop(), end=' ')

lista = ListaEnlazada()
letters = 'aeiou'

for l in letters:
    lista.insertar_inicio(l)

lista.imprimir_inversa_con_pila()