# classes = una plantilla o modelo que define cómo se crearán los objetos, actúa como un plano para construir instancias concretas.

class MyEmptyPerson:
    pass #pass = No hace nada, es una instrucción vacía = Evita errores de sintaxis, Sirve como placeholder, No cambia el flujo, No es lógica real

# se puede llamar una clase con o sin paréntesis, son necesarios solo si se va a crear una instancia
print(MyEmptyPerson)
print(MyEmptyPerson())


#el "init" es algo reservado del sisteme que sirve para crear un constructor de clase
class person:
    def __init__(self, name, surname): #con el "init" esto ya no es una función, es un constructor de clases (donde establecemos los valores asociados a la clase)
        self.full_name = f"{name} {surname}"

    def walk (self): #una función dentro de una clase le opdemos pasar el parametro "self" y podemos acceder a todo lo que este guardado dentro de self
        print(f"{self.full_name} está caminando")


my_person = person("Andres", "calle")
print(my_person.full_name) #con el . llamamos a la "variable" que creamos en la clase, en este caso el "self.full_name"
my_person.walk()






class person:
    def __init__(self, name, surname, alias = "Sin alias"): 
        self.full_name = f"{name} {surname} = ({alias})"

    def walk (self): 
        print(f"{self.full_name} está caminando")

my_person = person("Andres", "calle") #creamos un nuevo objeto para que funcione (no lo entendi muy bien)
my_person.full_name
print(my_person.full_name)

my_other_person = person("Brains", "Moure", "MoureDev")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Héctor de León El loco de los perros" #O sea puedo acceder a mi clase y a una propiedad de mi clase para cambiarla
print(my_other_person.full_name)

my_other_person.full_name = 4242124
print(my_other_person.full_name)






# Por si acaso y no lo he visto estudiar la "herencia" ya que esta es un mecanismo fundamental de la programación orientada a objetos
# Tambien estudiar lo de variables privadas o algo así era