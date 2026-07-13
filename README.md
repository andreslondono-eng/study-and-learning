Si es posible estudiarlo con el github al lado
Tambien revisar los ejercicios que he realizado y ver como lo he hecho y como lo mejoraria/Refactorizaria, y si se puede aplicar 
idea = pagina tipo "tier-list" para practicar html, css y js


# ----SISTEMA INFORMÁTICO----

## 🔸SOFTWARE:
Es la parte lógica e intangible de un sistema informático. Consiste en el conjunto de programas, instrucciones, datos y reglas que le indican al hardware qué hacer y cómo operar.
Ejemplos: Sistemas operativos (Windows, Android), aplicaciones (Word, Chrome), videojuegos.
Característica: No se puede tocar; es código que puede modificarse, actualizarse o borrarse fácilmente.

## 🔸HARDWARE:
Es la parte física y tangible de un sistema. Incluye todos los componentes materiales (eléctricos, electrónicos y mecánicos) que forman el dispositivo.
Ejemplos: Procesador (CPU), memoria RAM, pantalla, teclado, discos duros, y en sistemas mecánicos, engranajes y muelles.
Característica: Se puede tocar; sufre desgaste físico y requiere reemplazo si se daña.



## 🔹PROCESADOR / CPU (Unidad Central de Procesamiento): 
Es el componente físico más importante de un dispositivo informático, actuando como su cerebro; compuesto por miles de millones de transistores que se encargan de ejecutar instrucciones, realizar cálculos aritméticos y lógicos y interpretar los datos del software.
Su función principal es procesar información y coordinar el funcionamiento de todos los demás componentes del hardware (RAM, Almacenamiento, targeta gradica)


## 🔹TARGETAS GRAFICAS / GPU (Unidad de Procesamiento Gráfico):
Es el componente especializado en generar y renderizar las imágenes, vídeos y animaciones en la pantalla.
la GPU está diseñada para realizar miles de cálculos matemáticos simultáneos, lo que la hace ideal para tareas gráficas intensivas.

Tarjeta Gráfica Integrada = Una GPU integrada no es una tarjeta separada, sino un chip gráfico incrustado directamente dentro del mismo procesador (CPU) o soldado a la placa base. Utiliza una parte de la memoria RAM del sistema para almacenar y procesar los datos gráficos.

Tarjeta Gráfica Dedicada = Una GPU dedicada es un componente de hardware independiente que se instala en la placa base y cuenta con su propio procesador y sistema de refrigeración.


## 🔹Memoria RAM (El espacio de trabajo):
(Random Access Memory) es volátil: si el programa termina o la computadora se apaga, todo lo que hay allí se borra instantáneamente. Sin embargo, es extremadamente rápida. El procesador lee y escribe en la RAM casi en tiempo real, en esta se guarda por ejemplo:
Variables y Objetos: "jugador_1 = Jugador("Héroe")", ese objeto y todos sus atributos viven físicamente en la RAM.
Consumo de APIs: Cuando haces una petición GET mediante la librería requests, el archivo JSON se carga en la RAM.

El límite: Un bucle infinito que crea objetos sin parar, o intentar cargar un archivo txt de 10 GB de golpe en una variable, llenarás la RAM. Cuando esto pasa, el sistema operativo se vuelve extremadamente lento o el programa simplemente colapsa (Out of Memory).


## 🔹Almacenamiento (HDD / SSD):
El almacenamiento es persistente (no volátil) y tiene muchísima más capacidad.
Un disco duro tradicional (HDD) usa partes mecánicas y discos magnéticos
Una unidad de estado solida (SSD) usa chips de memoria flash, siendo mucho más rápida. 
Guarda el código fuente y las bases de datos para uso futuro.

extra: Incluso el SSD más rápido es muchísimo más lento que la RAM, la ram tambien se puede usar como almacenamiento(Esto se llama RAM Disk), aunque la tramapa esta en la volatidad propia de la RAM.


* DESINSTALACIÓN = Cuando desinstalas un programa lo que realmente sucede es que el sistema de archivos marca el espacio como "libre" o "disponible". Imagina que el disco duro es un libro y el sistema de archivos es el índice. Al desinstalar, el sistema simplemente tacha el nombre del programa en el índice, pero no arranca las páginas del libro.  El contenido (los bits con la información del programa) sigue ahí físicamente, ocupando el mismo espacio magnético o eléctrico.
*   Sobrescribir físicamente cada bit cada vez que desinstalas un programa tomaría mucho tiempo y desgastaría innecesariamente el disco.

Esto sirve por ejemplo para la Seguridad y Privacidad: Si desarrollas software que maneja datos sensibles (contraseñas, claves criptográficas, datos médicos), saber que un simple "borrar" deja los datos recuperables, se debe implementar funciones de borrado seguro.


