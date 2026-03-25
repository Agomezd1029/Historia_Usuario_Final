import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    """Guarda el inventario en un archivo CSV."""
    if not inventario:
        print(" Inventario vacío, no se puede guardar.\n")
        return
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            if incluir_header:
                escritor.writerow(["nombre", "precio", "cantidad"])
            for producto in inventario:
                escritor.writerow([producto["nombre"], producto["precio"], producto["cantidad"]])
        print(f" Inventario guardado en: {ruta}\n")
    except Exception as error:
        print(f"Error al guardar CSV: {error}\n")


def cargar_csv(ruta):
    """Carga el inventario desde un archivo CSV."""
    inventario = []
    errores = 0
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            encabezado = next(lector)
            if encabezado != ["nombre", "precio", "cantidad"]:
                print(" Encabezado inválido en CSV.\n")
                return []
            for fila in lector:
                if len(fila) != 3:
                    errores += 1
                    continue
                try:
                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])
                    if precio < 0 or cantidad < 0:
                        errores += 1
                        continue
                    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
                except ValueError:
                    errores += 1
                    continue
        if errores > 0:
            print(f"⚠ {errores} filas inválidas omitidas.\n")
        print(f" Inventario cargado desde: {ruta}\n")
        return inventario
    except FileNotFoundError:
        print(" Archivo no encontrado.\n")
    except Exception as error:
        print(f" Error al cargar CSV: {error}\n")
    return []