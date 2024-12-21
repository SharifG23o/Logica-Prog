"""
Programa que calcula el área de un triángulo
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

from apoyo import ingresar_real, mostrar_mensaje


def main():
    base = ingresar_real("Ingresar la base del triángulo: ")
    altura = ingresar_real("Ingrese la altura del triángulo: ")
    area_triangulo = calcular_area_triangulo(base, altura)
    mensaje = generar_mensaje_area_triangulo(area_triangulo)
    mostrar_mensaje(mensaje)


def calcular_area_triangulo(base, altura):
    area_triangulo = (base*altura)/2
    return area_triangulo


def generar_mensaje_area_triangulo(area):

    if area >= 0:
        mensaje = f"El área es {area}"

    else:
        mensaje = "No se muestra un área negativa"

    return mensaje


main()