# ----PYTHON BASICO----

* print("hola python")
tipos de datos (str = cadena de caracteres, numéricos (float, interger), Estructuras de datos (listas, tuplas sets, diccionarios), booleanos(True, False), NULL/NONE, creo que también existen los números complejos).

* Variables: my_string_variable = "Información"
en las variables se pueden almacenar cualquier tipo de dato (menos las estructuras de datos, esos almacenan de forma distinta los datos).
Las variables se pueden concatenar con "," tanto con otras variables como con datos: print("Este es el valor de:", my_bool_variable)
Dependiendo el lenguaje las variables son mutables, aunque existen opciones (dependiendo e lenguaje) para crear "variables" constantes.

* Operadores: Los operadores son símbolos o palabras clave especifica que le indican al interprete que realice una operación especifica sobre uno o mas valores, con estos podemos manipular datos y realizar cálculos.
Tener en cuenta que ciertos operadores se pueden utilizar también con cadenas de caracteres (str).
OP-Aritmético: + - * / % ** //.
OP-Comparación: < > <= >= == != <>.
OP_Lógicos: AND OR NOT, si uno o mas elementos son true o false devuelve true o false respectivamente del OP_Lógico utilizado.

* Los datos str se pueden dividir en variables, se les puede incrustar variables con: "f" al inicio y "{}", se pueden dividir o invertir con: "[]" ejemplo para invertir: variablestr[::-1].

* Estructuras de datos: Son las formas que hay de organizar almacenar y manipular información en una memoria del pc, cada estructura de datos es diferente y tiene sus pros y sus contras, cosas como la velocidad o el espacio que se usa/requiere; estas son:

* List: Colección ordenada y mutable de datos, los elementos se llaman por el numero índice y se define con [].

* Tuples: Colección ordenada e inmutable de datos, o sea una vez definido los elementos no pueden variar, los elementos se llaman por el índice y se define con ().

* Sets: Colección desordenada y mutable de elementos únicos, lo que significa que no permite duplicados, los sets no mantienen un orden especifico por lo cual no se pueden llamar por su índice, en relación los sets se consideran como un solo objeto por lo que no se puede llamar un objeto especifico y se define con {}.

* Diccionarios: Colección de datos que almacena información en pares "clave-valor", los elementos se llaman por su clave y adentro de esta están los datos llamados "valor", el diccionario se define con {clave:valores, calve2:valores}.

* Estructuras de control: ejecuta un bloque de código dependiendo el cumplimiento o no de una condición establecida; estas son:

* Secuenciales: Ejecutan instrucciones una tras otra en el orden en que están escritas, la base estándar de cualquier programa.

* Condicionales (Selección): Permiten ejecutar bloques de código específicos dependiendo de si una condición es verdadera o falsa. (if/else - switch/case).

* Iterativas (Repetición): Permiten crear bucles y repetir la ejecución de un bloque de código mientras se cumpla una condición o un número determinado de veces. (for, while - do/while)

* Funciones: bloques de código reutilizable que realiza una tarea especifica y puede ser llamado desde cualquier diferentes partes del programa con un nombre único que le asignamos

* Exceptions(manejo de errores): la forma en la que se manejan los errores que si o si saltaran, ya sea ignorandolos o manejarlos utilizamos palabras claves: 
try = código que puede fallar
except = que hacer si falla
(con python tambien se puede usar "else" y "finally").

* Para entender la terminal y saber como controlar los errores hay que saber las excepciones/Errores mas comunes, como:
    * SyntaxError
    * NameError
    * TypeError
    * ImportError
    * ValueError
    * IndexError
    * ModuleNotFoundError
    * AttributeError
    * KeyError


* Modulos: Son archivos con extensión .py que contiene código reutilizable (funciones, clases o cualquier otro código valido), los modulos se llaman con: import "modulo" (o from "modulo" import "función")


# ----PYTHON INTERMEDIO----

## 🔸Módulo para administrar las fechas:

Importar el modulo "datetime" sirve para manipular fechas, horas y zonas horarias de manera eficiente, sus principales funcionalidades y clases son:
* date = para fechas(año, mes, día).
* time = para horas(hora, minuto, segundo).
* datetime = combina las fechas y horas.
* timedelta = aritmética temporal(representa duraciones, se usa para sumar/restar intervalos de tiempo).
* strftime y strptime = convierte objetos de fecha y hora a cadenas de texto.
* timezone = gestión de zonas horarias

## 🔸List Comprehension (Comprensión de Lista):

forma compacta de crear listas en python a partir de un iterable, aplicando una expresión y opcionalmente una condición, como son legibles y eficientes son comunes en python, su estructura básica es: [expresión "for" elemento "in" iterable "if" condición].
Con esto podemos transformar datos, Filtrar elementos, Transformar + filtrar, por ejemplo:
Convertir texto a minúsculas:
```python 
nombres = ["Ana", "JUAN", "PeDro"]
normalizados = [n.lower() for n in nombres]
```
## 🔸Lambdas:

