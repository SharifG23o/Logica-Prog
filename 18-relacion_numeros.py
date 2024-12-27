"""
Programa que determina la relación entre dos números enteros a y b
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

from apoyo import ingresar_entero, mostrar_mensaje


def main():

    a = ingresar_entero("Ingrese el valor de a: ")
    b = ingresar_entero("Ingrese el valor de b: ")
    mensaje_relacion = generar_mensaje_relacion(a, b)
    mostrar_mensaje(mensaje_relacion)


def generar_mensaje_relacion(a, b):

    if a > b:
        mensaje = "El número a es MAYOR que el número b"
    else:
        if b > a:
            mensaje = "El número b es MAYOR que a"
        else:
            mensaje = "El número a es IGUAL al número b"
    return mensaje


main()
