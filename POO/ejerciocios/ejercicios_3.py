#Juego de fusión: El juego consiste en crear personajes en un juego y esos personajes se puedan fusionar para crear personajes mas poderosos que tengan mas poder...
#Para ello debemos cambiar el comportamiento del operador "+" para que cuando los personajes se fusionen, salga un nuevo personaje con habilidades mejoradas
#una posible formula es: el promedio de las habilidades de ambos, al cuadrado.

class Personaje:
    def __init__(self,vida,fuerza,estamina,magia):
        self.vida = vida
        self.fuerza = fuerza
        self.estamina = estamina
        self.magia = magia
    
    def __repr__(self):
        return f"Personaje(vida={self.vida},fuerza={self.fuerza},estamina={self.estamina},magia={self.magia}"
    
    def __add__(self, otro_p):
        nueva_vida = round(((self.vida+otro_p.vida)/2)**1.5,1)
        nueva_fuerza = round(((self.fuerza+otro_p.fuerza)/2)**1.5,1)
        nueva_estamina = round(((self.estamina+otro_p.estamina)/2)**1.5,1)
        nueva_magia = round(((self.magia+otro_p.magia)/2)**1.5,1)
        return Personaje(nueva_vida,nueva_fuerza,nueva_estamina,nueva_magia)
        
    
p1 = Personaje(2,3,4,5)
p2 = Personaje(5,3,1,2)

fusión = p1 + p2

print(fusión)



