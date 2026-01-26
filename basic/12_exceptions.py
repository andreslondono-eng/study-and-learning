# exception handling (manejo de errores) = o sea como manejar errores que si o si saltaran, ya sea para evitar que salten como ignorandolos o manejarlos 
# es la forma “correcta y elegante” de evitar que tu programa se rompa cuando ocurre algo inesperado… y además decidir qué hacer en ese caso.

#try = Palabra clave utilizada para definir un bloque de código que puede generar una excepción, permitiendo que los errores se capturen y manejen de forma controlada con except.

try:                                                                                                                                        pass
    # código que puede fallar
except:                                                                                                                                     pass
    # qué hacer si falla


numberOne, numberTwo = 5, 1
numberTwo = "1"

# try except:
try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except:
    # Se ejecuta si se produce una exepción (o sea si hay un error en el try)
    print("se ha producido un error")


# try except else finally (el else y el finally son opcionales)
try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except:
    print("se ha producido un error")
else:   
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally:
    # Se ejecuta siempre
    print("la ejecución continua")

#Excepciones por tipo = Podemos especificar el error, en este caso el except solo se ejecuta si se produce un typeError o un ValueError

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except ValueError as e:
    print("se ha producido un ValueError")
except TypeError:   
    print("se ha producido un error")

# Captura de la información de la excepción
# si nuestro programa da error vamos a querer saber que error o porque se a producido
# alabra clave utilizada principalmente para crear un alias o nombre alternativo para un módulo

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except ValueError as error:     #encapsulamos el error en un alias ("error" en este caso)
    print(error)    #Imprimimos el error
except Exception as error:  #Exception es una escepción cualquiera (la podemos usar cuando no sabemos el tipo de error)
    print(error)




"""""

Si no lo he visto investigar que es el comando raise


tambien estudiar las excepciones más comunes en python:

| Error               | Cuándo ocurre         |
| ------------------- | --------------------- |
| `ValueError`        | Valor incorrecto      |
| `TypeError`         | Tipo incorrecto       |
| `ZeroDivisionError` | División por cero     |
| `IndexError`        | Índice fuera de rango |
| `KeyError`          | Clave inexistente     |
| `FileNotFoundError` | Archivo no existe     |


Resumen rápido

try: intenta ejecutar

except: maneja el error

else: se ejecuta si no hubo error

finally: siempre se ejecuta

raise: lanza un error manualmente

"""
