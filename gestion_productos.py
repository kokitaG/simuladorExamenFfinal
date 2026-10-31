from producto import Producto, ProductoException


class GestionProductos:
    def __init__(self):
        self.productos = {}

    def registrar_producto(self, producto: Producto) -> bool:
        if producto.codigo in self.productos:
            raise ProductoException(f"El código '{producto.codigo}' ya existe.")
        self.productos[producto.codigo] = producto
        return True

    def buscar_producto(self, codigo: str) -> Producto:
        if codigo not in self.productos:
            raise ProductoException(f"El producto con código '{codigo}' no existe.")
        return self.productos[codigo]

    def actualizar_producto(self, codigo: str, nombre: str = None, precio: float = None, cantidad: int = None) -> bool:
        prod = self.buscar_producto(codigo)
        if nombre is not None:
            prod.nombre = nombre
        if precio is not None:
            prod.precio = precio
        if cantidad is not None:
            prod.cantidad = cantidad
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        self.buscar_producto(codigo)
        del self.productos[codigo]
        return True