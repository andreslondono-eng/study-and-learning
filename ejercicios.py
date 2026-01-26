# name = input("Nombre: ")
# print(f"Hola, {name}!")

# n_one = int(input("primer numero: "))
# n_two = int(input("segundo numero: "))

# print(f"suma: {n_one + n_two}\nresta: {n_one - n_two}\nmultiplicación: {n_one * n_two}")


# num_par_impar = int(input("digitte un numero: "))

# res = num_par_impar % 2

# print(f"tu numero es {res}")
# print("0 = par\n1 = impar")

# n = 0
# while n < 100:
#     n += 1
#     if n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz")
#         continue
#     elif n % 3 == 0:
#         print("Fizz")
#         continue
#     elif n % 5 == 0:
#         print("Buzz")
#         continue
#     print(n)

# Clasificador de vocales en un texto:

# texto = "Si ya tienes los fundamentos de Python, lo mejor es practicar con retos que te obliguen a pensar"
# vocales = {"a":0, "e":0, "i":0, "o":0, "u":0}

# for vocal in texto.lower():
#     if vocal == "a":
#         vocales["a"] += 1
#     elif vocal == "e":
#         vocales["e"] += 1
#     elif vocal == "i":
#         vocales["i"] += 1
#     elif vocal == "o":
#         vocales["o"] += 1
#     elif vocal == "u":
#         vocales["u"] += 1
# print(vocales)

# función para verificar si el numero es primo:

def es_primo(n: int) -> bool:
    i = 1
    if n <= 1:
        return False
    if n == 2:
        return True
    
    while i < n-1:
            i += 1
            if n % i == 0:
                return False
    return True


# numeros primos del 1 - 100 con la función creada


i = 1
lista_prim = []
while i <= 100:
    if es_primo(i):  #Esto funciona igual que un if es_primo(i) == True:
        lista_prim.append(i) #append() agrega un elemento al final sin tener que crear una nueva lista.
    i += 1

#Forma profesional:
# lista_prim = []

# for i in range(1, 101):
#     if es_primo(i):
#         lista_prim.append(i)

#Eliminar duplicados:

# numbers = [1, 2, 2, 3, 4, 4, 5, 2]
# numbers_repeat = []

# for num in numbers:
#     if num in numbers_repeat:
#         continue
#     else:
#         numbers_repeat.append(num)

# Alternativa recomendada:
# numbers = [1, 2, 2, 3, 4, 4, 5, 2]
# numbers_repeat = []
# vistos = set()

# for num in numbers:
#     if num not in vistos:
#         numbers_repeat.append(num)
#         vistos.add(num)


# Diccionario contador de palabras

# texto = "texto = hola hola mundo mundo mundo" 
# lis = texto.split() 
# vistos = list() 
# dic = dict() 
# for i in lis: 
#     if i not in vistos: 
#         dic[i] = None 
#     vistos.append(i) 
        
        
# for i in dic:
#     contador = vistos.count(i) 
#     dic[i] = contador

# El primer código (lo borre) conte los elementos con "count()" funciona pero es ineficiente ya que recorre toda la lista cada vez, por eso mejore el código.

# texto = "texto = hola hola mundo mundo mundo"
# palabras = texto.split()

# dic = dict()

# for i in palabras:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1

# Agenda con menu: Agregar contacto, buscar contacto, mostrar todos, salir:

# crear un diccionario para almacenar los nombres junto con sus numeros
# crear un bucle continuo con las opciones y romperlo cuando el usuario seleccione "salir" 
# las opciones crearlas con input?

contactos = {}

# función para controlar el flujo, mas que nada para no usar directamente input() (por sintaxis entre otras cosas):
def pausa(texto:str = ""):
    input(f"{texto}\nPresione una tecla para continuar")

# función para guardar información en el archivo.txt:
# Borramos el archivo y lo reconstruimos desde el diccionario para evitar errores(duplicados, perdida de información, etc):
def guardar_contacto():
    with open("contactos.txt","w") as archivo:
        for nombre, numero in contactos.items(): #items() es para poder iterar ambos elementos a la vez, sino solo nos daria la clave o saltaria error.
            archivo.write(f"{nombre},{numero}\n")




# Cargamos contactos del archivo.txt al diccionario:
try:
    with open("contactos.txt", "r") as archivo:
        for linea in archivo:
            nombre, numero = linea.strip().split(",") #strip = para quitar el \n al final de cada linea y split = separar los datos con la ","
            contactos[nombre] = numero
