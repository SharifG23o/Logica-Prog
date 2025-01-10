"""
Programa que cuenta el número de vocales empleadas en una frase
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Enero de 2025
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""


from apoyo import ingresar_texto, verificar_es_vocal, mostrar_mensaje


def main():

    frase = ingresar_texto("Ingrese la frase o respuesta del encuestado: ")
    cantidad_vocales = obtener_cantidad_vocales(frase)
    mensaje_vocales = generar_mensaje_vocales(frase, cantidad_vocales)
    mostrar_mensaje(mensaje_vocales)


def obtener_cantidad_vocales(frase):

    cantidad_vocales = 0

    for i in range(0,len(frase)):

        if verificar_es_vocal(frase[i]):
            cantidad_vocales = cantidad_vocales+1
    return cantidad_vocales



def generar_mensaje_vocales(frase, cantidad_vocales):

    mensaje = f"La frase \"{frase}\" tiene {cantidad_vocales} vocales"
    return mensaje


main()
