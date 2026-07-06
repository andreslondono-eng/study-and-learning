# Herencia en POO = la herencia es la herramienta que te permite crear moldes nuevos basados en otros que ya existen, sin tener que escribir todo desde cero
# Cuando creamos una clase a partir de otra clase(herencia) estas se llaman clases hijas

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print("hola, estoy hablando")
        
# Metiendo la clase entre parentesis creamos la herencia:
# class Empleado(Persona):
#     def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
#         #super() es una función especial que dice: "Busca a mi padre y ejecuta este método"(o sea heredamos los metodos que queramos del padre)
#         super().__init__(nombre, edad, nacionalidad)
#         self.trabajo = trabajo
#         self.salario = salario
        
#     #Dato extra: como siempre tambien se sobreescribir los datos (en este caso el método: hablar()) 
#     def hablar(self):
#         print("NO")
            

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"




 
#herencia multiple:

class PersonaArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        #Para heredar los metodos en una herencia multiple tenemos que hacer una referencia directa a las clases padres:
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
    
    def presentarse(self):
        return print(f"Hola soy: {self.nombre}, {super().mostrar_habilidad()} y trabajo en {self.empresa}")   #Con super() le decimos al programa que es un metodo de arriba
    #o sea super() es como un atajo e búsqueda, sirve para decirle a python: "Ve a la clase de arriba (el padre) y ejecuta esto que te pido"




roberto = PersonaArtista("Roberto", 43, "Colombiano", "Programador", 100000, "google")

# Verificamos si es una subclase con la función: issubclass()
herencia = issubclass(PersonaArtista, Persona)

# Verificamos si un objeto es una instancia de una clase con la función: isinstance()
instancia = isinstance(roberto, PersonaArtista)


print(herencia) 
print(instancia)










"""
Estudiar bien el concepto de herencia jerárquica y herencia multiple





"""













