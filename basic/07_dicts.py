# Diccionario = Estructura de datos que permite almacenar información en pares de clave-valor, donde cada clave actúa como un identificador único para su correspondiente valor.

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Andres","Apellido":"Lopez","Edad":35,1:"Python"}

my_dict ={
    "Nombre":"Andres",
    "Apellido":"Lopez",
    "Edad":35,
    "Lenguajes":{"Python","Swift","Kolin"},
    1:"1.77"
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro" #Actualizamos el "valor" dentro de la clave
print(my_dict["Nombre"])

my_dict["Calle"] = "Calle Andres" #Se agrega un nuevo campo al diccionario
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("pedro" in my_dict)
print("Nombre" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = my_dict.fromkeys(("Nombre", 1, "piso")) #crear un diccionario sin valores, conservando las "keys", o sea se queda con las claves, pero elimina los valores
print(my_new_dict)

my_new_dict = my_dict.fromkeys(my_dict) #Esto es mas logico, porque creamos un diccionario con las claves de otro diccionario
print(my_new_dict)

my_new_dict = my_dict.fromkeys(my_dict, ("nuevas", "elementos")) #Crear un diccionario con las claves de otro diccionario, pero asignando un mismo valor a todas las claves
print(my_new_dict)















