# modulos = son archivos con extensión .py que contienen código reutilizable, como funciones, clases, variables o cualquier otro código válido en Python.
# import 10_functions as my_functions  #importamos el modulo "10_functions.py" y le damos un alias "my_functions" 
#Tener en cuenta que no se puede importar un archivo con por ejemplo numeros delante como "10_functions", por sintaxis python no lo acepta


import my_module   #accedemos a todo lo que hay en el archivo "my_module.py"

my_module.sumValues(5, 3, 1) #primero llamamos al archivo(en este caso modulo) y luego llamamos a sus funciones con .
my_module.printValue("Hola python!")

# from 10_functions import sum_two_values = Importar una unica función de un fichero
from my_module import sumValues, printValue

sumValues(5, 3, 1) #Como importamos una unica función no tenemos que llamar primero a el archivo(my_module.py)
printValue("Hola")

# python por defecto tiene algunos modulos, como por ejemplo:
import random
import math

print(math.pi)
print(math.pow(2, 8))

from math import pi as PI_VALUE

print(PI_VALUE)