Son funciones anónimas(sin nombre) se define en una sola expresión, se usa para operaciones simples, cortas y puntuales también pueden estar dentro de una función, su sintaxis: lambdas argumentos: expresión.
ejemplo: lambda para sumar dos numero:
sum_two_values = lambda first_value, second_value: print(first_value + second_value).

higher order functions:

funciones que reciben una o más funciones como argumento y/o devuelva una función como resultado(o sea una función de orden superior opera sobre otra función).
ejemplo donde pasamos una función por medio de los parámetros de otra función:
```python
def operar(a, b, operador):
    return operador(a,b)

def sumar(x, y):
    return x + y

def multiplicar(x, y):
    return x * y
``` 
## 🔸CLOSURES:

Un closure es una función que encapsula (cierra sobre) su entorno léxico, se puede simplificar como una función que devuelve una función, ejemplo:
```python
def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)    -> (Es como si add_closure se convirtiera en la función que esta dentro de "def sum_ten").
print(add_closure(5)) 
```
tambien estan Built-in Higher Order Functions (Funciones de orden superior que ya existen en el propio lenguaje):
* Map = transformación de datos
* Filter = selección / filtrado
* sorted = Ordena elementos de un iterable

## 🔸FILE HANDLING(manejo de archivos):

Conjunto de operaciones que permite al programa crear, abrir, leer, escribir, modificar y cerrar archivos, para abrir archivos usamos la función "open()" su sintaxis es:
open(nombre_archivo, modo) = el modo indica que quieres hacer con el archivo

y una forma de editar (o agregar, en este caso texto) seria:
```python
with open("intermediate/my_file.txt","a") as file_2:
    file_2.write("\ny Swift")
```
"with" sirve para simplificar la gestión de recursos, se asegura la ejecución automática de métodos de limpieza como(.close()) al salir del bloque, del mismo modo ayuda a la seguridad, limpieza y legibilidad.


Algunos de los modos que existen:
* "r" = Read (leer) - modo por defecto
* "w" = Write (escribir) - borra el contenido si ya existe
* "a" = Append (agregar al final)
* "x" = Crear archivo (error si ya existe)
* "b" = Modo binario
* "t" = Modo texto (por defecto)

Ademas es importante conocer y dicernir los formatos de textos utilizados:
* json = formato de texto estándar para almacenar y transferir datos de manera sencilla y legible
* csv = archivos tipo excel
* * Tambien se puede trabajar con archivos binarios.

## 🔸REGULAR EXPRESSIONS (Expresiones regulares):

lenguaje formal para describir patrones en texto, es como un filtro en el que se especifica o se filtra parametros en un texto, en python se tiene que importar con el modulo "re" y se usan las funciones del modulo como:
* re.search() = Escanea toda la cadena y devuelve el primer objeto Match encontrado o None.
* re.findall() = Devuelve una lista con todas las coincidencias no superpuestas del patrón en la cadena.
* re.sub() = Sustituye todas las ocurrencias del patrón por una cadena de reemplazo (o el resultado de una función).
* re.match() = Específica para validar si una cadena COMIENZA con un patrón determinado.
etc.

## 🔸Python package manager (gestor de paquetes para python):

Explicación de que son y como manejar dependencias: Una dependencia es cualquier librería, framework o módulo externo que se instala para aprovechar funcionalidad ya creada. para gestionarlas utilizamos gestores, el mas "clasico" seria pip(gestor de paquetes oficial de Python).

Desde la terminal: "pip install pip" para instalar, descargamos dependencias con "pip install numpy"
tambien hay otras "funciones" con pip:
* pip list = muestra las librerias/dependencias que tenemos en el sistema.
* pip uninstall "paquete" = desinstala cualquier dependencia.
* pip install --upgrade "paquete" = actializa la dependencia/paquete.
* pip install "paquete"==1.2.3 = instala una versión especifica.
* pip show "paquete" = información de la dependencia.
* pip check: Verifica si hay dependencias rotas o conflictos de versiones.

tambien se suele importar el modulo "request" para facilitar enormemente el encio de solicitud HTTP.
investigar que es package = Un paquete en Python es simplemente una carpeta que contiene varios módulos (archivos .py) y que tiene un archivo especial llamado __init__.py(aunque ya no es necesario). Esto permite importar cosas estructuradamente como from mi_paquete.matematicas import sumar.


## 🔸ENTORNO VIRTUAL:

Un entorno virtual es un directorio aislado que contiene su propia instalación de Python y un conjunto independiente de paquetes (librerías).  Su función principal es evitar conflictos entre las dependencias de diferentes proyectos.

