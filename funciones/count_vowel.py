print('========================================')
print("Programa que cuenta las vocales en una cadena dada")
print('========================================\n')


# Codigo original
""" def count_worl(text):
    vocals = 'aeiouAEIOU'
    suma = 0
    for letter in text:
        for vol in vocals:
            if vol == letter:
                suma += 1
    return suma """

#Codigo Optimizado
def count_vowels(text):
    vocals = "aeiouAEIOU"
    return sum(1 for letter in text if letter in vocals)  #Sum es una funcion generadora. Devuelve 1 cada vez que encuentra
    #una coincidencia

text = input('Ingrese una cadena de texto: ')
print(count_vowels(text))