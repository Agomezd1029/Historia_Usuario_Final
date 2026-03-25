from servicios import (
    agregar_producto,
    mostrar_inventario,
    buscar_producto,
    actualizar_producto,
    eliminar_producto,
    calcular_estadisticas
)
from archivos import guardar_csv, cargar_csv

inventario = []

print("#" * 60)
print("Bienvenido al sistema avanzado de inventario\n")
print("#" * 60)

opcion = ""
while opcion != "9":
    print("=== Menú ===")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Calcular estadísticas")
    print("7. Guardar inventario en CSV")
    print("8. Cargar inventario desde CSV")
    print("9. Salir")

    opcion = input("Elija una opción (1-9): ")

    try:
        if opcion == "1":
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            agregar_producto(inventario, nombre, precio, cantidad)

        elif opcion == "2":
            mostrar_inventario(inventario)

        elif opcion == "3":
            nombre = input("Nombre del producto a buscar: ")
            producto = buscar_producto(inventario, nombre)
            if producto:
                print(f"Encontrado: {producto}\n")
            else:
                print("Producto no encontrado.\n")

        elif opcion == "4":
            nombre = input("Nombre del producto a actualizar: ")
            nuevo_precio = input("Nuevo precio (Enter para omitir): ")
            nueva_cantidad = input("Nueva cantidad (Enter para omitir): ")
            actualizar_producto(
                inventario,
                nombre,
                float(nuevo_precio) if nuevo_precio else None,
                int(nueva_cantidad) if nueva_cantidad else None
            )

        elif opcion == "5":
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(inventario, nombre)

        elif opcion == "6":
            calcular_estadisticas(inventario)

        elif opcion == "7":
            ruta = input("Ruta del archivo CSV: ")
            guardar_csv(inventario, ruta)

        elif opcion == "8":
            ruta = input("Ruta del archivo CSV: ")
            nuevo_inventario = cargar_csv(ruta)
            if nuevo_inventario:
                decision = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()
                if decision == "S":
                    inventario = nuevo_inventario
                    print(" Inventario sobrescrito.\n")
                else:
                    inventario.extend(nuevo_inventario)
                    print(" Inventario fusionado.\n")

        elif opcion == "9":
            print("Saliendo del sistema...")

        else:
            print(" Opción inválida.\n")

    except ValueError:
        print("Entrada inválida, intente de nuevo.\n")