#Liskov Substitution Principle (Principio de Sustitución de Liskov):
#Define que los objetos de una superclase deben ser reemplazables por instancias de sus subclases sin alterar el correcto funcionamiento del programa.

class Ave:
    def volar(self):
        return "Estoy volando"
    
class Pinguino(Ave):
    def volar(self):
        return "No puedo volar"
      
    
def hacer_volar(ave: Ave):
    return ave.volar()
    
# print(hacer_volar(Pinguino()))
    
    
#Esto estaria mal porque todo lo que herede de "Ave" deveria poder volar pero "Pinguino" no puede volar
#Una forma correcta de hacerlo seria:

class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"
    
class AveNoVoladora(Ave):
    pass

#Para que quede claro: Todo lo que tengan las aves lo tendran tanto las aves voladoras como las no voladoras, por lo que en "Ave" definiriamos todas las caracteristicas en comun,
#Y heredar la clase "Ave" para crear subdivisiones especificas: como "aves voladoras" o "aves nadadoras", etc.


##########################################################################################################

