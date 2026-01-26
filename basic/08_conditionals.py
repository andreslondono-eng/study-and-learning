# Condicionales = estructuras de control que permiten tomar decisiones durante la ejecución de un programa según el cumplimiento de ciertas condiciones

my_condition = False

if my_condition:
    print("se ejecuta la condición del if")

my_condition = 5*5

if my_condition == 10:
    print("se ejecuta la 2da condición del if")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual a 10 o mayor o igual que 20 o distinto de 25")

my_string = ""

if not my_string:
    print("Mi cadena de texto esta vacía")
    
if my_string == "Cadena de textooooo":
    print("La cadena de texto couincide")



print("La ejecución continua")


