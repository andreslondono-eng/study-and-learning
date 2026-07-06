class Celular:
    #Esto es el metodo constructor, se llama __init__ y se ejecuta automáticamente cada vez que se crea un nuevo objeto de la clase.
    #Es lo primero que se ejecuta al crear un nuevo objeto de la clase. Es el lugar donde se inicializan los atributos del objeto.
    def __init__(self, marca, modelo, camara):     #self es referencia a si mismo, es decir, al objeto que se está creando.
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    #metodos de la clase:
    def llamar(self):
        print(f"Estas haciendo un llamado desde un: {self.modelo}")
    
    def cortar(self):
        print(f"Cortaste la llamada desde un: {self.modelo}")
    
#Cuando creamos un objeto, estamos instanciando una clase. Es decir, estamos creando una instancia de esa clase. Cada objeto creado a partir de la clase tendrá sus propios atributos y métodos, pero compartirán la misma estructura definida por la clase.

celular1 = Celular("Samsung", "S23", "48MP")
celular2 = Celular("Apple", "iPhone 15 pro", "96MP")
celular1.cortar()



