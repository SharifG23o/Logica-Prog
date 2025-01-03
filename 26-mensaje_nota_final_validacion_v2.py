"""
Programa que muestra un mensaje según una nota final 
(Validación de entrada y validación de la información de la nota en un rango)
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Enero de 2025
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

from apoyo import ingresar_real_rango, mostrar_mensaje


NOTA_MINIMA_GANAR = 3.0
NOTA_MINIMA = 0.0
NOTA_MAXIMA = 5.0


def main():
    nota_final = ingresar_real_rango(
        "Ingrese la nota final: ", NOTA_MINIMA, NOTA_MAXIMA)
    mensaje_nota = generar_mensaje_nota_final(nota_final)
    mostrar_mensaje(mensaje_nota)


def generar_mensaje_nota_final(nota_final):

    mensaje=f"Con la nota {nota_final:.2f} usted: "
    if nota_final >= NOTA_MINIMA_GANAR:
        mensaje += "APROBÓ el curso"
    else:
        mensaje += "REPROBÓ el curso"
    return mensaje


main()
