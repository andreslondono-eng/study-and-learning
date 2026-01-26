# sets = una estructura de datos que almacena una colección desordenada de elementos únicos, lo que significa que no permite duplicados
# Los sets son mutables, A diferencia de las listas, los sets no mantienen un orden específico ni están indexados, por lo que no se puede acceder a sus elementos mediante índices
# "del" es para eliminar completamente 

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #inicialmente es un diccionario

my_other_set = {"Andres", "Lopez", 35}
print(type(my_other_set))

print(len(my_other_set))

# print(my_other_set[0]) = Asi no es, esto da ERROR
my_other_set.add("MoureDev") #agregar elementos (como el set es una lista desordenada da igual si lo agrega al principio o al final)
print(my_other_set)

# Sintaxis para comprobar si un elemento existe dentro de un set
print("Andres" in my_other_set)
print("Andes" in my_other_set)

my_other_set.remove("Andres") #Eliminar elementos con el .remove
print(my_other_set)

my_other_set.clear() #Borra todos los elementos del set
print(my_other_set)

del my_other_set #Eliminación completa del set
# print(my_other_set) = Esto da ERROR porque ya fue borrado

my_set = {"Andres", "Lopez", 35}
my_list = list(my_set)
print(type(my_list))
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

# para unir sets usamos la función .union:
my_new_set = my_set.union(my_other_set)
#recordar que los sets no haceptan datos repetidos, por eso los primeros union no funcíonan:
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"})) #Tener el cuenta que el union solo es en el print, no lo almacenamos en una variable

# el difference es para obtener un conjunto que excluyendo el o los datos de la "variable" que le pasamos:
print(my_new_set.difference(my_set))












