import os
import random

# Conjunto de caracteres con los que se forma el nombre
# (solo caracteres especiales que Windows permite en nombres de archivo)
CONJUNTO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "123456789" + "!@#$%&-_+="
LONGITUD = 8

# Carpeta NombresAleatorios dentro del propio proyecto
CARPETA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "NombresAleatorios")


def generar_nombre():
    nombre = ""
    for i in range(LONGITUD):
        nombre += random.choice(CONJUNTO)
    return nombre


def crear_archivo():
    if not os.path.exists(CARPETA):
        os.mkdir(CARPETA)

    # Se repite hasta encontrar un nombre que no exista
    creado = False
    while not creado:
        nombre = generar_nombre() + ".img"
        ruta = os.path.join(CARPETA, nombre)
        if not os.path.exists(ruta):
            archivo = open(ruta, "w")
            archivo.close()
            creado = True

    return ruta


if __name__ == "__main__":
    ruta = crear_archivo()
    print(f"Archivo creado: {ruta}")