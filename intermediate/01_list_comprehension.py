# list comprehension = es una forma compacta de crear listas en Python a partir de un iterable, aplicando una expresión y, opcionalmente, una condición.
#Recorre un iterable, evalúa cada elemento, aplica una operación y agrega el resultado a una nueva lista, todo en una sola línea.

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]

# rango = secuencia de valores comprendidos entre un inicio y un fin.
my_range = range(8)
print(my_range)
print(list(my_range))

my_lilst = [i + 1 for i in range(8)]
print(my_lilst)

my_lilst = [i * 2 for i in range(8)]
print(my_lilst)

def sum_five(number):
    return number + 5
my_lilst = [sum_five(i) * i for i in range(8)]
print(my_lilst)

#O sea es una forma compacta y expresiva de crear listas a partir de: iteración(for), condiciones(if), transformación de datos
#Ejemplos: 

#1 Transformar datos (uso MÁS común) (cuando necesitas modificar cada elemento de una colección)
#Numeros al cuadrado
numeros = [1, 2, 3, 4]
cuadrados = [n**2 for n in numeros]
print(cuadrados)

#2 Filtrar elementos (quedarte solo con lo que cumple una condición)
#Solo numeros pares
pares = [n for n in numeros if n % 2 == 0]

#3 Transformar + filtrar (Muy usado en procesamiento de texto y datos)
#Longitud de palabras largas
palabras = ["hola", "programación", "python", "sol"]
largas = [len(p) for p in palabras if len(p) > 4]

#Convertir texto a minúsculas
nombres = ["Ana", "JUAN", "PeDro"]
normalizados = [n.lower() for n in nombres]


"""
Cuándo NO usar list comprehension:
    Si tiene muchas condiciones
    Si es difícil de leer
    Si hay lógica compleja

Regla práctica: 
    Si no se entiende en 3 segundos, usa for normal
"""


