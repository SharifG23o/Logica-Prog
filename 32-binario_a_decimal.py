"""
Programa que convierte un número de binario (8 bits) a decimal 
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Enero de 2025
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""


from apoyo import ingresar_texto_longitud, mostrar_mensaje


LONGITUD_BINARIO = 8


def main():

    numero_binario = ingresar_texto_longitud(
        "Ingrese un número binario de 8 bits: ", LONGITUD_BINARIO)
    numero_decimal = convertir_binario_decimal(numero_binario)
    mensaje_decimal = generar_mensaje_conversion(
        numero_binario, numero_decimal)
    mostrar_mensaje(mensaje_decimal)


def convertir_binario_decimal(numero_binario):

    valor = 0
    potencia = 0
    i = len(numero_binario)-1

    while i >= 0:
        valor = valor + int(numero_binario[i]) * 2 ** potencia
        potencia = potencia + 1
        i = i-1

    return valor


def generar_mensaje_conversion(numero_binario, numero_decimal):

    mensaje = f"El número binario {
        numero_binario} equivale al valor de {numero_decimal}"

    return mensaje


main()
