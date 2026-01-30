contactos = {}

from flujo import pausa, menu


# función para guardar información en el archivo.txt:
# Borramos el archivo y lo reconstruimos desde el diccionario para evitar errores(duplicados, perdida de información, etc):
def guardar_contacto():
    with open("contactos.txt","w") as archivo:
        for nombre, numero in contactos.items(): #items() es para poder iterar ambos elementos a la vez, sino solo nos daria la clave o saltaria error.
            archivo.write(f"{nombre},{numero}\n")


# funcion para cargar los datos (contactos) del archivo:
def cargar_contactos():
     with open("contactos.txt", "r") as archivo:
        for linea in archivo:
            nombre, numero = linea.strip().split(",") #strip = para quitar el \n al final de cada linea y split = separar los datos con la ","
            contactos[nombre] = numero
        

# opcion 1: funcion para agregar contactos
def agregar_contacto():
    # Modificamos el diccionario, no guardamos en el archivo.txt:
    name = input("Digite el nombre del contacto: ")     #Hay un error? si ponemos datos con comas, por ejemplo: nombre = angel,1324 numero = 1234. El programa no esta preparado para esto.
    number = input("Digite el numero del contacto: ")   #Creo que deveria hacer una validación de archivos antes de leerlos?(talvez cuando cargo los contactos al diccionario?)
    if name in contactos:
        pausa("Ese contacto ya existe.")
    else:
        contactos[name] = number
        guardar_contacto()
        pausa("contacto agregado.")

# opcion 2: funcion para Buscar contactos:
def buscar_contact():
    look = input("Digite el nombre del contacto:" )
    if look in contactos:
        pausa(f"El numero del contacto es: {contactos[look]}.")
    else:
        pausa("Contacto no encontrado.")

#  opcion 3: funcion para mostrar contactos:
def mostrar_contactos():
    if not contactos: #si contactos esta vacio seria false, con el "not"  seria True, o dicho de otra forma: "si contactos esta vacio: hacer esto"
        pausa("No hay contactos guardados")
    else:
        for nombre, numero in contactos.items():
            print(f"nombre: {nombre} - numero: {numero}.")
        pausa()


# Cargamos contactos del archivo.txt al diccionario (recordar que solo se carga una vez y antes del bucle, asi evitamos lecturas inecesarias):

cargar_contactos()

while True:
     
    opcion = menu()
    
    if opcion is None:  #el "is" con el "None" compara "identidad", dicho de otro modo "¿opción es exactamente el objeto None?", Solo existe un único None en memoria. el "==" es solo si el valor es igual no si es exacto
        pausa("Seleccione una de las opciones validas")
        continue

    if opcion == 1:
        agregar_contacto()

    elif opcion == 2:
        buscar_contact()

    elif opcion == 3:
        mostrar_contactos()

    elif opcion == 4:
        break

    else:
        pausa("Seleccione una de las opciones validas")