Para crearlo, se ingresa a la carpeta del proyecto, luego en la terminal escribir "python -m venv venv" = este comando crea un entorno virtual de Python en una carpeta llamada venv.
Para empezar a trabajar con el entorno recién creado y trabajar/descargar las librerias, se debe ejecutar el archivo de activación que en windows suele ser: venv/scripts/activate	(se debe activar cada vez que se habra una terminal o se reinicie el computador).
Por cierto si se hace un push y se sube a GitHub solo se subiran los archivos del proyecto. No se subira la carpeta del entorno virtual (venv/ o .venv/) ni las librerías instaladas dentro de ella.


## 🔸METODOLOGIAS DE PROGRAMACIÓN:

Son marcos de trabajo estructurados que definen cómo se planifica, ejecuta y controla el ciclo de vida de un proyecto tecnológico. son como las reglas o pautas que hay que seguir para estructurar bien el código, estas se clasifican en dos grupos:


## 🔹Metodologías Tradicionales (Predictivas):
Se caracterizan por ser secuenciales y rígidas; El proyecto se divide  en dases que deben completarse una tras otra, no se puede avanzar a la siguiente sin haber terminafo la anterior. son ideales para proyectos con requisitos muy claros y estables, por jemplo:

* Cascada (Waterfall): Es la más clásica. Sigue un flujo lineal: requisitos → diseño → implementación → pruebas → mantenimiento. Cualquier cambio requiere volver al inicio.

* Espiral: Combina la estructura de la cascada con la evaluación continua de riesgos. Es útil en proyectos grandes y complejos donde la seguridad y el riesgo son críticos.

* Prototipado: Se centra en crear versiones preliminares (prototipos) para validar requisitos con el cliente antes del desarrollo final. 

## 🔹Metodologías Ágiles (Adaptativas):
Son flexibles, se basan en iteraciones cortas(ciclos de trabajo) que permiten entregar valor al cliente frecuentemente y adaptarse a cambios sobre la marcha, algunas son:

* Scrum: La más popular. Organiza el trabajo en Sprints (ciclos de 2 a 4 semanas).  Define roles específicos y se centra en reuniones diarias para sincronizar al equipo.

* Kanban: se basa en la visualización del flujo de trabajo mediante un tablero (pendiente, en curso, terminado). Limita la cantidad de trabajo en proceso para evitar cuellos de botella y mejorar la eficiencia continua.

* XP (Programación Extrema): Se enfoca en la calidad técnica del código y la satisfacción del cliente mediante prácticas como la programación en pareja y el desarrollo guiado por pruebas (TDD). Ideal para proyectos con plazos muy cortos y requisitos cambiantes.

* Lean: Se centra en la eliminación de desperdicios (actividades que no aportan valor) y en la optimización del flujo de entrega.


## 🔸Paradigmas: 

Los paradigmas son estilos o enfoques fundamentales que dictan cómo se estructura y escribe el código para resolver problemas. o sea son "filosofias" que definen las reglas, la lógica y la forma de pensar al desarrollar al software, algunos ejemplos:

