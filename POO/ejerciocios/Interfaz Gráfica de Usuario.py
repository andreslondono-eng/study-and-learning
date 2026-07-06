#Interfaz Gráfica de Usuario (GUI)


# tkinter es la librería estándar de Python para crear interfaces gráficas, lo que significa que no se necesita instalar nada extra con "pip"


import tkinter as tk

class VentanaPersonaje:
    def __init__(self, ventana_principal):
        # 1. Configuración de la ventana base
        self.ventana = ventana_principal
        self.ventana.title("Menú del Personaje")
        self.ventana.geometry("350x250") # Ancho x Alto en píxeles
        self.ventana.config(bg="#2b2b2b") # Color de fondo oscuro
        
        # Atributo del personaje para la lógica
        self.hp_actual = 50
        self.hp_maximo = 100
        
        # 2. Creación de los Widgets (Elementos visuales)
        # Etiqueta de Título
        self.etiqueta_nombre = tk.Label(
            self.ventana, 
            text="Héroe: Arthur", 
            font=("Arial", 16, "bold"), 
            bg="#2b2b2b", 
            fg="white"
        )
        # pack() es el método para colocar el elemento en la ventana
        self.etiqueta_nombre.pack(pady=20) 
        
        # Etiqueta de Vida (HP)
        self.etiqueta_hp = tk.Label(
            self.ventana, 
            text=f"Salud: {self.hp_actual} / {self.hp_maximo}", 
            font=("Arial", 14), 
            bg="#2b2b2b", 
            fg="#ff4d4d" # Rojo
        )
        self.etiqueta_hp.pack(pady=10)
        
        # Botón para curar
        self.boton_curar = tk.Button(
            self.ventana, 
            text="Tomar Poción de Vida", 
            font=("Arial", 12),
            bg="#4caf50", # Verde
            fg="white",
            command=self.curar_personaje # Conectamos el botón a un método (sin paréntesis)
        )
        self.boton_curar.pack(pady=20)

    # 3. Lógica y Eventos
    def curar_personaje(self):
        """Método que se ejecuta cuando se hace clic en el botón."""
        if self.hp_actual < self.hp_maximo:
            self.hp_actual += 20
            # Evitamos que la vida pase del máximo
            if self.hp_actual > self.hp_maximo:
                self.hp_actual = self.hp_maximo
                
            # Actualizamos el texto visual de la etiqueta
            self.etiqueta_hp.config(text=f"Salud: {self.hp_actual} / {self.hp_maximo}")
            
            # Si el HP llega al máximo, deshabilitamos el botón
            if self.hp_actual == self.hp_maximo:
                self.boton_curar.config(state="disabled", bg="gray")

# --- Ejecución del programa ---
if __name__ == "__main__":
    # Creamos la raíz (la ventana principal del sistema operativo)
    raiz = tk.Tk()
    
    # Instanciamos nuestra clase y le pasamos la ventana principal
    app = VentanaPersonaje(raiz)
    
    # Iniciamos el "Event Loop" (bucle de eventos)
    # Esto mantiene la ventana abierta y esperando a que el usuario haga clic en algo
    raiz.mainloop()
    
"""
Conceptos Clave de este Código:
Widgets: En tkinter, todo elemento visual se llama widget. Los más comunes son Label (para mostrar texto o imágenes), Button (botones interactivos) y Entry (cajas de texto para que el usuario escriba).

Gestor de Geometría (.pack()): Cuando creas un widget, este no aparece mágicamente en la pantalla. Debes decirle a Python cómo posicionarlo. El método .pack() lo apila de forma vertical (puedes usar
pady para darle márgenes). También existen .grid() (para posicionar por filas y columnas) y .place() (para coordenadas X, Y exactas).

Eventos (command=): Para que un botón haga algo, se le pasa el nombre de una función o método al parámetro command. Fíjate que al conectar self.curar_personaje no se le ponen paréntesis al final, 
porque solo queremos referenciar el método, no ejecutarlo inmediatamente.

El Bucle Principal (mainloop()): A diferencia de un script normal que se ejecuta de arriba a abajo y termina, una interfaz gráfica se queda "congelada" en la línea mainloop() escuchando permanentemente
si mueves el ratón, haces clic o escribes algo.

¿Te gustaría que veamos cómo separar completamente la lógica interna (los datos y reglas de tu proyecto) de la interfaz visual usando el principio de responsabilidad única?

"""
