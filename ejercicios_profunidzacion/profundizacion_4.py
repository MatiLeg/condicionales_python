# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

palabra_1 = str(input('Palabra 1: '))
palabra_2 = str(input('Palabra 2: '))
palabra_3 = str(input('Palabra 3: '))

letrasPalabra_1 = len(palabra_1)
letrasPalabra_2 = len(palabra_2)
letrasPalabra_3 = len(palabra_3)

print('¿Como quiere ordenar las palabras?')
print('Presione "1" si desea ordenarlas alfabeticamente.')
print('Presione "2" si desea ordenarlas de mayor a menor por cantidad de caracteres.')

eleccion = int(input('Eleccion: '))

#Orden alfabetico
if eleccion == 1:
    if palabra_1 < palabra_2 and palabra_1 < palabra_3:
        if palabra_2 < palabra_3:
            print ('"{}", "{}", "{}"'.format(palabra_1, palabra_2, palabra_3))
        elif palabra_2 > palabra_3:
            print ('"{}", "{}", "{}"'.format(palabra_1, palabra_3, palabra_2))
            #
    elif palabra_2 < palabra_1 and palabra_2 < palabra_3:
        if palabra_1 < palabra_3:
            print ('"{}", "{}", "{}"'.format(palabra_2, palabra_1, palabra_3))
        elif palabra_1 > palabra_3:
            print ('"{}", "{}", "{}"'.format(palabra_2, palabra_3, palabra_1))
            #
    elif palabra_3 < palabra_1 and palabra_3 < palabra_2:
        if palabra_1 < palabra_2:
            print ('"{}", "{}", "{}"'.format(palabra_3, palabra_1, palabra_2))
        elif palabra_1 > palabra_2:
            print ('"{}", "{}", "{}"'.format(palabra_3, palabra_2, palabra_1))
# Orden de mayor a menor por cantidad de letras
elif eleccion == 2:
    if letrasPalabra_1 > letrasPalabra_2 and letrasPalabra_1 > letrasPalabra_3:
        if letrasPalabra_2 > letrasPalabra_3:
            print ('"{}", "{}", "{}"'.format(palabra_1, palabra_2, palabra_3))
        elif letrasPalabra_2 < letrasPalabra_3:
            print ('"{}", "{}", "{}"'.format(palabra_1, palabra_3, palabra_2))
            #
    elif letrasPalabra_2 > letrasPalabra_1 and letrasPalabra_2 > letrasPalabra_3:
        if letrasPalabra_1 > letrasPalabra_3:
            print ('"{}", "{}", "{}"'.format(palabra_2, palabra_1, palabra_3))
        elif letrasPalabra_1 < letrasPalabra_3:
            print ('"{}", "{}", "{}"'.format(palabra_2, palabra_3, palabra_1))
            #
    elif letrasPalabra_3 > letrasPalabra_1 and letrasPalabra_3 > letrasPalabra_2:
        if letrasPalabra_1 > letrasPalabra_2:
            print ('"{}", "{}", "{}"'.format(palabra_3, palabra_1, palabra_2))
        elif letrasPalabra_1 < letrasPalabra_2:
            print ('"{}", "{}", "{}"'.format(palabra_3, palabra_2, palabra_1))
            
