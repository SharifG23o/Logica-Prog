"""
Programa que muestra una oración en minúsculas y capitalizada
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Enero de 2025
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

from apoyo import ingresar_texto, mostrar_mensaje


def main():
    oracion = ingresar_texto("Ingrese la oración: ")
    oracion_minuscula = convertir_minusculas(oracion)
    oracion_capitalizada = convertir_capitalizada(oracion)
    mensaje = generar_mensaje_oracion( oracion, oracion_minuscula, oracion_capitalizada)
    mostrar_mensaje(mensaje)


def convertir_minusculas(oracion):
    oracion_minusculas = ""
    i = 0
    while i < len(oracion):
        oracion_minusculas += oracion[i].lower()
        i += 1
    return oracion_minusculas


def convertir_capitalizada(oracion):
    oracion_capitalizada = " "
    for i in range(0, len(oracion)):
        if i == 0 or oracion[i-1] == " ":
            oracion_capitalizada += oracion[i].upper()
        else:
            oracion_capitalizada += oracion[i].lower()
    return oracion_capitalizada


def generar_mensaje_oracion(oracion, oracion_minuscula, oracion_capitalizada):
    mensaje = (f"Su oración original es \"{oracion}\" \n"
               f"La oración en minúsculas es \"{oracion_minuscula}\" \n"
               f"La oración capitalizada es \"{oracion_capitalizada}\"")
    return mensaje


main()
