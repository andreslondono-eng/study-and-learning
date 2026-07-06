#poli (muchos) y morfismo (formas) = En programación, es la capacidad de que objetos de diferentes clases respondan al mismo mensaje (método) de maneras distintas.
#por ejemplo si quieres reproducir algo(musica, video, podcasr): el comando es el mismo reproducir() pero el resultado depende de quién recibe la orden.

#Por lo que llevo entendido el polimorfismos es hacre una funcion que llame a las clases con un mismo metodo


class Gato():
    def sonido(self):
        return "Miau"
    
class Perro():
    def sonido(self):
        return "Guau"

def hacer_sonido(animal):
        print(animal.sonido())
 
 
gato = Gato()
perro = Perro()
 

 
 
print(gato.sonido()) 
print(perro.sonido())

hacer_sonido(gato)
hacer_sonido(perro)







#Estudio importante relacionado al tema:
#todos los tipos de polimorfismo en Python = polimorfismo de inclusión, de herencia de subclases, sobrecarga, coerción, etc. y sus usos.(no estoy seguro si todos estos tipos estan en python pero aprenderlos de todas formas)

#Estudiar lo que es el Duck Typing y como afecta a el polimorfismo de python (eso que en los lenguajes estaticos tiene que aver una herencia, pero en python no)

#Estudiar los enlaces dinámicos y enlaces estáticos

#Estudiar lo que es un tipo real y tipo declarado (esto para entender que es un enlace dinamico)

"""
En Python existe un concepto llamado "Duck Typing" (Tipado de Pato):

"Si camina como un pato y grazna como un pato, entonces es un pato".

Esto significa que dos clases no necesitan heredar del mismo padre para ser polimórficas. Si ambas tienen un método con el mismo nombre, Python las tratará igual.
""" 