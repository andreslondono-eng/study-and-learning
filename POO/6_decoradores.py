#Un decorador en Python es una función que modifica o extiende el comportamiento de otra función o clase sin alterar su código original
#Se aplica usando la sintaxis @nombre_decorador (la función que creamos) justo encima de la definición de la función
#El decorador "envuelve" la función, permitiendo ejecutar código antes, después, o bajo ciertas condiciones

def decorador(funcion):
    def funcion_modificada():
        print("antes de llamar a la función")
        funcion()
        print("Despues de llamar a la función")
    return funcion_modificada

###Esto es como se hacia anteriormente:

# def saludo():
#     print("!Hola, mundo!")

# saludo_modificado = decorador(saludo)
# saludo_modificado()


###Esta es la forma de ejecutar el código optimo con el que deveriamos hacerlo:

@decorador
def saludo():
    print("Hola como estas")

saludo()















"""
Aclaración: Un decorador debe devolver la función (como un objeto), no ejecutarla. o sea el return de la función no deve de tener paréntesis.
Investigar bien para que sirven o en que situaciones se puede/suelen usar los decoradores 

Un detalle importante: El Orden Importa
Python lee los decoradores de abajo hacia arriba (o de adentro hacia afuera).

"""
