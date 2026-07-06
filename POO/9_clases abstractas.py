#Es una clase que no se puede instanciar, ¿Por qué? Porque es tan genérica o incompleta que no tiene sentido que exista por sí sola
#Su propósito es servir como plantilla obligatoria para otras clases. Define un contrato: "Cualquiera que quiera ser un 'Empleado', tiene que tener sí o sí estos métodos"
#Python no tiene palabras reservadas como abstract (de Java). Usamos el módulo incorporado abc (Abstract Base Classes).

from abc import ABC, abstractmethod

class Persona(ABC):
    # El __init__ NO debe ser abstracto. 
    # Es el constructor que todas las hijas usarán vía super().__init__()
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    # Este sí es abstracto: obliga a las hijas a tener su propia versión
    @abstractmethod
    def hacer_actividad(self):
        pass

    # Este también puede ser abstracto si quieres obligar a definirlo
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")



# --- Ejemplo de cómo se implementa una hija ---
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de: {self.actividad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")
    



# --- Prueba ---
# p = Persona("Juan", 25, "M", "Dev") # Esto daría error, es abstracta
Juan = Estudiante("Juan", 25, "F", "Programación")
Juan.presentarse()
Juan.hacer_actividad()
        
Dalto = Trabajador("Dalto", 30, "M", "Programación")
Dalto.presentarse()
Dalto.hacer_actividad()



"""
Esttudiar cuales son las ventajas y en que situaciones se usan las clases abstractas 
por ejemplo cuando queremos hacer autodocumentación o si queremos fomentar el polimorfismo. Esto aparte del nivel extra de seguridad que nos dan

########################
Tambien hacer un ejercicio para probar si al heredar una clase abstracta sin definir el __init__ python busca el __init__ de la clase padre
########################




1 - @staticmethod y @abstractmethod:

Estudiar bien paraque es @staticmethod = Este decorador sirve para crear métodos que no necesitan al objeto (self) para funcionar. Es una función que vive dentro de la clase por orden, pero que no toca los datos internos del objeto.
Para qué sirve: Para funciones de utilidad o ayuda. Cosas que se relacionan con la clase, pero que no necesitan saber quién es el usuario actual o cuál es su saldo.
No usa self: Fíjate que en los paréntesis no se pone self.

class Validador:
    @staticmethod
    def es_adulto(edad):
        return edad >= 18 # No necesita 'self', solo el dato que le pasas
        
        
@abstractmethod = Este decorador solo vive dentro de las Clases Abstractas. Su única misión es obligar.
Para qué sirve: Para decir: "Cualquier clase que herede de esta, TIENE que escribir su propia versión de este método, o no dejaré que el programa funcione"
No tiene código real: Normalmente solo lleva un pass.

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass # Obligo a los hijos a definir su sonido


2 - Cuando los combinamos estamos creando una Obligación independiente:
Le estás diciendo a las clases hijas:

(@staticmethod): " ese método debe ser independiente (no debe usar self)".
(@abstractmethod): "Y además, Estás obligada a tener este método".


"""