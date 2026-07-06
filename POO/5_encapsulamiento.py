#Encapsulamiento: ocultar los detalles internos y exponer solo una interfaz segura.
#A diferencia de Java o C++, donde existen palabras como private o protected, Python no tiene mecanismos estrictos de ocultación. En Python todo es "público" por defecto.
#Sin embargo, existe una convención muy respetada por todos los programadores:
#Existen tipos: publico, protegido y privado. El publico es el que se puede acceder desde cualquier parte del programa, el protegido es el que se puede acceder desde la clase y sus subclases, y el privado es el que solo se puede acceder desde la clase.
#Público: self.nombre (Acceso libre).
#Protegido: self._nombre (Un solo guion bajo). Indica: "Esto es interno, no deberías tocarlo desde afuera".
#Privado: self.__nombre (Dos guiones bajos). Python hace un "truco" llamado name mangling para que sea difícil acceder desde afuera.

class miClase:
    def __init__(self):
        #Para definir los atributos privados, se utiliza un guion bajo antes del nombre del atributo. y para atributos muy privados se utilizan dos guiones bajos, lo que hace que el nombre del atributo se "mangle" (cambie) para evitar accesos directos desde fuera de la clase.
        self.__atributo_privado = "valor"
    #Tambien existen los metodos privados
    def __hablar(self):
        print("hola como estas")    
    

objeto = miClase()

#Los metodos y atributos privados no se pueden ejecutar o llamar directamente
# print(objeto.__atributo_privado)

#Para acceder a los datos encapsulados tenemos que utilizar "Getters"(obtenedor) y "Setters"(Establecedor/Definidor/modificador)
#El getter es método que tenemos que utilizar para acceder a un atributo muy privado o privado.
#El setter es el que utilizamos para establecer/modificar el valor de un atributo privado o muy privado

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    #creamos el getter: En Python el getter es crear un método con que devuelva un atributo privado
    def get_nombre(self):
        return self.__nombre
    #creamos el setter: En Python es un método que permite establecer o modificar el valor de un atributo de una clase de forma controlada
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre
    
        
        
dalto = Persona("Lucas", 21)

nombre = dalto.get_nombre()    
print(nombre)

dalto.set_nombre("Pepito")

nombre = dalto.get_nombre()    
print(nombre)




#Forma en la que deveria ser la sintaxis en python segun la ia:

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo interno (convención con guion bajo)
        self._edad = edad

    # 1. GETTER: Se accede como 'obj.nombre'
    @property
    def nombre(self):
        return self._nombre

    # 2. SETTER: Se asigna como 'obj.nombre = "Nuevo"'
    @nombre.setter
    def nombre(self, nuevo_valor):
        if not isinstance(nuevo_valor, str):
            raise ValueError("El nombre debe ser una cadena de texto.")
        self._nombre = nuevo_valor

    # 3. DELETER: Se activa con 'del obj.nombre'
    @nombre.deleter
    def nombre(self):
        print(f"Eliminando el nombre: {self._nombre}")
        self._nombre = None

# --- Uso ---
p = Persona("Ana", 30)

# Leer (ejecuta el getter)
print(p.nombre)  # Salida: Ana

# Escribir (ejecuta el setter con validación)
p.nombre = "Carlos" 
# p.nombre = 123  # Lanzaría ValueError

# Eliminar (ejecuta el deleter)
del p.nombre  






"""
El encapsulamiento se usa para proteger el estado interno de un objeto y evitar que sea modificado directamente desde fuera de la clase. Esto ayuda a mantener la integridad de los datos y a controlar cómo se accede y modifica la información dentro de un objeto
Al usar métodos getter y setter, puedes validar los datos antes de permitir cambios, lo que mejora la seguridad y la robustez del código.: 

Investifar que es el @property y porque en python este remplaza el get_ y set_
al parecer en python crear el setter y el getter es diferente a lo que aprendi entonce investigar mas por mi cuenta.

Investigar el termino "decorador" en python (o programación en general)

"""


















class encaopsulamiento:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("La edad no puede ser negativa.")