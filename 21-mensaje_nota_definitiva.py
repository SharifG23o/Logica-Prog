"""
Programa que muestra un mensaje según una nota definitiva
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

from apoyo import ingresar_real, mostrar_mensaje


def main():
    nota_definitiva = ingresar_real("Ingrese la nota definitiva: ")
    mensaje_nota_definitiva = generar_mensaje_nota_definitiva(nota_definitiva)
    mostrar_mensaje(mensaje_nota_definitiva)


def generar_mensaje_nota_definitiva(nota):

    if nota < 3.0:
        mensaje = "INSUFICIENTE"
    elif nota <= 3.5:
        mensaje = "ACEPTABLE"
    elif nota <= 4.0:
        mensaje = "SOBRESALIENTE"
    else:
        mensaje = "EXCELENTE"
    return mensaje


main()
