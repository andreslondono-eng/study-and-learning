"""
Chatbot analizador de sentimientos:

En este proyecto, podrias desarrollar un chatbot en python, que nos pida que le digamos algo y tome eso que
le decimos, analice el sentimiento y nos responda cual sentimos

Este proyecto te daria la oportunidad de trabajar con varios aspectos de la programación orientada a 
objetos (POO),modulos, API, análisis de datos, etc.
"""

#primero creamos un programa pequeño que analise el sentimiento, hacemos esta mini pruena para verificar que funcione

#Tener en cuenta que esta es una biblioteca que funciona en ingles (o sea tengo que pasarle el texto en ingles para que lo "analize" )
from textblob import TextBlob

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self,texto):
        analisis =  TextBlob(texto)
        if analisis.sentiment.polarity > 0:
            return "positivo"
        elif analisis.sentiment.polarity == 0:
            return "neutral"
        else:
            return "negativo"
        
analizador = AnalizadorDeSentimientos()
resultado = analizador.analizar_sentimiento("hello, i bad")
print(resultado)


#la idea es hacerlo con chatGPT, pasarle el texto a chatgpt y que nos devuelva un resultado entre -1 y 1 (0.8, etc) esto lo haria mas preciso




