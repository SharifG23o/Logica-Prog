"""
Programa que convierte un número decimal a binario (8 bits)
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Enero de 2025
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

from apoyo import ingresar_entero_rango, mostrar_mensaje

LONGITUD_BINARIO = 8
VALOR_MINIMO = 0
VALOR_MAXIMO = 255


def main():
    numero_decimal = ingresar_entero_rango("Ingrese un número decimal: ", VALOR_MINIMO, VALOR_MAXIMO)
    numero_binario = convertir_decimal_binario(numero_decimal, LONGITUD_BINARIO)
    mensaje_conversion = generar_mensaje_conversion(numero_decimal, numero_binario)
    mostrar_mensaje(mensaje_conversion)


def convertir_decimal_binario(numero_decimal, longitud):
    
    return bin(numero_decimal)[2:].zfill(longitud)


def generar_mensaje_conversion(numero_decimal, numero_binario):
  
    return f"El número decimal en base 10 {numero_decimal} equivale a {numero_binario} en binario ({LONGITUD_BINARIO} bits)"



main()
