""" Clase Usuario con Autenticación Crea una clase Usuario con 
    atributos nombre y contraseña. Implementa un método autenticar(contraseña_ingresada) 
    que valide si la contraseña ingresada es correcta. """  

class Usuario:
    def __init__(self, nombre:str, contrasena:str):
        self.nombre = nombre
        self.contrasena = contrasena
    
    def autenticar(self, password:str):
        if self.contrasena.lower() == password.lower():
            return f'Usuario autenticado correctamente'
        else:
            return f'La contraseña ingresada no es correcta'


user1 = Usuario('Fernanda', 'Harry9347')
print(user1.autenticar('Harry 9347'))