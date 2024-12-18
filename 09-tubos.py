"""
Programa que determina la cantidad de metros de tubo que se venden
Autor: Julian Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

from apoyo import ingresar_entero, ingresar_real, mostrar_mensaje


def main():
    cantidad_tubos = ingresar_entero("Ingrese la cantidad de tubos: ")
    longitud_tubo = ingresar_real("Ingrese la longitud de un tubo: ")
    metros_totales = calcular_metros_totales(cantidad_tubos, longitud_tubo)
    mensaje = generar_mensaje_tubos(metros_totales)
    mostrar_mensaje(mensaje)


def calcular_metros_totales(cantidad_tubos, longitud_tubo):
    metros_totales = cantidad_tubos*longitud_tubo
    return metros_totales


def generar_mensaje_tubos(metros_totales):
    mensaje = f"La longitud total de los tubos vendidos es {metros_totales:.1f} metros"
    return mensaje


main()
