#Single Responsibility Principle (Responsabilidad Única):
# una clase o módulo debe tener una sola razón para cambiar, es decir, debe enfocarse en una única funcionalidad o responsabilidad.

class Auto():
    def __init__(self):
        self.posicion = 0
        self.combustible = 100
        
    def mover(self, distancia):
        if self.combustible >= distancia / 2:
            self.posicion += distancia
            self.combustible -= distancia / 2
        else:
            print("no hay suficiente combustible")

    def agregar_combustible(self,cantidad):
        self.combustible += cantidad
        
    def obtener_combustible(self):
        return self.combustible
#Esto estaria mal porque la clase auto estaria encargandose de el movimiento del auto y el combustible del auto, rompiendo la regla SRP.
#lo mejor es separar estas "funcionalidades" en distintas clases:

class Auto():
    def __init__(self,tanque):
        self.posicion = 0
        self.tanque = tanque
        
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            return f"Has movido el auto exitosamente"
        else:
            return "no hay suficiente combustible"
            
    def obtener_posición(self):
        return self.posicion

class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self,cantidad):
        self.combustible += cantidad
    
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self,cantidad):
        self.combustible -= cantidad
        
tanque = TanqueDeCombustible()
autito = Auto(tanque)

print(autito.obtener_posición())
print(autito.mover(10))
print(autito.obtener_posición())
print(autito.mover(20))
print(autito.obtener_posición())
print(autito.mover(60))
print(autito.obtener_posición())
print(autito.mover(100))
print(autito.obtener_posición())
print(autito.mover(29))
print(autito.obtener_posición())



