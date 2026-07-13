#Expresiones regulare (regex)
import re

# Para escribir una formula lo tenemos que poner entre comillas y para que se entienda que es una expresiòn regular (en python) hay que anteponer una r:

regex = r"((M|m)+) [a-z0-9A-Z]{5,8} ((M|m)+)"

#re.match = Intenta encontrar un patron desde el inicio de la cadena, en caso contrario retorna "None" 
#Si el patrón se encuentra al principio, devuelve un objeto de coincidencia (match object)
#Sintaxis re.match(patrón, cadena) = la función verifica si el patron empieza como la cadena

match = re.match(regex, "Mi nombre es mouredev")
print(match)

#re.findall = Encontra todas las coincidencias no superpuestas de un patrón de expresión regular en una cadena de texto y devolverlas como una lista
match = re.findall(regex, "Mmmmmm")
print(match)

#re.search = busca la primera coincidencia de un patrón de expresión regular en una cadena de texto, A diferencia de re.match(), re.search() escanea todo el texto.
findall = re.search(regex, "Mmmmmm Moure10 MMmM") #Con el simbolo $ busca hasta el final de la cadena por lo que nos devuelve una concidencia en span=(13, 17)
print(findall)

#verificar la URL de una web:
regex_web = r"^((https?://(www\.)?)|www\.)\w{3,}\.[a-zA-Z]{2,3}$"    #?: Hace que el carácter anterior sea opcional. \w: acepta cualquier palabra. \.: valida un punto.

findall = re.search(regex_web, "http://www.moure.com")
print(findall)














#regex para validar emails:

p = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

#Forma de crear un regex para validad una contraseña:

def validar_password(password):
    # Usamos re.VERBOSE para que sea legible
    patron = r"""
    ^                      # Inicio de la cadena
    (?=.*[A-Z])            # Lookahead: busca al menos una mayúscula
    (?=.*\d)               # Lookahead: busca al menos un número
    (?=.*[@$!%*?&])        # Lookahead: busca al menos un carácter especial
    [A-Za-z\d@$!%*?&]      # Permitir solo estos caracteres
    {8,}                   # Mínimo 8 caracteres de largo
    $                      # Fin de la cadena
    """
    
    # re.X es el alias de re.VERBOSE
    if re.match(patron, password, re.VERBOSE):  #re.VERBOSE = Su función principal es ignorar los espacios en blanco y permitir comentarios dentro de la cadena de texto de tu regex (o sea es para mayor legibilidad)
        return True
    return False

# Pruebas
passwords = ["abc123", "Password123", "Admin@2026", "sololetras"]

for p in passwords:
    estado = "Válida" if validar_password(p) else "Invalida" #Esto es una expresión condicional (operador ternario) = se usa cuando a condición es simple (solo asigna True o False)
    print(f"{p:15} -> {estado}")    #El p:15 = es un especificador de formato dentro de un f-string (Python reservará 15 espacios para mostrar el valor de p)




#### LO SIGUIENTE A ESTUDIAR: 
# 1 - Las Anclas Avanzadas (Lookaheads y Lookbehinds)
# 2 - El concepto de "Codicia" (Greedy vs. Lazy)
# 3 - Otros métodos de re en Python:
# re.sub(patron, reemplazo, texto)  
# re.split(patron, texto))








