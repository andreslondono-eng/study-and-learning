import os
# FILE HANDLING(manejo de archivos) = conjunto de operaciones que permiten a un programa crear, abrir, leer, escribir, modificar y cerrar archivos almacenados en el sistema de archivos

# .txt file

# La sintaxis completa de la función open() es: open(nombre_archivo, modo) = el modo indica que quieres hacer con el archivo

txt_file = open("intermediate/my_file.txt","r+")    #"r+" = leer y escribir
print(txt_file.read())
print(txt_file.read(10))    #unicamente lee y printea los primeros 10 caracters 
print(txt_file.readline())  #lee linea por linea
print(txt_file.readline())
print(txt_file.readlines())   #devuelve una lista donde cada elemento es una linea del archivo, cada linea es una cadena"str"
for line in txt_file.readlines():
    print(line) 

# txt_file.write("\nAunque tambien me gusta Kotlin")  #Esto se escribe en cada ejecución 
# print(txt_file.readline())

# LECTURA?

txt_file = open("intermediate/my_file.txt","w+")
txt_file.write("Mi nombre es Andres\nMi apellido es Lopez\n35 Años\ny mi lenguaje preferido es Python")
print(txt_file.read())
txt_file.write("\nAunque tambien me gusta Kotlin")

txt_file.close()

with open("intermediate/my_file.txt","a") as file_2:
    file_2.write("\ny Swift")

# os.remove("intermediate/my_file.txt")     #Importamos el moduloo os.remove para eliminar el archivo


# .json file = formato de texto estándar para almacenar y transferir datos de manera sencilla y legible tanto para humanos como para máquinas.

import json

json_file = open("intermediate/my_file.json","w+")

json_text = {"Nombre":"Andres",
             "Apellido":"Lopez",
             "Edad":35,
             "languaje":["Python", "Swift", "Kotlin"],
             "website":"https://moure.dev"
             }

#json_file.write(json_text)  #TypeError = el argumento debe de ser un "str"
#json.dumb = se utiliza para serializar (convertir) un objeto de Python a formato JSON y escribirlo directamente en un archivo.
#Es ideal cuando necesitas guardar datos estructurados en un archivo, como configuraciones, bases de datos simples o respuestas de APIs.
### ESTUDIAR LA SINTAXIS DE ESTE ATRIBUTO Y LO RELACIONADO E IMPORTANTE DEL MODULO "json"
json.dump(json_text, json_file, indent=4)   #puede que lo mejor sea sin identar para que el archivo no ocupe tanto
# json.dump(json_text, json_file, indent=4)

json_file.close()

with open("intermediate/my_file.json") as my_other_file:    #Como aclaración para mi mismo: poner open("intermediate/my_file.json") es lo mismo que incluir el: "r" (modo lectura)
    for line in my_other_file.readlines():
        print(line)

# Transformar lo que se lee a un diccionario:


json_dict = json.load(open("intermediate/my_file.json"))#leer datos en formato JSON desde un archivo y convertirlos a estructuras de datos de Python. json.load() → lee desde un archivo. json.loads() → lee desde un string
print(json_dict)
print(type(json_dict))
print(json_dict["Nombre"])

# .csv file = archivos tipo excel
import csv

csv_file = open("intermediate/my_file.csv","w+")

csv_write = csv.writer(csv_file)
#una primera fila con el "titulo de los datos" y una segunda con los datos que queremos meter
#csv.writer = constructor de un objeto serializador CSV.
# .writerow(iterable) = método que escribe una fila serializando cada elemento como campo CSV.
csv_write.writerow(["Nombre","Apellido","Edad","languaje","website"]) 
csv_write.writerow(["Andres","Lopez",35,"Python","https://moure.dev"])
csv_write.writerow(["roswell","", 2,"COBOL",""])

csv_file.close()


#.xlsx file
# import xlrd # Debe instalarse el modulo

# .xml file
import xml









"""
"r" = Read (leer) - modo por defecto
"w" = Write (escribir) - borra el contenido si ya existe
"a" = Append (agregar al final)
"x" = Crear archivo (error si ya existe)
"b" = Modo binario
"t" = Modo texto (por defecto)

modo conbinado = En open(), un modo combinado es aquel que, incluye un modo base: "r", "w" o "a" Y además incluye "+":
El símbolo "+" significa: Abrir el archivo en modo actualización (update mode) → permite leer y escribir

"""













