# Loops =  estructuras de control que permiten ejecutar un bloque de código múltiples veces, automatizando tareas repetitivas y facilitando el procesamiento de colecciones de datos de forma eficiente.


# While = Repetir mientras se cumpla una condición

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:
    print("Mi condición es mayor o igual que 10") #En python se le puede poner un "else" a un bucle.

print("La ejecución continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detenie la ejecución en 15") 
        break #detenemos la ejecución del loop(bucle)
    
    print(my_condition)

print("La ejecución continua")


# For = Recorrer algo que ya tiene elementos = Iterar un listado de elementos

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuples = (35, 1.77, "Andres", "Lopez", "Andres")

for element in my_tuples:
    print(element)

my_set = {"Andres", "Lopez", 35}

print("SETS:")
for element in my_set:
    print(element)

my_dict = {"Nombre":"Andres","Apellido":"Lopez","Edad":35,1:"Python"}

print("DICT:")
for element in my_dict: #Esto imprime solo las claves, recordar que si queremos que nos devielva los valores tenemos que usar el .values():
    print(element)
    if element == "Edad":
        break  #Cuando se ejecuta el "break" se cancela completamente el bucle
else:
    print("El bucle for para diccionario a finalizado")



for element in my_dict:
    print(element)
    if element == "Edad":
        continue        #Salta lo que queda de esta iteración y pasa a la siguiente
    print("se ejecuta")
else:
    print("El bucle for para diccionario a finalizado")


# Ejemplo del continue:
print("===CONTINUE===")
for i in range(1, 6):
    if i == 3: #Nos saltamos el 3 gracias al "Continue"
        continue
    print(i)
















