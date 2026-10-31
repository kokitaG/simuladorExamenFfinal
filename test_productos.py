import pytest
from producto import Producto, ProductoException
from gestion_productos import GestionProductos

# ==========================================
# SERIE II - 5 PRUEBAS UNITARIAS
# ==========================================

def test_u1_registrar_producto_valido():
    p = Producto("P001", "Laptop", 1200.0, 10)
    assert p.codigo == "P001"
    assert p.nombre == "Laptop"

def test_u2_buscar_en_diccionario():
    gestor = GestionProductos()
    p = Producto("P002", "Mouse", 25.0, 50)
    gestor.productos["P002"] = p
    resultado = gestor.productos.get("P002")
    assert resultado.nombre == "Mouse"

def test_u3_actualizar_atributos_objeto():
    p = Producto("P003", "Teclado", 45.0, 20)
    p.precio = 50.0
    p.cantidad = 15
    assert p.precio == 50.0
    assert p.cantidad == 15

def test_u4_eliminar_del_diccionario():
    gestor = GestionProductos()
    gestor.productos["P004"] = Producto("P004", "Monitor", 300.0, 5)
    del gestor.productos["P004"]
    assert "P004" not in gestor.productos

def test_u5_validacion_precio_negativo():
    with pytest.raises(ProductoException) as exc_info:
        Producto("P005", "Audífonos", -10.0, 5)
    assert "El precio no puede ser negativo." in str(exc_info.value)


# ==========================================
# SERIE II - 5 PRUEBAS DE INTEGRACIÓN
# ==========================================

def test_i1_registrar_y_buscar_producto():
    gestor = GestionProductos()
    p = Producto("INT01", "Impresora", 200.0, 8)
    gestor.registrar_producto(p)
    buscado = gestor.buscar_producto("INT01")
    assert buscado.nombre == "Impresora"

def test_i2_actualizar_y_verificar_cambio():
    gestor = GestionProductos()
    p = Producto("INT02", "Cámara", 500.0, 4)
    gestor.registrar_producto(p)
    gestor.actualizar_producto("INT02", precio=450.0, cantidad=6)
    buscado = gestor.buscar_producto("INT02")
    assert buscado.precio == 450.0
    assert buscado.cantidad == 6

def test_i3_eliminar_y_confirmar_inexistencia():
    gestor = GestionProductos()
    p = Producto("INT03", "Disco Duro", 80.0, 15)
    gestor.registrar_producto(p)
    gestor.eliminar_producto("INT03")
    with pytest.raises(ProductoException):
        gestor.buscar_producto("INT03")

def test_i4_operar_sobre_producto_inexistente():
    gestor = GestionProductos()
    with pytest.raises(ProductoException) as exc_info:
        gestor.actualizar_producto("NO_EXISTE", precio=100.0)
    assert "El producto con código 'NO_EXISTE' no existe." in str(exc_info.value)

def test_i5_registrar_codigo_duplicado():
    gestor = GestionProductos()
    p1 = Producto("INT05", "Silla Gamers", 150.0, 10)
    p2 = Producto("INT05", "Silla Oficina", 120.0, 5)
    gestor.registrar_producto(p1)
    with pytest.raises(ProductoException) as exc_info:
        gestor.registrar_producto(p2)
    assert "El código 'INT05' ya existe." in str(exc_info.value)