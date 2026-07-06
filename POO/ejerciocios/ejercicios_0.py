# Probando crear una clase
#En python hay una regla universal en donde todas las primersa letras de una clase deven ser mayusculas (ayuda a distinguir una clase de una variable)
class Libro:    
    def __init__(self, titulo, autor, n_paginas):
        self.n_paginas = n_paginas
        self.titulo = titulo
        self.autor = autor
        
        
    def describir(self):    # La clase ya conoce el titulo y el autor por lo que no hay que definirlos, solo el "self" para ir a buscarlos a su propia "memoria".
        return f"El libro: {self.titulo}, fue escrito por {self.autor}" #se usa solo el retur (si usaramos print() nos devolveria un "None")
    
    def leer(self, paginas_leidas:int):
        self.n_paginas -= paginas_leidas
        return f"has leido {paginas_leidas} páginas, te quedan {self.n_paginas}"  


mi_objeto = Libro("El principito", "Saint-Exupéry", 104)

print(mi_objeto.describir())
print(mi_objeto.leer(24))


#Existe un método especial llamado __str__ (viene de string o cadena de texto). Si lo defines, Python sabrá automáticamente cómo mostrar tu objeto cuando uses un simple print():

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    # Reemplazamos 'describir' por el método mágico __str__
    def __str__(self):
        return f"El libro: {self.titulo}, fue escrito por {self.autor}"

mi_objeto = Libro("El Principito", "Saint-Exupéry")

# Ya no tienes que llamar a un método específico
# Solo imprimes el objeto y Python usa el __str__ por detrás
print(mi_objeto)


### HAY QUE APRENDER A VALIDAR LOS DATOS ###
#Por ahora confio en que el usuario pondra valores logicos. Pero ¿qué pasa si alguien crea un libro con -10 páginas?
#hay que aprender a poner pequeñas reglas dentro del __init__ para evitar que se creen objetos con datos absurdos











#Clase de cuenta bancaria basica:

class CuentaBancaria:
    #El Constructor:
    def __init__(self, titular:str, saldo_inicial:int):
        self.cuenta = titular
        self.saldo = saldo_inicial
        
    def depositar(self, cantidad:int):
        self.saldo += cantidad
        return f"Depositaste ${cantidad}. Nuevo saldo ${self.saldo}"
    
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            return f"Error, No tiene suficientes fondos. Tu saldo es {self.saldo}"
        else:
            self.saldo -= cantidad
            return f"Retiraste ${cantidad}. Nuevo saldo ${self.saldo}"
        
    def cobrar_comision(self):
        self.saldo -= 10
        return "La comisión le ha restado $10 a su saldo."     
        
        
    def __str__(self):
        return f"Cuenta de: {self.cuenta} | Saldo actual: ${self.saldo}"
    
    
mi_cuenta = CuentaBancaria("Andres L", 100005000)
    
print(mi_cuenta.retirar(53631))
    
print(mi_cuenta.cobrar_comision())




