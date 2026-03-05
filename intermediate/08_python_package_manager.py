#Comom manejar dependensias
#Python package manager (gestor de paquetes para python) = herramienta que permite instalar, actualizar, eliminar y administrar dependencias (librerías externas) dentro de un entorno Python
#pip es el gestor de paquetes oficial de Python: https://pypi.org #investigar mas sobre pip y como se utiliza desde la terminal
#creo que podemos trabajar desde la terminal con el pip y las dependencias descargadas.

#pip install pip = instalarlo
# #pip --version = ver la versión

#pip install numpy = descargamos/instalamos la dependencia numpy
import numpy as np   

print(np.version.version)

numpy_array = np.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))
print(numpy_array + 2)

#pip install pandas
import pandas 

# pip list = muestra las librerias/dependencias que tenemos en el sistema
# pip uninstall pandas = desisntalar pandas (o cualquier dependencia)
# pip show numpy = información de la dependencia

#pip install requests
import requests
#esta libreria facilita enormemente el envío de solicitudes HTTP, como GET, POST, PUT, DELETE, entre otros (o sea es como en php)
#esto me recuerda que tengo que aprender a hacer solicitudes HTTP con python, es algo que me interesa mucho y es super util para trabajar con APIs

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=20")
print(response)
print(response.status_code)
print(response.json())

# package = carpeta que creamos y contiene un archivo __init__.py (puede estar vacio) y otros modulos (archivos .py) con funciones, clases, etc. que se pueden importar y usar en otros archivos de python

import my_package.arithmetics #importamos el modulo arithmetics que esta dentro de la carpeta my_package
from my_package import arithmetics #otra forma de importar el modulo arithmetics

print(my_package.arithmetics.sum_two_values(5, 10))
print(arithmetics.sum_two_values(5, 10))

# por cierto el __init__.py es un archivo que se utiliza para indicar que la carpeta es un paquete de python, y puede contener código de inicialización para el paquete, pero no es obligatorio que tenga contenido, puede estar vacio.
from my_other_package import other_arithmetics
print(other_arithmetics.sum_two_values(5, 10))