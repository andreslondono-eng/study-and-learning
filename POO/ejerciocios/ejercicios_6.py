#Juego de texto tipo rol con POO

class Lugar:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descipcion = descripcion
        self.objetos = []
        self.personajes = []
        self.caminos = {}

    def __str__(self):
        return f"{self.nombre}: {self.descipcion}"
    
    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)
        
    def agregar_personaje(self, personaje):
        self.personajes.append(personaje)
        
    def conectar_lugar(self, lugar, direccion):
        self.caminos[direccion] = lugar
        
class Objeto:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        
    def __str__(self):
        return f"{self.nombre}: {self.descripcion}"
    
class Personaje:
    def __init__(self, nombre, descripcion, dialogo=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.dialogo = dialogo
    
    def __str__(self):
        return f"{self.nombre}: {self.descripcion}"
        
    def hablar(self):
        if self.dialogo:
            print(f"{self.nombre}: {self.dialogo}")
        else:
            print(f"{self.nombre} no tiene nada que decir.")

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []

    def recoger_objeto(self, objeto):
        self.inventario.append(objeto)
    
    def mostrar_inventario(self):
        if self.inventario:
            print("Tu inventario:")
            for objeto in self.inventario:
                print(objeto)
        else:
            print("No tienes objetos en tu inentario")


class Juego:
    def __init__(self):
        self.lugares = {}
        self.jugador = None
        
    def agregar_lugar(self, lugar: Lugar):  #no estoy seguro de si tiene que ser una instancia de la clase Lugar
        self.lugares[lugar.nombre] = lugar
        
    def iniciar(self, nombre_jugador):
        self.jugador = Jugador(nombre_jugador)
        self.lugar_actual = self.lugares["Entrada"]
        print(f"Bienvenido al juego, {nombre_jugador}")
        self.mostrar_lugar_actual()
        
    def mostrar_lugar_actual(self):
        print(self.lugar_actual)
        if self.lugar_actual.objetos:
            print("objeto disponible")
            for objetos in self.lugar_actual.objetos:
                print(f" - {objetos.nombre}")
            if self.lugar_actual.personajes:
                print("Personaje presentes:")
                for personaje in self.lugar_actual.personajes:
                    print(f" - {personaje.nombre}")
            if self.lugar_actual.caminos:
                print("Puedes ir a:")
                for direccion in self.lugar_actual.caminos:
                    print(f" - {direccion}: {self.lugar_actual.caminos[direccion].nombre}")
            
    def mover_a(self, direccion):
        if direccion in self.lugar_actual.caminos:
            self.lugar_actual = self.lugar_actual.caminos[direccion]
            self.mostrar_lugar_actual()
        else:
            print(f"No puedes ir a {direccion}")
            
    def recoger_objeto(self, nombre_objeto):
        for objeto in self.lugar_actual.objetos:
            if objeto.nombre.lower() == nombre_objeto.lower():
                self.jugador.recoger_objeto(objeto)
                self.lugar_actual.objetos.remove(objeto)
                print(f"Has recogido {nombre_objeto}.")
                return
        print(f"No hay ningún objeto llamado {nombre_objeto} aqui.")
        
    def hablar_con(self, nombre_personaje):
        for personaje in self.lugar_actual.personajes:
            if personaje.nombre.lower() == nombre_personaje.lower():
                personaje.hablar()
                return
        print(f"No hay ningún personaje llamado {nombre_personaje} aqui.")
        
    def mostrar_inventario(self):
        self.jugador.mostrar_inventario()
        
        
### Creación del mundo del juego:

#Creación de lugares:
entrada = Lugar("Entrada", "Estas en la entrada de un bosque oscuro.")
bosque = Lugar("Bosque", "Te encuentras en un bosque lleno de árboles altos y oscuros.")
cueva = Lugar("Cueva", "Has entrado a una cueva fria y húmeda.")
aldea = Lugar("Aldea", "Una pequeña aldea con casas de madera y una plaza central.")

#Creación de los objetos:
espada = Objeto("Espada", "Una espada afilada y brillante")
pocion = Objeto("Poción", "Una poción de curación")
llave = Objeto("Llave", "Una llave vieja y oxidada.")

#Creación de personajes:          
goblin = Personaje("Goblin", "Un goblin pequeño y feo",
                   "Grulido... ¿Quien eres tú?")
aldeano = Personaje("Aldeano", "Un aldeano amigable",
                    "Hola, aventurero. ¡Gracias por salvarme del goblin!") 

#Colocación de objetos:
entrada.agregar_objeto(espada)
bosque.agregar_objeto(pocion)
cueva.agregar_objeto(llave)
cueva.agregar_personaje(goblin)
aldea.agregar_personaje(aldeano)

#Conectar los lugares
entrada.conectar_lugar(bosque,"norte")
bosque.conectar_lugar(cueva,"este")
bosque.conectar_lugar(entrada, "sur")
cueva.conectar_lugar(bosque,"oeste")
bosque.conectar_lugar(aldea, "oeste")
aldea.conectar_lugar(bosque, "este")


juego = Juego()
juego.agregar_lugar(entrada)
juego.agregar_lugar(bosque)
juego.agregar_lugar(cueva)
juego.agregar_lugar(aldea)

juego.iniciar("aventurero")

while True:
    comand = input(">").lower().split() #La función input() en Python se utiliza para recibir datos introducidos por el usuario desde el teclado durante la ejecución del programa
    if len(comand) == 0:
        continue
    if comand[0] == "ir":
        if len(comand) > 1:
            juego.mover_a(comand[1])
        else:
            print("Debes especificar una dirección para ir.\n")
    elif comand[0] == "recoger":
        if len(comand) > 1:
            juego.recoger_objeto(" ".join(comand[1:]))
        else:
            print("Debes especificar el nombre del objeto a recoger.\n")
    elif comand[0] == "hablar":
        if len(comand) > 1:
            juego.hablar_con(" ".join(comand[1:]))
        else:
            print("Debes especificar el nombre del personaje con el que quieres hablar.\n")
    elif comand[0] == "inventario":
        juego.mostrar_inventario()
    elif comand[0] == "salir":
        print("Gracias por jugar!")
        break
    else:
        print("Comando no reconocido. Intenta con 'ir', 'recoger', 'hablar', 'inventario' o 'salir'.\n")
            
            
        




















