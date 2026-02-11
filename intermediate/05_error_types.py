# Error Types = excepciones/errores que puede devolver python (por consola) y como solucionarlos/controlarlos

# SyntaxError:

# print "Hola mundo"    #Error
print("Hola mundo")


#NameError:
# print(language)     Error = language no esta definido 


#IndexError:
my_list = ["python","swift","kotlin","dart","javaScript"]
# print(my_list[5])   #Error = el index esta fuera de rango(no existe el elemento 5)


#:ModuleNotFoundError:
#import maths    #Error = modulo no existente
import math


#AttributeError:
#print(math.PI)  # Error = modulo math no tiene un atributo llamado PI (en mayusculas)
print(math.pi)


# KeyError:
my_other_dict = {"Nombre":"Andres","Apellido":"Lopez","Edad":35,1:"Python"}
print(my_other_dict["Edad"])
#print(my_other_dict["Apelido"])     #Error = no existe clave llamada Apelido (deberia ser Apellido) 


# TypeError:
# print(my_list["Nombre"])    #Error = en las listas los indices deben de ser integers or slices, no str(texto)


# ImportError:s
# from math import PI     #Error = no se ha podido importar el nombre PI(no existe pi en mayusculas)


# ValueError:
# my_int = int("10 Años")     #Error = no se puede transformar un "str" a "int"
# print(type(my_int))


# ZeroDivisionError:
#print(4/0)     Error = error especifico para cuando dividimos entre zero



"""
RESUMEN Y DESCRIPCIÓN DE LOS ERRORES MAS COMUNES:

SyntaxError = Error de sintaxis
El intérprete no puede parsear el código porque viola las reglas gramaticales del lenguaje

NameError = Uso de un identificador que no existe en el namespace actual
Variable, función o nombre no definido

IndexError = Índice fuera de rango
Se intenta acceder a una posición inexistente en una secuencia (lista, tupla, string)

ImportError = Problema al importar algo dentro de un módulo existente
El módulo existe, pero el objeto no

ModuleNotFoundError = Subclase de ImportError
Python no encuentra el módulo que intentas importar

AttributeError = El objeto no tiene el atributo o método que intentas usar

KeyError = Se intenta acceder a una clave inexistente en un diccionario

TypeError = Operación aplicada a un tipo de dato incorrecto

ValueError = El tipo es correcto, pero el valor es inválido

zeroDivisionError = División entre cero

# Extras, no vistas:

IndentationError = Subclase de SyntaxError
Problemas de indentación (mezclar tabs y espacios)

FileNotFoundError = Intentar abrir un archivo que no existe

UnboundLocalError = Subclase de NameError
Variable local referenciada antes de asignarse:
def f():
    print(x)
    x = 5


AssertionError = Cuando falla una instrucción assert

StopIteration = Relacionado con iteradores. Normal en internals, pero puede aparecer en generadores mal manejados.
"""