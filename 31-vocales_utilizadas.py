"""
Programa que determina las vocales utilizadas en una frase
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Enero de 2025
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""


from apoyo import ingresar_texto, verificar_es_vocal, mostrar_mensaje


def main():

    frase = ingresar_texto("Ingrese la frase: ")
    vocales_empleadas = obtener_vocales_empleadas(frase)
    mensaje_vocales_empleadas = generar_mensaje_vocales_empleadas(
        frase, vocales_empleadas)
    mostrar_mensaje(mensaje_vocales_empleadas)


def obtener_vocales_empleadas(frase):

    vocales_empleadas = " "

    for letra in frase:
        if verificar_es_vocal(letra) and letra not in vocales_empleadas:
            vocales_empleadas = vocales_empleadas + letra
    return vocales_empleadas


def generar_mensaje_vocales_empleadas(frase, vocales_empleadas):

    mensaje = f"En la frase \"{ frase}\" se utilizan las vocales \"{vocales_empleadas}\""
    return mensaje


main()
