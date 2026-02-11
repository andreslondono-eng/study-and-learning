# Higher Order Functions (funciones de orden superior) = función que cumple al menos una de estas condiciones: recibe una o más funciones como argumentos, y/o devuelve una función como resultado.
# Es decir una función de orden superior opera sobre funciones.

# Usamos funciones dentro de funciones:
def sum_one(value):
    return value + 1

def sum_two_values_and_add_one(first_value, second_value):
    return sum_one(first_value + second_value)

print(sum_two_values_and_add_one(5, 2))

# Pasarle por parametro la función:

def sum_five(value):
    return value + 5


def sum_two_values_and_add_values(first_value, second_value, f_sum):    # "f_sum" es solo para indicar que vamos a pasar un parametro (en este caso la función)
    return f_sum(first_value + second_value)    #"f_sun" solo representa la función que se dara afuera, puede ser tanto "sum_five" como "sum_one", etc.


print(sum_two_values_and_add_values(5,2, sum_one))
print(sum_two_values_and_add_values(5,2, sum_five))


# Otro ejemplo de uso donde pasamos una función por medio de los parametros de otra función

def operar(a, b, operador):
    return operador(a,b)

def sumar(x, y):
    return x + y

def multiplicar(x, y):
    return x * y

# print(operar(3, 4, sumar))
# print(operar(3, 4, multiplicar))



# CLOSURES = Es una función que: se define dentro de otra función; Usa variables de la función externa, recuerda esas variables incluso despues de que la función externa termino su ejecución.
# Definición tecnica = Un closure es una función que encapsula (cierra sobre) su entorno léxico, se puede simploificar como una función que devuelve una función.

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)
print(add_closure(5)) 
print(sum_ten(5)(1))    #Tambien podemos llamar la función y ejecutarlo como si fuera una lambda.



# Built-in Higher Order Functions (Funciones de orden superior que ya existen en el propio lenguaje)


numbers = [2, 5, 10, 21, 3, 30]

#Map = transformación de datos (con un listaqdo iterable genera otro listado iterable en función a la función dada)

def multiply_two(number):
    return number * 2


print(list(map(multiply_two, numbers)))   #Para imprimir el objeto lo transformamos a "list()"
print(list(map(lambda number: number * 2 , numbers)))   #podemos usar lambdas como argumento(función)

#Filter = selección / filtrado

def filter_greater_than_ten(number):
    if number > 10:
        return True 
    return False

print(list(filter(filter_greater_than_ten, numbers)))  #Solo devuelve numeros mayores a 10, en este caso: 21 y 30
print(list(filter(lambda number: number > 10 , numbers)))   #lo mismo pero con una lambda


# Reduce
from functools import reduce

def sum_two_values(first_number, second_number):
    print(first_number)
    print(second_number)
    return first_number + second_number

print(reduce(sum_two_values, numbers))  #suma el primer dato con el segundo, como es un iterable es practicamente como sumar

