# Tuples = estructura de datos orrdenada, A diferencia de las listas, las tuplas no pueden modificarse una vez creadas, lo que significa que no se pueden agregar, eliminar ni reasignar sus elementos.
# Esta inmutabilidad hace que las tuplas sean más eficientes en términos de memoria y velocidad de acceso en comparación con las listas.

my_tuples = tuple()
my_other_tuple = ()

my_tuples = (35, 1.77, "Andres", "Lopez", "Andres")
my_other_tuple = (35, 60, 30)

print(my_tuples)
print(type(my_tuples))

print(my_tuples[0])
print(my_tuples[-1])

print(my_tuples.count("Andres"))
print(my_tuples.index("Lopez")) #nos dice el indice, o sea la posición en donde se encuentra
print(my_tuples.index("Andres"))

# my_tuples[1] = 1.80 = Error, no se puede cambiar una tupla ya creada

my_sum_tuple = my_tuples + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

# para transformar una tupla a una lista:
my_tuples = list(my_tuples)
print(type(my_tuples))

my_tuples[4] = "MoureDev"
my_tuples.insert(1, "Azul")
print(my_tuples)

# Para transformarla nuevamente a una tupla:
my_tuples = tuple(my_tuples)
print(type(my_tuples))

# del my_tuples[2] = Esto daria un error, no se puede eliminar un elemento de uno en uno
del my_tuples #eliminamos la tupla 
# print(my_tuples) Da error porque acabamos de eliminar la tupla