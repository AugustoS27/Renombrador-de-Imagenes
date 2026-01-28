# Renombrador de Imágenes (Python)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)

Un script ligero para renombrar automáticamente lotes de imágenes o archivos de forma secuencial y ordenada. Ideal para organizar datasets de Machine Learning, galerías de fotos o archivos desordenados.

## Funcionalidades

- **Renombrado Secuencial:** Convierte nombres aleatorios en un formato limpio: `nombre_001`, `nombre_002`, etc.
- **Seguridad de Extensión:** Detecta y mantiene la extensión original de cada archivo (`.jpg`, `.png`, `.xml`, etc.), evitando corrupciones.
- **Padding con Ceros:** Utiliza formato de 3 dígitos (ej. `001` en lugar de `1`) para garantizar un ordenamiento correcto en cualquier sistema operativo.
- **Validación:** Ignora subcarpetas para evitar errores, procesando solo archivos.

## Requisitos

- Python 3.6 o superior.
- No requiere de librerías externas

## Funcionalidades

- **Renombrado Secuencial:** Convierte nombres aleatorios en un formato limpio: `nombre_001`, `nombre_002`, etc.
- **Seguridad de Extensión:** Detecta y mantiene la extensión original de cada archivo (`.jpg`, `.png`, `.xml`, etc.), evitando corrupciones.
- **Padding con Ceros:** Utiliza formato de 3 dígitos (ej. `001` en lugar de `1`) para garantizar un ordenamiento correcto en cualquier sistema operativo.
- **Validación:** Ignora subcarpetas para evitar errores, procesando solo archivos.
