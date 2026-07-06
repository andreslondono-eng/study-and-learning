#Métodos especiales (o dunder) =  son funciones predefinidas que permiten personalizar el comportamiento de las clases y sus objetos ante operaciones específicas.
#El nombre "Dunder" viene de Double Underscore (doble guion bajo), porque todos empiezan y terminan así: __metodo__. También se les conoce como métodos mágicos o métodos especiales.

class Persona:
    #init = método constructor: se ejecuta al crear un objeto. su propósito es inicializar los atributos
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #str = se ejecuta al usar print() o str(). su propósito es devolver una versión "bonita" del objeto para humanos. (o sea cuando se imprime un objeto o se usa str() devuelve una cadena con lo que pongamos)
    def __str__(self):
        return f"Persona(nombre={self.nombre},edad={self.edad})"
    
    #repr = se utiliza para definir una representación de cadena oficial y inequívoca de un objeto, principalmente destinada a desarrolladores y depuración.
    #se ejecuta al ver el objeto en la consola. O sea es como el str pero devuelve una representación técnica para desarrolladores.
    def __repr__(self):
        return f'Persona("{self.nombre}","{self.edad}")'



Dalto = Persona("Dalto", 21)
repre = repr(Dalto)     #repre de representación. 
resultado = eval(repre)      #eval() = evalúa una cadena como una expresión de Python y devuelve su resultado.(o sea agarra una cadena de texto y permite hacer operaciones)

#con eval reconstruimos el objeto: "resultado" es el objeto
print(Dalto)
print(resultado)

#Otros métodos especiaes:
# Estudiar mas sobre el concepto de sobrecarga de operadores: característica de la programación orientada a objetos que permite redefinir el comportamiento de los operadores estándar (como +, -, ==, <<) 
# para que funcionen con tipos de datos definidos por el usuario (clases o estructuras), en lugar de limitarse a los tipos primitivos del lenguaje.


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"Persona(nombre={self.nombre},edad={self.edad})"
    
    def __repr__(self):
        return f'Persona("{self.nombre}","{self.edad}")'
    
    def __add__(self, otro):
        return Persona(self.nombre+otro.nombre,self.edad+otro.edad)





dalto = Persona("Dalto", 21)
pedro = Persona("Pedro", 30)
maria = Persona("maria", 20)

nueva_persona = dalto + pedro + maria
print(nueva_persona.edad)














"""
ejemplo de funcionamiento de la función eval()


expresion = "1 + 2 + 3"
resultado = eval(expresion)
print(resultado)
"""