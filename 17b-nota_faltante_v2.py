"""
Programa que calcula la cuarta nota de un curso
que emplea un promedio aritmético
considerando los descuentos por salud y pensión
para llevar un pedido
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

from apoyo import ingresar_real, ingresar_texto, mostrar_mensaje

NOTA_MINIMA = 0.0
NOTA_MAXIMA = 5.0
NOTA_MINIMA_GANAR = 3.0
NUMERO_NOTAS = 4


def main():

    nombre_curso = ingresar_texto("Ingrese el nombre del curso: ")
    nota1 = ingresar_real("Ingrese la nota 1: ")
    nota2 = ingresar_real("Ingrese la nota 2: ")
    nota3 = ingresar_real("Ingrese la nota 3: ")
    nota4 = calcular_cuarta_nota_promedio_aritmetico(nota1, nota2, nota3)
    mensaje = generar_mensaje_nota(nombre_curso, nota4)
    mostrar_mensaje(mensaje)


def calcular_cuarta_nota_promedio_aritmetico(nota1, nota2, nota3):
    nota4 = NOTA_MINIMA_GANAR*NUMERO_NOTAS-nota1-nota2-nota3
    return nota4


def generar_mensaje_nota(nombre_curso, nota4):

    if nota4 < NOTA_MINIMA:
        mensaje = f"El curso {nombre_curso} ya se APROBÓ"

    elif nota4 > NOTA_MAXIMA:
        mensaje = f"El curso {nombre_curso} ya se REPROBÓ"

    else:

        mensaje = f"Necesita una nota de {nota4} para APROBAR"

    return mensaje


main()