__Programación Orientada a Objetos (POO)__ = Es el estándar indiscutible para el desarrollo de software empresarial, videojuegos y aplicaciones grandes.
* dónde se usa: Sistemas bancarios, aplicaciones Android (Java/Kotlin), motores de videojuegos (C++/C#) y backend corporativo.
* Lenguajes clave: Java, C#, C++, Python. 

__Programación Funcional__ = Ha pasado de ser académica a ser esencial debido al auge de la Inteligencia Artificial y el Big Data.
* Dónde se usa: Ciencia de datos, aprendizaje automático (Machine Learning), sistemas financieros de alta frecuencia y procesamiento en la nube.
Lenguajes clave: Python (líder en IA), JavaScript (para web moderna), Scala, Haskell.

__Programación Imperativa/Procedimental__ = Es la base de todo.  Aunque parezca antigua, es crítica para el rendimiento puro y el control del hardware.
* Dónde se usa: Sistemas operativos (Windows, Linux, macOS), drivers, dispositivos embebidos (IoT) y motores de bases de datos.
Lenguajes clave: C, Rust (la evolución moderna y segura de C), Go


# 🔸POO (programación orientada a objetos): 

paradigma que organiza el código en unidades llamadas objetos, los cuales combinan datos y funcionalidad.

## 🔹Conceptos fundamentales de POO:

1. La clase (El Molde) = No es el objeto, es el diseño o plano, es la definición de como será.

2. El Objeto (La Instancia) =  Es lo que construimos usando la clase, es el elemento real que vive en la memoria del pc. Ejemplo: La casa fisica donde vive alguien.

3. Atrinutos (Variales) = Son las caracteristicas del objeto: color, puertas, modelo, etc.

4. Métodos (Funciones) = Son las acciones que el objeto puede realizar: encender(), tocar bocina, etc.

## 🔹Sintaxis en python:
```python
class Perro:
    # El constructor (inicializa al perro)
    def __init__(self, nombre, raza):
        self.nombre = nombre  # Atributo
        self.raza = raza      # Atributo

    # Un método (acción)
    def ladrar(self):
        return f"{self.nombre} dice: ¡Guau!"

# Crear un objeto (instanciar)
mi_perro = Perro("Rex", "Pastor Alemán")
```

# 🔸Los 4 Pilares de POO:

## 🔹Encapsulamiento: 
Esconder los detalles internos del objeto para que nadie los rompa por accidente:
Existen tipos: publico, protegido y privado. El publico es el que se puede acceder desde cualquier parte del programa, el protegido es el que se puede acceder desde la clase y sus subclases, y el privado es el que solo se puede acceder desde la clase:

* Público: self.nombre (Acceso libre).
* Protegido: self._nombre (Un solo guion bajo). Indica: "Esto es interno, no deberías tocarlo desde afuera".
* Privado: self.__nombre (Dos guiones bajos).

Para acceder a los datos encapsulados tenemos que utilizar: "Getters"(obtenedor) y "Setters"(Establecedor/Definidor/modificador)

ejemplo de sintaxis:
```python
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo interno (convención con guion bajo)
        self._edad = edad

    # 1. GETTER: Se accede como 'obj.nombre'
    @property
    def nombre(self):
        return self._nombre

    # 2. SETTER: Se asigna como 'obj.nombre = "Nuevo"'
    @nombre.setter
    def nombre(self, nuevo_valor):
        if not isinstance(nuevo_valor, str):
            raise ValueError("El nombre debe ser una cadena de texto.")
        self._nombre = nuevo_valor

    # 3. DELETER: Se activa con 'del obj.nombre'
    @nombre.deleter
    def nombre(self):
        print(f"Eliminando el nombre: {self._nombre}")
        self._nombre = None

# --- Uso ---
p = Persona("Ana", 30)

# Leer (ejecuta el getter)
print(p.nombre)  # Salida: Ana

# Escribir (ejecuta el setter con validación)
p.nombre = "Carlos" 
# p.nombre = 123  # Lanzaría ValueError

# Eliminar (ejecuta el deleter)
del p.nombre   
```
💎en Python el encapsulamiento privado (__atributo) no es estrictamente privado como en Java en Python se confía en que si un dev ve un _ o __, sabe que no debe tocarlo desde afuera.


## 🔹Abstracción: 
Mostrar solo lo necesario, en términos técnicos, la abstracción consiste en ocultar los detalles de implementación complejos y mostrar solo las funcionalidades necesarias al usuario.No necesitas saber cómo funciona el motor para manejar el coche.


## 🔹Herencia y herencia multiple: 
Crear clases nuevas basadas en clases existentes (ej. una clase Camion que hereda de auto)

la herencia es la herramienta que te permite crear moldes(clases) nuevos basados en otros que ya existen, sin tener que escribir todo desde cero, esto se crea metiendo la clase entre parentesis: Nueva_clase(Clase_a_heredar).

tambien existe la herencia multiple: se pueden heredar multiples clases, pero para heredar los "metodos" tenemos que hacer una referencia directa a las clases padres:
```
clase_heredada_1.__init__(self, nombre, edad, nacionalidad)
clase_heredada_2.__init__(self, habilidad)
```
Extra: super() es una función muy utiliza y le dice al programa que es un metodo de arriba o de una clase heredada, ejemplo de uso: 
```
return print(f"Hola soy: {self.nombre}, {super().mostrar_habilidad()} y trabajo en {self.empresa}")
```
tambien existen funciones como:
* issubclass() = con esta función se verifica si es una subclase
* isinstance() = con esta función se verifica si un objeto es una instancia de una clase.



## 🔹MRO: 

Method Resolution Order (Orden de Resolución de Métodos) son basicamente las reglas que utiliza python para decidir el orden en que va a buscar un método o atributo dentro de una jerarquia de clases. Funciona utilizando el algoritmo llamado C3 Linearization.

1. Los hijos primero: Python siempre buscará el método en la clase actual antes de buscar en sus clases padre

2. De izquierda a derecha:
En la herencia múltiple (ej. class D(B, C):), Python buscará primero en la clase de la izquierda (B) y luego en la de la derecha (C)

3. Las clases base compartidas van al final: Si varias clases comparten un mismo padre (la clase A en el problema del diamante), Python solo revisará esa clase padre una vez que haya revisado todos sus hijos

__Tambien se puede ver MRO exacto utilizando el método:__ .mro() o el atributo .__mro__



## 🔹Polimorfismo: 
La capacidad de que diferentes objetos respondan al mismo comando de formas distintas

Poli (muchos) y morfismo (formas) = En programación, es la capacidad de que objetos de diferentes clases respondan al mismo mensaje (método) de maneras distintas.
ejemplo: 
```python
class Gato():
    def sonido(self):
        return "Miau"
    
class Perro():
    def sonido(self):
        return "Guau"

def hacer_sonido(animal):
        print(animal.sonido())
```
El polimorfismo se manifiesta principalmente a través de cuatro tipos, aprovechando su naturaleza dinámica:

* Duck Typing: El comportamiento depende de los métodos que tenga el objeto

* Sobrescritura de Métodos (Override)

* Sobrecarga de Operadores

* Sobrecarga de Funciones (Simulada)


## 🔸CLASES ABSTRACTAS: 

Es una clase que funciona como plantilla obligatoria para otras clases. Su propósito principal es definir una estructura común y comportamientos base que las clases hijas (subclases) deben heredar e implementar.
la sintaxis es: importar el modulo abc o from abc import ABC, abstractmethod.
Luego se crea una clase "heredada" de ABC, así: 
```python
class Persona(ABC):
	def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```
paso siguiente definir normalmente los atributos y métodos, los métodos que sean obligatorios heredar se les pone encima el decorador @abstractmethod.
y para implementar la subclase(clase hija):
```python
class Estudiante(Persona):
	def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
```
Las clases abstractas se utilizan únicamente cuando necesitas garantizar que todas las subclases implementen una funcionalidad específica.


🔸Extras:

## 🔹DECORADORES: 
Es una función que modifica o extiende el comportamiento de otra función o clase sin alterar su código original, se aplica usando la sintaxis @nombre_decorador (la función que creamos) justo encima de la definición de la función, la forma optima de ejecutarlos:
```python
@decorador
def saludo():
    print("Hola como estas")

saludo()
```

## 🔹PROPIEDADES(properties):
Las propiedades sirven para controlar y validar el acceso a los datos de una clase manteniendo una sintaxis limpia y natural. sintetizan y simplifican el uso de getters y setters.
No confundir estas propiedades con variable o las propiedades de un objeto. (literalmente son getters y setters(y deleiters))

Para decirle a la clase que vamos a usar un getter usamos: @property = es un decorador que permite definir un método como un getter, de modo que se pueda acceder a él como si fuera un atributo en lugar de llamarlo como una función

Para crear el setter se usa: @nombre_de_la_propiedad.setter, donde nombre_de_la_propiedad es el nombre del atributo que deseas controlar

Despues seguirian los @deleters = @deleter es un decorador en Python que se utiliza junto con @property para definir la lógica que se ejecuta cuando se elimina una propiedad de una instancia de clase (usando la sentencia del), se crea con = nombre_de_la_propiedad.deleter



## 🔹MÉTODOS ESPECIALES (abreviatura de double underscore o "doble guion bajo") o métodos mágicos:
Son funciones predefinidas en Python que permiten personalizar el comportamiento de tus objetos.
Gracias a ellos se puede configurar el comportamiento tanto de operadores(+, -, ==), funciones incorporadas(len(), str(), print()) y contextos especiales(iteración, gestión de contexto), o sea se configura cómo tus objetos interactúan con casi todas las características nativas de Python.
Algunos de los mas utilizados:

### 🔹Inicialización y Representación = Controlan la creación del objeto y cómo se muestra como texto:
* __init__(self, ...) = Es el constructor.  Se ejecuta automáticamente al crear una nueva instancia.
* __str__(self) = Define la representación "legible" del objeto, debe devolver una cadena amigable para el usuario final.
* __repr__(self): Define la representación "oficial" o técnica, Su objetivo es mostrar una cadena que, idealmente, permita recrear el objeto

### 🔹Operadores Aritméticos y de Comparación = Permiten usar símbolos matemáticos y lógicos con tus objetos (sobrecarga de operadores):

* __add__(self, otro) = Habilita el uso del operador suma (+). 
* __sub__(self, otro) = Habilita la resta (-). 
* __mul__(self, otro) = Habilita la multiplicación (*).
etc.

### 🔹Contenedores y Colecciones = Hacen que tu objeto se comporte como una lista, diccionario o colección:
* __len__(self) = Permite usar la función len(obj) para obtener el tamaño del objeto.
* __getitem__(self, clave) = Permite acceder a elementos usando corchetes (obj[indice]).
etc.



# 🔸PRINCIPIOS SOLID: 
Son el estándar de oro para escribir código limpio, mantenible y escalable. 5 principios/reglas SOLID (Responsabilidad Única, Abierto/Cerrado, Sustitución de Liskov, Segregación de Interfaces e Inversión de Dependencias).

### 🔹SRP (Single Responsibility Principle): Una clase o módulo debe tener una sola razón para cambiar, es decir, debe enfocarse en una única funcionalidad o responsabilidad.

### 🔹OCP (Open/Closed Principle): Las entidades de software deben estar abiertas para su extensión (permitir nuevas funcionalidades) pero cerradas para su modificación (sin alterar el código existente).

### 🔹LSP (Liskov Substitution Principl): Define que los objetos de una superclase deben ser reemplazables por instancias de sus subclases sin alterar el correcto funcionamiento del programa.

### 🔹ISP (Interface Segregation Principle): Sugiere que muchas interfaces específicas son mejores que una interfaz de propósito general, evitando que los clientes se vean forzados a depender de métodos que no utilizan.("interfaz" se estan refiriendo a las clases abstractas)
* Aplicarlo correctamente:
Evitar interfaces "gordas"
Alta cohesión y bajo acoplamiento

### 🔹DIP (Dependency Inversion Principle): Establece que los módulos de alto nivel no deben depender de módulos de bajo nivel, sino ambos deben depender de abstracciones, y las abstracciones no deben depender de los detalles (implementaciones concretas) deben depender de las abstracciones.
* Módulos de Alto Nivel: Contienen la lógica de negocio compleja y las políticas principales de la aplicación (el "qué" hace el sistema).  Son los que aportan valor directo.
Módulos de Bajo Nivel: Se encargan de los detalles operativos como acceso a bases de datos, llamadas a APIs, manejo de archivos o logging (el "cómo" se hacen las tareas). 


# 🔸Consumo de APIs y JSON:
JSON(JavaScript Object Notation) es el idioma universal de las APIs, es simplemente texto estructurado. Las APIs lo usan porque cualquier lenguaje de programación puede leerlo, JSON es prácticamente idéntico a un diccionario de Python.

## 🔹Peticiones HTTP: 
GET vs POST = Cuando te comunicas con una API, usas el protocolo HTTP. Los dos métodos que usarás el 95% de las veces son:

GET (Obtener): Lo usas para pedir información. "Oye servidor, dame los datos del usuario 5". No envías datos complejos, solo pides.

POST (Enviar/Crear): Lo usas cuando necesitas enviar información al servidor para que la procese (por ejemplo, enviarle un "prompt" a un modelo de lenguaje para que te devuelva una respuesta).

Para hacer esto en Python, usamos la librería externa requests. Ejemplo de peticion simple:
import requests
url = "https://jsonplaceholder.typicode.com/users/1"

### Hacemos la petición GET
```python
respuesta = requests.get(url)

# Verificamos si la petición fue exitosa (Código 200 significa OK)
if respuesta.status_code == 200:
    # Convertimos la respuesta de texto JSON a un diccionario de Python
    datos = respuesta.json() 
    print(f"Nombre: {datos['name']}")
else:
    print(f"Hubo un error: {respuesta.status_code}")
```

### 🔹Autenticación y POST (El estándar para IA):
para usar la api de muchos servicios profesionales, el servidor necesita saber quién eres y si tienes permiso(o saldo) para usarlo. Para esto usamos las API Keys y los Headers(Los Headers (Cabeceras) son metadatos ocultos que viajan con tu petición).


## 🔸TESTING BASICÓ: 

🔹XP (Extreme Programming) = Es una metodología ágil de desarrollo de software. Su objetivo es mejorar la calidad del código y la capacidad de respuesta ante los cambios del cliente.
* Programación en pareja: Dos trabajan en la misma máquina para mejorar la calidad y compartir conocimiento.
* Desarrollo guiado por pruebas (TDD): Escribir pruebas automatizadas antes del código de producción.
* Integración continua: Fusionar el código frecuentemente para detectar errores tempranamente
* Diseño simple y refactorización: Mantener el código limpio y adaptable sin complejidad innecesaria. 


🔹TDD (Test-Driven Development): Significa Desarrollo Guiado por Pruebas. En lugar de escribir tu código y luego probarlo, escribes la prueba primero. El ciclo de TDD (conocido como Red-Green-Refactor) funciona así:

* Red: Escribes un test que falla (porque la función aún no existe).

* Green: Escribes el código mínimo necesario para que el test pase.

* Refactor: Limpias y mejoras el código aplicando buenas prácticas (como SOLID), con la tranquilidad de que si rompes algo, el test te avisará inmediatamente.

🔹TEST UNITARIO: Un test unitario aísla una pequeña parte de tu programa (una función, un método o una clase) y verifica que se comporte exactamente como esperas.

Si estás creando un sistema estructurado con objetos (como un juego de rol o un SaaS), los tests te dan una red de seguridad. Si mañana decides cambiar la lógica interna de cómo un personaje recibe daño o cómo se calcula una factura, corres tus tests. Si todos pasan, sabes que no rompiste nada en el proceso.

🔹Cómo hacer un test básico en Python: Tenemos esta clase simple en el proyecto:
```python
# logica.py
class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud

    def recibir_dano(self, cantidad):
        self.salud -= cantidad
        if self.salud < 0:
            self.salud = 0

```
Opción 1: Probamos esta funcion usando el modulo nativo "unittest" = Está inspirado en Java, por lo que requiere crear clases y usar métodos específicos como assertEqual.

Opción 2: Usando la libreria externa "pytest" = es la herramienta estándar en la industria moderna de Python. Su sintaxis es mucho más limpia, directa y "pythónica" porque usa la palabra reservada nativa assert:
```python
from logica import Personaje

def test_recibir_dano_reduce_salud():
    guerrero = Personaje("Arthur", 100)
    guerrero.recibir_dano(30)
    
    assert guerrero.salud == 70

def test_salud_no_baja_de_cero():
    mago = Personaje("Merlín", 50)
    mago.recibir_dano(100)
    
    assert mago.salud == 0

```
Para ejecutarlo, simplemente abres tu terminal, navegas a la carpeta y escribes pytest.


## El Problema de las Dependencias
Cuando empiezas a conectar diferentes partes de tu código, te encuentras con un desafío: ¿cómo pruebas una sola pieza sin arrastrar a las demás?
Imagina que estás construyendo tu juego de rol y tienes una clase Heroe que necesita usar una clase Dado para calcular si un ataque es crítico, o una clase BaseDeDatos para guardar el progreso.

Si haces un test unitario de la clase Heroe usando el Dado real, el resultado será aleatorio. A veces el test pasará y a veces fallará. Además, si la clase Dado tiene un error, tu test de Heroe va a fallar, haciéndote creer que el problema está en el héroe cuando no es así.

Un test unitario debe probar una sola "unidad" (el héroe) en aislamiento.

## ¿Qué es un Mock?
Un mock (o un "objeto simulado") es literalmente un doble de acción para tu código.

Es un objeto falso que tú creas exclusivamente para el test. Este objeto se disfraza de la dependencia real (como el Dado o un Arma), pero en lugar de tener lógica compleja, tú le dices exactamente cómo debe comportarse para ese test en específico.

## Cómo usar un Mock en Python
Python trae una herramienta maravillosa en su librería estándar llamada unittest.mock. Funciona perfectamente con pytest.
#### Código en producción:
```python
# logica.py

class Arma:
    def calcular_dano(self):
        # Imagina que esto hace cálculos complejos de daño y estadísticas
        return 50

class Heroe:
    def __init__(self, nombre, arma):
        self.nombre = nombre
        self.arma = arma  # <--- Dependencia inyectada

    def atacar(self):
        # El héroe depende del arma para saber cuánto daño hace
        dano = self.arma.calcular_dano()
        return f"{self.nombre} ataca causando {dano} puntos de daño."
```
#### Y así es como harías el test unitario aislando al Heroe con un mock:
```python
# test_logica.py
from unittest.mock import Mock
from logica import Heroe

def test_heroe_ataca_usando_arma():
    # 1. SETUP: Creamos el mock (el doble de acción) del arma
    arma_falsa = Mock()
    
    # Le ordenamos al mock qué debe responder cuando alguien llame a su método
    arma_falsa.calcular_dano.return_value = 100 
    
    # Inyectamos el arma falsa en nuestro héroe
    guerrero = Heroe("Conan", arma_falsa)
    
    # 2. ACT: Ejecutamos el método que queremos probar
    resultado = guerrero.atacar()
    
    # 3. ASSERT: Comprobamos que el héroe armó correctamente el mensaje
    assert resultado == "Conan ataca causando 100 puntos de daño."
    
    # Extra mágico de los mocks: Podemos verificar si el héroe realmente intentó usar el arma
    arma_falsa.calcular_dano.assert_called_once()
```

Pregunta a responder:
¿Cómo se aplica este concepto de mocks para probar eventos en una interfaz gráfica (GUI) sin que se abra la ventana físicamente durante el test?




🔹Estudiar mas sobre las apis y como conectarlas en el .txt de apis

🔹aprenderme o al menos conocer funciones mas utilizadas de python (aunque dependa del proyecto)
Estudiar y aprender bien las metodologias y paradigmas de programación
tambien las mejores practicas




PROYECTOS: 





💡 Un consejo para empezar:
Elige uno de estos proyectos y ejecútalo dentro de un entorno virtual (venv) limpio. A medida que escribas el código, intenta aplicar la mentalidad de "¿Cómo puedo estructurar esto en clases independientes?" para mantener tu software limpio y fácil de mantener.