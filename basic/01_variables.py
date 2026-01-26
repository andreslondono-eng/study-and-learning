# Aclaración de que no se pueden crear constantes en python (si hay formas de crear variables que actuen como una pero al final no son)
# Variables:
My_string_variable = "My string variable"
print(My_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable) 

# concatenación de variables en un print
print(My_string_variable, str(my_int_variable), my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(My_string_variable)) #len cuenta el número de caracteres de una cadena

# variables en una sola línea (se puede hacer pero creo que no es muy buena practica porque hace muy dificil el mantenimiento del codigo)
name, surname, alias, age = "Andres", "Lopez", "ANN", 25
print("Me llamo:",name, surname, ", mi alías es", alias, "Tengo",age,"años.")

# inputs: pedir datos al usuario
name = input("Cual es tu nombre?: ")
age = input("Cuantos años tienes?: ")
print("Tu nombre es:", name)
print("Tu edad es:", age)
# recuerda ejecutar desde la terminal con "python tu_archivo.py" para poder poner los datos

# cambiamos su tipo
name = 35
age = "Andres"
print(name)
print(age)

# ¿Forzamos el tipo?
address:str = "Mi dirección"    #python es typado devil entonces no se restringe a "str" pero ayuda y nos de funciones de "str" cuando hacemos por ejemplo: address.lower
address = 32
print(address)
print(type(address)) 

# se puede intentar cambiar el tipo o algo asi:
gravity = 9.81
numerInt = int(gravity)
print(numerInt)                  

# int to str
num_int = 10
print(type(num_int))                  # 10
num_str = str(num_int)
print(type(num_str))