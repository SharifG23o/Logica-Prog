"""
Programa que determina si un aspirante al ejército es 
apto o no para entrar
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Enero de 2025
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

from apoyo import ingresar_entero, ingresar_real, ingresar_texto, mostrar_mensaje


def main():

    genero = ingresar_texto("Ingrese el género: ")
    estado_civil = ingresar_texto("Ingrese el estado civil: ")
    estatura = ingresar_real("Ingrese su estatura: ")
    edad = ingresar_entero("Ingrese la edad: ")
    ingresa_aspirante = verificar_ingresa_aspirante(
        genero, estado_civil, estatura, edad)
    mensaje_incorporacion = generar_mensaje_incorporacion(ingresa_aspirante)
    mostrar_mensaje(mensaje_incorporacion)


def verificar_ingresa_aspirante(genero, estado_civil, estatura, edad):
    ingresa_mujer = verificar_ingresa_mujer(
        genero, estado_civil, estatura, edad)
    ingresa_hombre = verificar_ingresa_hombre(
        genero, estado_civil, estatura, edad)
    ingresa_aspirante = ingresa_mujer or ingresa_hombre
    return ingresa_aspirante


def verificar_ingresa_mujer(genero, estado_civil, estatura, edad):

    ingresa_mujer =\
        genero == "mujer" and \
        estado_civil == "soltera" and \
        estatura > 1.60 and \
        edad >= 20 and edad <= 25
    return ingresa_mujer


def verificar_ingresa_hombre(genero, estado_civil, estatura, edad):
    ingresa_hombre = genero == "hombre" and estado_civil == "soltero" and estatura > 1.65 and edad >= 18 and edad <= 24
    return ingresa_hombre


def generar_mensaje_incorporacion(ingresa_aspirante):
    if ingresa_aspirante:
        mensaje = "El aspirante es APTO para ser incorporado"

    else:
        mensaje = "El aspirante NO ES APTO para ser incorporado"
    return mensaje


main()
