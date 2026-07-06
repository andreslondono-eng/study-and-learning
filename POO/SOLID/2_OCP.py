#Open/Closed Principle (Principio de Abierto/Cerrado):
#las entidades de software deben estar abiertas para su extensión (permitir nuevas funcionalidades) pero cerradas para su modificación (sin alterar el código existente)
class Notificador:
    def __init__(self,usuario,mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificar(self):
        raise NotImplementedError
    

class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por MAIL a {self.usuario.email}")
        
        
class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviando SMS a {self.usuario.sms}")
        
    #ahora si queremos agregar mas funcionalidades, como "notificar por whatsapp" pues simplemente creamos una clase que herede de "Notificador"

class NotificadorWhatsApp(Notificador):
    def Notificar(self):
        print(f"Enviando Whatsapp a {self.usuario.whatsapp}")




#otro Ejemplo de una buena aplicación:
#Para cumplir con OCP, usamos herencia o polimorfismo. Creamos una base que define "qué se hace", y las extensiones definen "cómo se hace":

from abc import ABC, abstractmethod

# 1. Definimos una clase abstracta (el contrato)
class Personaje(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def atacar(self):
        pass

# 2. Extendemos la funcionalidad creando nuevas clases
# No modificamos la clase Personaje, simplemente creamos nuevas.
class Guerrero(Personaje):
    def atacar(self):
        return f"{self.nombre} usa su espada ⚔️"

class Mago(Personaje):
    def atacar(self):
        return f"{self.nombre} lanza una bola de fuego 🔥"

class Arquero(Personaje): # ¡Añadir esto fue fácil! No toqué las clases de arriba.
    def atacar(self):
        return f"{self.nombre} dispara una flecha 🏹"

# 3. El procesador ahora es SIMPLE y no cambiará nunca
class ProcesadorDeCombate:
    def ejecutar_ataque(self, personaje: Personaje):
        # No le importa qué tipo de personaje es, solo que tenga el método atacar()
        print(personaje.atacar())

# Uso:
guerrero = Guerrero("Aragorn")
mago = Mago("Gandalf")
arquero = Arquero("Legolas")

combate = ProcesadorDeCombate()
combate.ejecutar_ataque(guerrero)
combate.ejecutar_ataque(mago)
combate.ejecutar_ataque(arquero)

"""
¿Por qué es mejor así?
Código Intocable: Una vez que ProcesadorDeCombate está testeado y funcionando, no lo vuelves a tocar. Esto evita que al añadir un personaje nuevo rompas accidentalmente la lógica de los personajes viejos.

Escalabilidad: Si mañana quieres añadir un "Nigromante", solo creas la clase Nigromante(Personaje), escribes su ataque y listo. El resto del sistema ni se entera, pero lo acepta perfectamente.

Mantenibilidad: Los errores son más fáciles de encontrar. Si el ataque del arquero falla, sabes que el problema está en la clase Arquero, no en un if gigante de 500 líneas.
"""
 
        