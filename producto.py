class ProductoException(Exception):
    """Excepción personalizada para errores del módulo de productos."""
    pass


class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, cantidad: int):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float):
        if valor < 0:
            raise ProductoException("El precio no puede ser negativo.")
        self._precio = valor

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor: int):
        if valor < 0:
            raise ProductoException("La cantidad no puede ser negativa.")
        self._cantidad = valor