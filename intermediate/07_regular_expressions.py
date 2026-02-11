#REGULAR EXPRESSIONS (Expreciones regulares) = enguaje formal para describir patrones en texto
#Existe en la mayoría de lenguajes (Java, JavaScript, C#, PHP, etc.) porque resuelve un problema muy común en programación: buscar, validar, extraer o reemplazar texto según reglas específicas
#Para que se entienda mejor es como un filtro en el que especificamos o filtramos parametros, por ejemplo: [0-9] {9-9} = [0 a 9(solo numeros)], {rango minimo(9)-rango maximo(9)}

import re   # importamos el modulo de regular expressions

### Match = 

my_string = "Esta es la lección número 7: Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

#re.match = Intenta encontrar un patron, retornando si lo ha encontrado, en caso contrario retorna "None" 
print(re.match("Esta es la lección", my_string))    #Si la encuentra
print(re.match("Esta es la lección", my_other_string))  #None
print(re.match("Expresiones Regulares", my_string))     #Nos devuelve None porque .match empieza a buscar desde el principio

# En la sintaxis tambien podemos agregar criterios (creo que se les llama flags(vanderas)): Este caso "re.I" = ignorar mayúsculas y minúsculas
match = re.match("Esta es la lección", my_string, re.I)

print(match)
span = match.span()     #.span = devuelve las posiciones (índices) donde ocurrió la coincidencia dentro del string original.
print(span)

# match.span devuelve una tupla, por lo que podemos desempaquetarla en variables y estas pasarlas a la variable, así solo nos quedamos con el texto buscado:
start, end = span
print(my_string[start:end])

#Acceder a el? la forma de comprobar el None es directamente comparandolo
match = re.match("Esta es la lección", my_other_string)

# Otra forma de comprobar: if match si not None:
# Otra forma de comprobar: if not match == None:
if match != None:   
    print(match)
    start, end = match.span()
    print(my_string[start:end])



### search = 

search = re.search("lección", my_string, re.I)  #En vez de buscar desde el princio como el "match" busca en todo el contenido
print(search)
start, end = search.span()
print(my_string[start:end])
































"""
Las expresiones regulares permiten responder preguntas como:

¿Este string es un email válido?
¿Este texto contiene solo números?
¿Cuántas veces aparece una palabra?
¿Extraer todos los números de un texto?
¿Reemplazar todos los espacios por guiones?

En lugar de escribir múltiples condicionales (if, for, etc.), se define un patrón declarativo.





"""