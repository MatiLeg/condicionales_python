# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

if texto_1 > texto_2:
    print('"{}" es mayor alfabeticamente que "{}"'.format(texto_1, texto_2))
else:
    print ('"{}" es mayor alfabeticamente que "{}"'.format(texto_2, texto_1))

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

if len(texto_1) > len(texto_2):
    print('"{}" tiene la mayor cantidad de letras'.format(texto_1))
elif len(texto_1) < len(texto_2):
    print('"{}" tiene la mayor cantidad de letras'.format(texto_2))
else:
    print('Tienen la misma cantidad de letras.')

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

if texto_1[0] > texto_2[0]:
    print('{} es mayor a {}'.format(texto_1[0], texto_2[0]))
elif texto_1[0] < texto_2[0]:
    print('{} es mayor a {}'.format(texto_2[0], texto_1[0]))
else:
    print('Las dos letras iniciales son iguales.')


copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

if copia_texto_1 == texto_1:
    print('copia_texto_1 es igual a texto_1')

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

if copia_texto_1 != texto_2:
    print('copia_texto_1 es distinta a texto_2')