except FileNotFoundError:
    print("Archivo no encontrado")

while True:
    try:
        # input siempre devuelve un "str" por eso cuando le quito el "int" deja de funcionar, porque no reconoce el dato como un numero
        opción = int(input(
            "\n1. Agregar contacto"
            "\n2. Buscar contacto"
            "\n3. Mostrar contactos"
            "\n4. Salir\n"
            ))
    except ValueError:
        pausa("Seleccione una de las opciones validas")
        continue

    if opción == 1:
        # Modificamos el diccionario, no guardamos en er archivo.txt:
        name = input("Digite el nombre del contacto: ")     #Hay un error? si ponemos datos con comas, por ejemplo: nombre = angel,1324 numero = 1234. El programa no esta preparado para esto.
        number = input("Digite el numero del contacto: ")   #Creo que deveria hacer una validación de archivos antes de leerlos?(talvez cuando cargo los contactos al diccionario?)
        if name in contactos:
            pausa("Ese contacto ya existe.")
        else:
            contactos[name] = number
            guardar_contacto()
            pausa("contacto agregado.")

    elif opción == 2:
        look = input("Digite el nombre del contacto:" )
        if look in contactos:
            pausa(f"El numero del contacto es: {contactos[look]}.")
        else:
            pausa("Contacto no encontrado.")

    elif opción == 3:
        if not contactos: #si contactos esta vacio seria false, con el "not"  seria True, o dicho de otra forma: "si contactos esta vacio: hacer esto"
            print("No hay contactos guardados")
        else:
            for nombre, numero in contactos.items():
                print(f"nombre: {nombre} - numero: {numero}.")
        pausa()

    elif opción == 4:
        break

    else:
        pausa("Seleccione una de las opciones validas")

########### El codigo esta bien pero seria mejor simplificarlo creando funciones para tareas como cargar/guardar/agregar contactos, etc, para luego meter esas funciones dentro de una funcion mas grande.Hacer un código mas modular y reutilizale
########### Tambien guardar la indormación antes de salir (haciendola función), por si se cierra la aplicación de forma inesperada no se pierda 
#por si no existe el archivo lo mejor es hacer un manejo de errores(try, except), tambien agregar la función: isdigit(): (para asegurar que ingresen un numero)

# strip() = elimina espacios en blanco (como espacios, tabulaciones y saltos de línea) al inicio y al final de una cadena de texto.
# split() = método de cadenas que divide una cadena en una lista de subcadenas según un delimitador especificado, Este método es ampliamente utilizado para procesar texto.(hay que indicarles el separador)
# como convertir una oración en una lista de palabras o extraer datos de formatos como CSV, su sintaxis es: cadena.split(separador, maxsplit) (dónde dividir la cadena, limita número máximo de divisiones).
# .items() = 
















"""
para que es el "in" como en "if num in numbers" = in es un operador de pertenencia:
Su función es responder a esta pregunta lógica:
“¿Existe este valor dentro de esta colección?”

investigar EAFP (Easier to Ask Forgiveness than Permission).

estudiar metodos y funciones mas relevantes.

o tambien un  "for nombre, numero in contactos.items():" (contactos es una lista)

siempre usar .items() al iterar un diccionario
any()
split()

que es "as"? = es el alías

En programación se sigue mucho este patrón:
Fail fast / early return

Primero se controla: error, vacío, caso límite

Luego se ejecuta la lógica principal, ejemplo mental:

if no hay datos:
    aviso
else:
    proceso normal

Regla mental que debes quedarte:

Primero pregunta: “¿puedo continuar?”
Si la respuesta es NO → maneja eso y sal
Si es SÍ → ejecuta lo normal

Estudiar los modos de archivo y la forma correacta de acceder a un archivo:
tambien que es y como se utiliza el with.
diferencia y traduccion entre with y while y los que se parescan.

with open("contactos.txt", "r") as archivo:
    contenido = archivo.read()


| Modo   | Significado                  |
| ------ | ---------------------------- |
| `"r"`  | Leer (read)                  |
| `"w"`  | Escribir (borra lo anterior) | IMPORTANTE RECORDAR QUE BORRA LO ANTERIOR
| `"a"`  | Agregar (append)             | 
| `"r+"` | Leer y escribir              |

Regla mental clave

"r" = el archivo DEBE existir
"w" = si no existe, se crea
"a" = si no existe, se crea



investigar que es "global variable" y como afecta a las funciones


"""