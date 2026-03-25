def agregar_producto(inventario, nombre, precio, cantidad):
    """Agrega un producto al inventario."""
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    print(" Producto agregado.\n")


def mostrar_inventario(inventario):
    """Muestra todos los productos del inventario."""
    if not inventario:
        print("Inventario vacío.\n")
    else:
        print("=== Inventario ===")
        for indice, producto in enumerate(inventario, start=1):
            print(f"{indice}. {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
        print()


def buscar_producto(inventario, nombre):
    """Busca un producto por nombre y retorna el dict o None."""
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """Actualiza precio y/o cantidad de un producto existente."""
    producto = buscar_producto(inventario, nombre)
    if producto:
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad
        print(" Producto actualizado.\n")
    else:
        print(" Producto no encontrado.\n")


def eliminar_producto(inventario, nombre):
    """Elimina un producto del inventario por nombre."""
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        print(" Producto eliminado.\n")
    else:
        print(" Producto no encontrado.\n")


def calcular_estadisticas(inventario):
    """Calcula estadísticas del inventario y las muestra."""
    if not inventario:
        print("No hay productos.\n")
        return

    unidades_totales = sum(producto["cantidad"] for producto in inventario)
    valor_total = sum(producto["precio"] * producto["cantidad"] for producto in inventario)

    # Encontrar producto más caro y con mayor stock sin usar lambda
    producto_mas_caro = inventario[0]
    producto_mayor_stock = inventario[0]

    for producto in inventario:
        if producto["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = producto
        if producto["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = producto

    print("=== Estadísticas ===")
    print(f"Unidades totales: {unidades_totales}")
    print(f"Valor total del inventario: {valor_total}")
    print(f"Producto más caro: {producto_mas_caro['nombre']} (${producto_mas_caro['precio']})")
    print(f"Producto con mayor stock: {producto_mayor_stock['nombre']} ({producto_mayor_stock['cantidad']} unidades)\n")