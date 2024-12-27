"""
Programa que determina la mayor edad entre cuatro posibles
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

from apoyo import ingresar_entero, mostrar_mensaje


def main():
    edad1 = ingresar_entero("Ingrese la edad 1:")
    edad2 = ingresar_entero("Ingrese la edad 2: ")
    edad3 = ingresar_entero("Ingrese la edad 3: ")
    edad4 = ingresar_entero("Ingrese la edad 4: ")
    mayor_edad = obtener_mayor_edad(edad1, edad2, edad3, edad4)
    mensaje_mayor_edad = generar_mensaje_mayor_edad(mayor_edad)
    mostrar_mensaje(mensaje_mayor_edad)


def obtener_mayor_edad(edad1, edad2, edad3, edad4):

    if edad1 > edad2 and edad1 > edad3 and edad1 > edad4:
        mayor = edad1

    else:
        if edad2 > edad3 and edad2 > edad3:
            mayor = edad2

        else:
            if edad3 > edad4:
                mayor = edad3
            else:
                mayor = edad4
    return mayor


def generar_mensaje_mayor_edad(mayor_edad):
    mensaje = f"La mayor edad es {mayor_edad}"
    return mensaje


main()
