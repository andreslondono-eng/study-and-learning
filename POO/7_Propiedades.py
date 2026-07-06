#Getters y Setters?:
#No confundir estas propiedades con variable o las propiedades de un objeto. (literalmente son getters y setters(y deleiters))


class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    #para decirle a la clase que vamos a usar un getter usamos: @property
    #@property es un decorador que permite definir un método como un getter, de modo que se pueda acceder a él como si fuera un atributo en lugar de llamarlo como una función
    @property
    def nombre(self):
        return self.__nombre
    
    #ahora vamos a crear el setter para modificar el valor, esto lo hacemos con @nombre_de_la_propiedad.setter  donde nombre_de_la_propiedad es el nombre del atributo que deseas controlar
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    
    #ahora siguen los deleters
    
    @nombre.deleter
    def nombre(self):
        del self.__nombre
    
    
    
dalto = Persona("Lucas", 21)

#Imprimimos el nombre:
nombre = dalto.nombre
print(nombre)

#Modificamos el nombre:
dalto.nombre = "Pepe"

nombre = dalto.nombre
print(nombre)

#Eliminamos el nombre:
del dalto.nombre 




