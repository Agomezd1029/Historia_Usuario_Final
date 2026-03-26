# 📦 Sistema Avanzado de Inventario

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Estado](https://img.shields.io/badge/Estado-Completo-brightgreen)
![Licencia](https://img.shields.io/badge/Licencia-Uso%20Académico-lightgrey)

Sistema de gestión de inventario desarrollado en Python, basado en consola, que permite administrar productos mediante operaciones CRUD y almacenamiento en archivos CSV.

---

## 📑 Tabla de Contenidos

- [📖 Descripción](#-descripción)
- [✨ Características](#-características)
- [🗂️ Estructura del Proyecto](#️-estructura-del-proyecto)
- [⚙️ Requisitos](#️-requisitos)
- [🚀 Ejecución](#-ejecución)
- [💾 Formato de Datos](#-formato-de-datos)
- [🛡️ Validaciones](#️-validaciones)
- [🧠 Arquitectura](#-arquitectura)
- [👨‍💻 Autor](#-autor)

---

## 📖 Descripción

Este proyecto implementa un sistema de inventario modular que permite gestionar productos mediante un menú interactivo en consola. Está diseñado con una estructura organizada para facilitar su mantenimiento y escalabilidad.

---

## ✨ Características

- Gestión completa de inventario (CRUD)
- Búsqueda de productos por nombre
- Actualización de precio y cantidad
- Eliminación de productos
- Cálculo de estadísticas
- Guardado y carga de archivos CSV
- Validación de datos
- Control de cambios no guardados

---

## 🗂️ Estructura del Proyecto

```bash
📁 proyecto_inventario/
│
├── main.py        # Interfaz y menú principal
├── servicios.py   # Lógica del inventario
├── archivos.py    # Manejo de archivos CSV
└── README.md      # Documentación
⚙️ Requisitos
Python 3.x
No se requieren librerías externas
🚀 Ejecución

Ejecuta el programa desde la terminal:

python main.py
💾 Formato de Datos

El archivo CSV debe tener la siguiente estructura:

nombre,precio,cantidad
Laptop,2500,3
Mouse,50,10
🛡️ Validaciones
Se valida el encabezado del CSV
Se ignoran filas con errores
No se permiten valores negativos
Manejo de errores con try/except
Confirmación antes de sobrescribir datos
Advertencia de cambios sin guardar
🧠 Arquitectura

El proyecto está dividido en módulos:

main.py → Controla el flujo del programa
servicios.py → Contiene la lógica del inventario
archivos.py → Gestiona la lectura y escritura en CSV
👨‍💻 Autor
 Angel_gomez 
