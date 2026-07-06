# MRO = Method Resolution Order (Orden de Resolución de Métodos)
# conjunto de reglas que utiliza Python para decidir en qué orden va a buscar un método o atributo dentro de una jerarquía de clases
"""
Funciona utilizando el algoritmo llamado C3 Linearization. Sus reglas principales se resumen en tres principios:

1 - Los hijos primero: Python siempre buscará el método en la clase actual antes de buscar en sus clases padre

2 - De izquierda a derecha:
En la herencia múltiple (ej. class D(B, C):), Python buscará primero en la clase de la izquierda (B) y luego en la de la derecha (C)

3 - Las clases base compartidas van al final: Si varias clases comparten un mismo padre (la clase A en el problema del diamante), Python solo revisará esa clase padre una vez que haya revisado todos sus hijos
"""
class A:
    def saludar(self):
        print("Hola desde A")

class B(A):
    def saludar(self):
        print("Hola desde B")

class C(A):
    def saludar(self):
        print("Hola desde C")

class D(B, C):
    pass

obj = D()
obj.saludar()

#En este ejemplo el orden seria = D > B > C > A 


class A:
    def saludar(self):
        print("Hola desde A")
        
class E:
    def saludar(self):
        print("Hola desde E")

class B(A):
    pass

class C(E):
    def saludar(self):
        print("Hola desde C")

class D(B, C):
    pass


obj = D()
obj.saludar()

# En este caso el orden seria = 1: D > B > A 
#                               2: D > C > E


#inspeccionar el mro = Python permite ver el MRO exacto utilizando el método: .mro() o el atributo .__mro__:

print(D.mro())



#Llamar explícitamente a la clase por su nombre, o sea saltarse el orden natural del MRO:

#Normalmente, si usas self.metodo(), Python usará el MRO para buscarlo. Si en cambio usas NombreDeLaClase.metodo(self), tú tomas el control total:
A.saludar(obj)
E.saludar(obj)
C.saludar(obj)

