# función para controlar el flujo, mas que nada para no usar directamente input() (por sintaxis entre otras cosas):
def pausa(texto:str = ""):
    input(f"{texto}\nPresione una tecla para continuar")

# Funcion para mostrar menu + control de errores:
def menu():
    try:
        # input siempre devuelve un "str" por eso cuando le quito el "int" deja de funcionar, porque no reconoce el dato como un numero
        opcion = int(input("\n1. Agregar contacto"
                           "\n2. Buscar contacto"
                           "\n3. Mostrar contactos"
                           "\n4. Salir\n"))
        return opcion
    except ValueError:
        return None