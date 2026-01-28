import os

def renombrar_imagenes(ruta_carpeta, nombre_base):
    if not os.path.exists(ruta_carpeta):
        print(f"Error: La carpeta '{ruta_carpeta}' no existe.")
        return

    archivos = os.listdir(ruta_carpeta)
    archivos.sort()
    
    contador = 1

    print(f"Iniciando renombrado en: {ruta_carpeta}...\n")

    for archivo in archivos:

        ruta_actual = os.path.join(ruta_carpeta, archivo)

        if os.path.isfile(ruta_actual):
            
            extension = os.path.splitext(archivo)[1]
"
            nuevo_nombre_archivo = f"{nombre_base}_{contador:03d}{extension}"
            
            ruta_nueva = os.path.join(ruta_carpeta, nuevo_nombre_archivo)

            try:
                os.rename(ruta_actual, ruta_nueva)
                print(f"Renombrado: {archivo} -> {nuevo_nombre_archivo}")
                contador += 1
            except Exception as e:
                print(f"No se pudo renombrar {archivo}. Error: {e}")

    print("\n--- ¡Proceso terminado con éxito! ---")

# --- CONFIGURACIÓN ---
# Nota: Usa r"" antes de la ruta para evitar errores con las barras en Windows
ruta = r"C:\Users\Pepe"  # <-- Cambia esta ruta a la carpeta deseada
nombre = "PEPE"          # <-- Cambia este nombre base según prefieras

renombrar_imagenes(ruta, nombre)