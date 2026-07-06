#crear clase Estudiante -> atributos: Nombre, Edad, Grado -> metodos: estudiar() -> se deve interactuar y brindar los atributos al usuario para que los llene, al escribir "estudiar" poner al estudiante a estudiar:


class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print("Estudiando...")
        

nombre = input("Digite su nombre: ") 
edad = input("Digite su edad: ") 
grado = input("Digite su grado: ") 

estudiante = Estudiante(nombre, edad, grado)

print(f"""
DATOS DEL ESTUDIANTE: \n\n
Nombre: {estudiante.nombre}\n
Edad: {estudiante.edad}\n
Grado: {estudiante.grado}\n
      """)

while True:
    estudiar = input("que hará?: ")
    if estudiar.lower() == "estudiar":
        estudiante.estudiar()
        break
    else:
        respuesta = input("opción no valida, quiere seguir intentando (enter - No)")
        if respuesta.lower() == "no":
            break





 