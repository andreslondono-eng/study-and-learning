#sistema de inventario usando POO

class Producto:
    def __init__(self, id: int, nombre: str, precio: float, cantidad: int):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def __str__(self):
        return f"Producto(id={self.id}, nombre='{self.nombre}', precio={self.precio}, cantidad={self.cantidad})"


class Inventario:
    def __init__(self):
        self.productos = {}
        
    def agregar_producto(self, producto: Producto):
        if producto.id in self.productos:
            print(f"El producto con id {producto.id} ya existe, Actualizando cantidad.")
            self.productos[producto.id].cantidad += producto.cantidad
        else:
            self.productos[producto.id] = producto
            print(f"El producto '{producto.nombre}', con el id '{producto.id}' fue agregado al inventario")
        
    def eliminar_producto(self, id):
        if id in self.productos:
            nombre_producto = self.productos[id].nombre     #como exactamente se encuentra el nombre?
            del self.productos[id]
            print(f"El producto {nombre_producto}, con el id {id} fue eliminado")
        else:
            print("producto no encontrado")

    def actualizar_producto(self, id, cantidad, precio=None):
        if id in self.productos: 
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio
                print(f"Actualización para el producto de id {id}.")

            print(f"Cantidad actual de '{self.productos[id].nombre}': {self.productos[id].cantidad}.")
            print(f"precio actual de '{self.productos[id].nombre}': {self.productos[id].precio}.")
        else:
            print("producto no encontrado")

    def listar_producto(self):
        for producto in self.productos.values():
            print(producto)
        
        

inventario1 = Inventario()
producto1 = Producto(1, "Laptop", 999.99, 150)
producto2 = Producto(2, "Manzana", 10, 100)
print(inventario1.productos)
#como podria hacer que el metodo resiva varios productos a la vez? algo como: agregar_producto(producto1,producto2)
inventario1.agregar_producto(producto1)
inventario1.agregar_producto(producto2)
inventario1.agregar_producto(producto2)
inventario1.actualizar_producto(1, 1000)
inventario1.listar_producto()
inventario1.eliminar_producto(1)
print(inventario1.productos)
inventario1.listar_producto()

inventario1.actualizar_producto(2, 25)