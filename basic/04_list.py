# List = Colección ordenada y mutable de elementos que puede contener datos de diferentes tipos, como números, cadenas, objetos o incluso otras listas.


my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list =[35, 1.77, "Andres", "Lopez",]

print(type(my_list))
print(type(my_other_list))


print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
# .count retorna el numero de veces que esta un valor (como tenemos 2 veces 30 en la lsta .count nos devuelve un 2)
print(my_list.count(30))

age, height, name, surname = my_other_list #Se necesita desempaquetar todos los elementos para funcionar, si solo se definen 3 no funcionaria
print(name) 

print(my_list + my_other_list)#suma las 2 listas

my_other_list.append("Nuevo dato")#Insertamos un nuevo elemento al final
print(my_other_list)

my_other_list.insert(1, "Rojo")#Insertar en una posición especifica
print(my_other_list)

my_other_list[1] = "Azul" #Estamos cambiando el indice 1 que era "Rojo" por "azul"
print(my_other_list)

my_other_list.remove("Azul")#Remover el elemento que le pasemos, o sea nosotros debemos de saber que existe
print(my_other_list)

my_list.remove(30)#Solo remueve le primer elemento que coincide, por eso sigue habiendo un 30
print(my_list)


print(my_list.pop())#Quita el ultimo elemento, en este caso el 17 y con el print vemos que tambien nos lo retorna
print(my_list)

my_poop_element = my_list.pop(2) #Asi podemos guardar el elemento que estamos eliminando
print(my_poop_element)
print(my_list)

# Si queremos eliminar completamente el elemento sin que nos lo devuelva usamos el "del":
del my_list[2]
print(my_list)

my_new_list = my_list.copy() #crea una copia
print(my_list)

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse() #Para darle la vuelta a la lista
print(my_new_list)

my_new_list.sort() #sort(clasifica/ordena) podemos indicar criterios para ordenar (si no lo indicamoscomo de todas formas lo organizara como pueda)
print(my_new_list)

# Sublistas: para ver los elementos entre dos posiciones 
print(my_new_list[1:2])
print(my_new_list[1:3])


my_list = "hola python"
print(my_list)
print(type(my_list))










