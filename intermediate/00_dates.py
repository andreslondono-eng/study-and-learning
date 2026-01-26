# Dates =  

# import datetime #importamos las fechas
from datetime import datetime #o nos traemos solo la función

now = datetime.now()    #definimos una variable con la fecha y hora actual

#función para imprimir la información de una fecha y su timestamp.
def print_date(date:datetime):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())    

print_date(now)

#timestamp es un valor numérico que representa la cantidad de segundos (o milisegundos) transcurridos desde una fecha de referencia conocida como la época Unix, que es el 1 de enero de 1970 a las 00:00:00 UTC.
# Este formato permite una representación precisa, compacta y fácil de comparar para fechas y horas en sistemas informáticos.:
timestamp = now.timestamp()
print(timestamp)

# crear una fecha: con datetime metemos los datos que queremos(año, mes, dia, hora, etc.)
year_2026 = datetime(2026,1,1)

print_date(year_2026)

#time = representa una hora del día, sin fecha y sin zona horaria(Al llamar time() sin argumentos, estás creando un objeto time con valores por defecto: 00:00:00)
from datetime import time

current_time = time(21, 6, 0) #current time(hora)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# date = como el "time" pero solo con fechas 
from datetime import date

current_date = date.today() #esta fnucion devuelve la fecha actual

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 6) #especificamos la fecha

print(current_date.year)
print(current_date.month)
print(current_date.day)

# operaciones con fechas:
current_date = date(current_date.year , current_date.month + 1, current_date.day)

print(current_date.month)

diff = year_2026.date() - current_date
print(diff)

diff = year_2026 - now
print(diff)

# clase del módulo datetime que representa una duración o diferencia entre dos fechas, horas o instancias de datetime.
# Se utiliza principalmente para realizar operaciones aritméticas con fechas y horas, como sumar o restar días, horas, minutos, segundos, etc. 
from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)





















"""
time() → crea una hora 00:00:00
datetime.now().time() → obtiene la hora actual
datetime.time sirve para modelar horas, no para leer el reloj del sistema






"""