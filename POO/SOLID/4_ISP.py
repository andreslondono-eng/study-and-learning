#Interface Segregation Principle (Principio de Segregación de la Interfaz): 
#Sugiere que muchas interfaces específicas son mejores que una interfaz de propósito general, evitando que los clientes se vean forzados a depender de métodos que no utilizan
#(creo que en este caso con "interfaz" se estan refiriendo a las clases abstractas)

from abc import ABC, abstractmethod

class Trabajador(ABC):
    
    @abstractmethod
    def comer(self):
        pass
    
    @abstractmethod
    def trabajar(self):
        pass
    
    @abstractmethod
    def dormir(self):
        pass


class Humano(Trabajador):
    def comer(self):
        return "El humano esta comiendo"
    
    def trabajar(self):
        return "El humano esta trabajando"
    
    def dormir(self):
        return "El humano esta durmiendo"
    

class Robot(Trabajador):
    def comer(self):
        pass
    
    def trabajar(self):
        return "El robot esta trabajando"
    
    def dormir(self):
        pass

#Esto esta mal porque la clase "Robot" está "engordando" con métodos que no necesita solo para satisfacer a la clase padre.
#Un ejemplo de una buena aplicación:

#Primero segregamos (separamos) en subclases:

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass
    
class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass

#Luego hacemos que Humano herede todas las caracteristicas que necesite:

class Humano(Trabajador, Comedor, Durmiente):
    def comer(self):
        return "El humano esta comiendo"
    
    def trabajar(self):
        return "El humano esta trabajando"
    
    def dormir(self):
        return "El humano esta durmiendo"
    
#Ahora a diferencia del humano el robot podra solo heredar de la clase "Trabajador":

class Robot(Trabajador):
    
    def trabajar(self):
        return "El robot esta trabajando" 
    

robot = Robot()
humano = Humano()

print(robot.trabajar())
print(humano.trabajar())
print(humano.comer())
# print(robot.comer())      Esto da error porque robot no tiene implementado el metodo "comer", porque no lo necesita.




"""
Investigar que son las interfaces o la implementación de interfaces tanto en python como en otros lenguajes de programación(es muy importante esta comparativa)




"""





