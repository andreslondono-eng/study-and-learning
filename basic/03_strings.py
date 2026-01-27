# Strings

my_string = "Mi string"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

My_new_string = "este es un string \n con salto de linea" #\n = caracter especial = salto de linea
print(My_new_string)

My_new_string = "\teste es un string con tabulación de linea"
print(My_new_string)

# Formateo

name, surname, age = "Andres", "Lopez", 35

# se usa {} o %
# %s = string
# %d = interger (Entero)
# %f = Floating point number

print("mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("mi nombre es %s %s y mi edad es %s" %(name, surname,age))
# Inferencia de datos, una manera mas simplificada: poner "f" adelante y meter los datos en {}
print(f"mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
languaje = "python"
a, b, c, d, e, f = languaje
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División
languaje_slice = languaje[1:3] # empieza en la posicion 1 y termina en la 3 (no incluida)
print(languaje_slice)

languaje_slice = languaje[1:] 
print(languaje_slice)

languaje_slice = languaje[-2] 
print(languaje_slice)

# evitar los caracteres, mas bien con el tercer dato que le pasamos le decimos cuanto saltar
languaje_slice = languaje[0:6:2] 
print(languaje_slice)

# Reverse 
reversed_languaje = languaje[:: -1] #El final empieza desde -1
print(reversed_languaje)

#Funciones = al poner un "." nos dice que operaciones tenemos disponibles para cadenas de texto

print(languaje.capitalize())    #pone la primera letra en mayuscula
print(languaje.upper())         #convierte a mayusculas
print(languaje.count("t"))      #cuantas "t" hay
print(languaje.isnumeric())  
print("1".isnumeric())
print(languaje.lower())         #convierte a minusculas 
print(languaje.upper().isupper()) #isupper es para comprobar si esta en mayusculas
print(languaje.startswith("py")) #¿Comienza con py?




