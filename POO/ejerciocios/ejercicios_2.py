#Ejercicio de herencia y uso de super:
"""
1.
Crea un sistema para una escuela. En este sistema, vamos a tener dos clases principales:
Persona y Estudiante.La clase Persona tendrá los atributos de nombre y edad y un método que improima el nombre y la edad de la persona.
La clase Estudiante heredará de la clase Persona y también tendrá un atributo adicional: grado y un método que imprima el grado del estudiante.

Deberás utilizar super en el método de inicialización (init) para reutilizar el código de la clase padre(Persona).
Luego crear una instancia de la clase Estudiante e imprime sus atributos y utiliza sus métodos para asegurarte de que todo funciona correctamente.
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def info(self):
        return f"Información:\n\nNombre: {self.nombre}.\nEdad: {self.edad}"


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def mostrar_grado(self):
        return f"Grado: {self.grado}"


estudiante = Estudiante("Andres", 15, 10)

print(estudiante.nombre)
print(estudiante.edad)
print(estudiante.grado)

print(estudiante.info())
print(estudiante.mostrar_grado())


"""
2.
Imagina que estás modelando animales en un zoológico. Crear tres clases: "Animal", "Mamifero" y "Ave".La clase "Animal" debe tener un método llamado "comer".
La clase "Mamifero" debe tener un método llamado "amamantar" y la clase "Ave" un método llamado "volar".

Ahora, crea una clase "Murcielago" que herede de "Mamifero" y "Ave", en ese orden, y por lo tanto debe ser capaz de "amamantar" y "volar", ademas de "comer".

Finalmente, juega con el orden de herencua de la clase "Murcielago" y observa cómo cambia el MRO y el comportamiento de los métodos al usar super().
"""
print("\nEJERCICIO 2:\n")

class Animal:
    def comer(self):
        return "El animal esta comiendo"
    
class Ave(Animal):
    def volar(self):
        return "El animal esta volando"
    
class Mamifero(Animal):
    def amamantar(self):
        return "El animal esta amamantando"
    
class Murcielago(Mamifero, Ave):
    pass

murcielago = Murcielago()

print(murcielago.comer())
print(murcielago.amamantar())
print(murcielago.volar())

print(Murcielago.mro())
