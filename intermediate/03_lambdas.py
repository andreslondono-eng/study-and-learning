# Lambdas = Son funciones anonimas (sin nombre) definida en una sola expresión. Se usa para operaciones simples, cortas y puntuales
#Sintaxis: lambda argumentos: expresión

sum_two_values = lambda first_value, second_value: print(first_value + second_value)
print(sum_two_values(2, 4))     #nos devuelve un None porque el lambda nos devuelve un print, dicho de otro modo es como estuvieramo poniendo: print(print())

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 4))

# Una lambda puede pasar a estar dentro de una función:
def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(4)(2, 4))



# Estudiar en que situaciones se utiliza, sus usos tipicos:
"""
### Uso típico con map()

Aplica una función a cada elemento de un iterable.

numeros = [1, 2, 3, 4]
resultado = map(lambda x: x * 2, numeros)
print(list(resultado))  # [2, 4, 6, 8]


### Uso con filter()

Filtra elementos según una condición.

numeros = [1, 2, 3, 4, 5]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  # [2, 4]


### Uso con sorted()

Muy común para definir criterios de ordenación.

personas = [("Ana", 25), ("Luis", 20), ("Juan", 30)]
ordenadas = sorted(personas, key=lambda x: x[1])


LAMBDA VS DEF(FUNCIÓN)

| Lambda                 | def              |
| ---------------------- | ---------------- |
| Función corta          | Función completa |
| Una sola expresión     | Múltiples líneas |
| Menos legible si crece | Más legible      |
| Uso puntual            | Uso reutilizable |
 
Las lambdas no permiten:

múltiples expresiones
asignaciones (=)
bucles
try/except
return
 
Regla práctica:
Si la función tiene más de una línea o lógica compleja, NO usar lambda.


"""