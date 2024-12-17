"""
Programa que muestra un mensaje personalizado
Autor: Julian Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia GNU GPL v3
Rec
ursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""


def main():
    nombre = ingresar_texto("Ingrese el nombre del cliente: ")
    mensaje = generar_mensaje_bienvenida(nombre)
    mostrar_mensaje(mensaje)


def ingresar_texto(mensaje):
    texto = input(mensaje)
    return texto


def generar_mensaje_bienvenida(nombre):
    mensaje = f"Bienvenid@ {nombre} a la tienda"
    return mensaje


def mostrar_mensaje(mensaje):
    print(mensaje)


main()
