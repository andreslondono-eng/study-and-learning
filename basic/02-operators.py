# operadores, como los aritméticos y lógicos.
a = 10
b = 5
# Operadores aritméticos
print("Suma:", a + b)          # Suma
print("Resta:", a - b)         # Resta
print("Multiplicación:", a * b) # Multiplicación
print("División:", a / b)       # División
print("Módulo:", a % b)        # Módulo
print("Exponente:", a ** b)    # Exponente
print("División entera:", a // b) # División entera

print("Hola " + "Python " + "¿Que tal?")
print("Hola " + str(5)) #si no usamos la funcion str nos daria error
print("Hola " * 5)#si se puede multiplicar(ojo solo con los int, si son float dara error)

# Operadores de comparación
print("Operadores de comparación:")
print(3>4)
print(3<4)
print(3>=4)
print(3<=4)
print(3==4)
print(3!=4)


#Comparación alfabetica, no estamos contando caracteres, estamos comparando con una ordenación alfabetica cual es mayor
print("Orden alfabetico:")
print("aaaa" >= "aaaa")
print("aaaa" >= "abaa")
print("Hola"!="Hola")
print("Hola"<"python")
print("Hola" >= "python")

# Si queremos hacer una comparación contando caracteres utilizamos la función "Len"
print(len("aaaa") >= len("abaa"))

# Operadores lógicos
x = True
y = False
print("AND:", x and y) 
print("OR:", x or y)    
print("NOT x:", not x)  

























