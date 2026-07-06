#En términos técnicos, la abstracción consiste en ocultar los detalles de implementación complejos y mostrar solo las funcionalidades necesarias al usuario.
#o sea ocultar la complejidad interna de un sistema.
class Auto:
    def __init__(self):
        self.estado = "apagado"
        
    def encender(self):
        self._estado = "encendido"
        print("El auto esta encendido")
        
    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo el auto")
        
mi_auto = Auto()

mi_auto.conducir

#esto es un ejemplo de abstracción porque el usuario no necesita saber cómo funciona el motor o los sistemas internos del auto para poder conducirlo. Solo interactúa con la interfaz (encender y conducir) sin preocuparse por los detalles técnicos.
















"""
1 - EL CONCEPTO: ¿Qué es realmente?
Abstraer es "extraer lo esencial". Cuando tú usas un objeto, no necesitas saber cómo funciona por dentro; solo necesitas saber qué puedes hacer con él.

Ejemplo de la vida real: Cuando conduces un coche, abstraes toda la complejidad del motor, la inyección de combustible y los pistones.
Solo interactúas con el volante, los pedales y la palanca de cambios. Esa es tu interfaz de abstracción. Si el coche cambia su motor de gasolina por uno eléctrico, tú sigues conduciendo igual. Eso es una abstracción exitosa.

2 - Abstracción vs. Encapsulamiento
A veces se confunden, pero piensa en esto:

Encapsulamiento: Es el mecanismo (los guiones bajos __, los métodos privados) para proteger los datos.
Abstracción: Es el diseño (la clase, qué métodos decides mostrar y cuáles ocultas).

La abstracción es el "qué hace" y el encapsulamiento es el "cómo lo protege".

Tambien la diferencia entre la abstracción en POO (o en progrmación) o sea el concepto y abstracción que es como un mecanismo para crear clases abstractas.
"""
