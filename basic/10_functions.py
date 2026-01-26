# Functions = bloques de código reutilizables que realizan una tarea específica y pueden ser llamados desde diferentes partes de un programa.
# Definir una función:

def my_function ():
    print("Esto es una función")

my_function ()
my_function ()

# función que resive parametros:
def sum_two_values (first_value, second_value):
    print(first_value + second_value)


sum_two_values(5, 7)
sum_two_values(23231, 34534)
sum_two_values("5", "7") #Nos concatena las cadenas de texto
sum_two_values(1.4, 5.2)

my_result = sum_two_values(1.4, 5.2) 
print(my_result) #como la función no tiene "return" no nos devuelve nada


def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value + second_value
    return my_sum #return nos devuelve el valor Y TERMINA la función inmediatamente.

my_result = sum_two_values_with_return(10, 5)
print(my_result)


def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname ="Lopez",name = "Andres") #Podemos reasignar las variables, en este caso para intentar ordenar


#Parametros por defecto: 

def print_name_with_default (name, surname, alias = "Sin alias"): #el = en el alias es para asignar un valor "default"
    print(f"{name} {surname} = {alias}")

print_name_with_default("Andres", "Lopez", "AN")
print_name_with_default("Andres", "Lopez")


def print_upper_text(*texts: str): #El * es para indicar que se puede pasar varios parametros
    for text in texts:
        print(text.upper())


print_upper_text("Hola", "Python", "Andres")





















