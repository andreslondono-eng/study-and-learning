#Dependency Inversion Principle (Principio de Inversión de la Dependencia):
#Establece que los módulos de alto nivel no deben depender de módulos de bajo nivel, sino ambos deben depender de abstracciones, y las abstracciones no deben depender de los detalles

#forma erronea:

class Diccionario:
    def verificar_diccionario(self,palabra):
        #Lógica para verificar palabras
        pass
    
class CorrectorOrtografico:
    def __init__(self):
        self.diccionario = Diccionario()

    def corregir_texto(self,texto):
    #usamos el diccionario para corregir el texto
        pass

#El problema aqui es que el corrector ortografico esta fuertemente ligado al diccionario, esto significa que si queremos cambiar la forma en la que "revisamos palabras" tendriamos que
#cambiar la clase corrector ortografico, porque si la clase "Diccionario" cambia la clase "CorrectorOrtografico" tambien cambia

#En este caso hay que ponerse a pensar cual clase es la mas importante (alto nivel) y que esta no dependa de una clase de menos importante (bajo nivel).

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        #Logica para verificar palabra
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #Lógica para verificar palabras si esta en el diccionario
        pass

#podemos simplemente crear otra clase
class ServicioOnline(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #Lógica para verificar palabras desde el servicio web
        pass

class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador
        
    def corregir_textos(self, texto):
        #usamos el verificador para corregir texto
        pass


corrector = CorrectorOrtografico()




# OTRO EJEMPLO:
#El Mal Ejemplo (Violando el DIP)
#Aquí, la clase de "alto nivel" (Robot) depende directamente de una clase de "bajo nivel" (Espada)

class Espada:
    def usar(self):
        return "Atacando con espada ⚔️"

class Robot:
    def __init__(self):
        # ERROR: El Robot está 'soldado' a la Espada. 
        # Si queremos un arco, hay que modificar la clase Robot.
        self.arma = Espada() 

    def combatir(self):
        print(self.arma.usar())


#El Buen Ejemplo (Siguiendo el DIP)
#Para arreglarlo, creamos una abstracción (una interfaz o clase base). El Robot dejará de depender de una clase concreta y empezará a depender de un concepto.

from abc import ABC, abstractmethod

# 1. Creamos la ABSTRACCIÓN (el "enchufe")
class Arma(ABC):
    @abstractmethod
    def usar(self):
        pass

# 2. Implementamos los detalles (las "herramientas")
class Espada(Arma):
    def usar(self):
        return "Atacando con espada ⚔️"

class Arco(Arma):
    def usar(self):
        return "Disparando flecha 🏹"

# 3. La clase de ALTO NIVEL depende de la ABSTRACCIÓN
class Robot:
    def __init__(self, arma: Arma): 
        # Ya no creamos el arma adentro, la RECIBIMOS (Inyección de Dependencias)
        self.arma = arma

    def combatir(self):
        print(self.arma.usar())

# --- USO ---
espada_comun = Espada()
arco_veloz = Arco()

# Podemos darle cualquier arma al robot sin tocar su código interno
robot_guerrero = Robot(espada_comun)
robot_arquero = Robot(arco_veloz)

robot_guerrero.combatir()
robot_arquero.combatir()






#Este principio "amarra" todos los anteriotes, para que el dip funcione, se suele usar el OCP y el LSP


