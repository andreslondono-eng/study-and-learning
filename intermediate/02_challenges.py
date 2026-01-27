### Challenges ###

def fizzbuz():
    for numbers in range(1, 101):
        if numbers % 3 == 0 and numbers % 5 == 0:
            print("fizzbuzz")
        elif numbers % 3 == 0:
            print("fizz")
        elif numbers % 5 == 0:
            print("buzz")
        else:
            print(numbers)

# anagrama = contiene las mismas letras desordenadas = ordenar las eltras por orden alfavetico y compararlas
# poner un condicional: en caso de que las dos palabras sean iguales = False. En ese caso no seria un anagrama solo la misma palabra. 

def is_anagram(word_one:str , word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower().strip()) == sorted(word_two.lower().strip())   #las funciones no se ven activas porque python no sabe que tipo de datos son #Al usar sorted creo que lo transforma en una lista y por eso funciona(porque para utilizar el .sort() se necesita una lista) 


#Si quisieramos hacer un palíndromos(misma palabra al derecho y del revez) lo podriamos hacer con: 
# return word_one[::-1]   #[:] (slicing) = La sintaxis general es: word_one[inicio:fin:paso] -> paso = -1 → recorre la cadena hacia atrás


# fibonacci = primeros 50 primeros numeros
def fibonacci_1():
    
    prev = 0
    next = 1
    
    for _ in range(1, 51):
        print("Puesto: ", _)
        print(prev)
        
        fib = next + prev
        prev = next
        next = fib 


#Ejemplo 2 fivonacci:
def fibonacci_2(n):
    
    a, b = 0, 1
    
    for _ in range(n):
        a, b = b, a + b
    return a
 
 
# fibonacci_1()
# print(fibonacci_2(2))

# Numero primo = comprueba si un numero es primo, imprimir tambien lo numeros entre 1 - 100 

def is_prime():
    
    for number in range(1, 101):
        
        if number >= 2:
            
            is_divisible = False
            
            for _ in range(2, number):
                if number % _ == 0:
                    is_divisible = True
                    break
                    
            if not is_divisible:
                print(number)

is_prime()

# Invertir el orden de una cadena

def reverse(text):
    reversed_text = ""
    for _ in range(0, len(text)):
        reversed_text = text[::-1]
    
    
    return reversed_text
    
    
    
print(reverse("Hola mundo"))














