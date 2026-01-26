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




















