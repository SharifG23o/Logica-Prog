"""
Programa que muestra un mensaje según una nota final
(Validación de entrada)
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Enero de 2025
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

from apoyo import ingresar_real, mostrar_mensaje


NOTA_MINIMA_GANAR = 3.0


def main():
    nota_final = ingresar_real("Ingrese la nota final: ")
    mensaje_nota = generar_mensaje_nota_final(nota_final)
    mostrar_mensaje(mensaje_nota)


def generar_mensaje_nota_final(nota_final):
    if nota_final >= NOTA_MINIMA_GANAR:
        mensaje = "APROBÓ el curso"
    else:
        mensaje = "REPROBÓ el curso"
    return mensaje


main()
