"""
Programa que muestra la TRM 
Autor: Julian Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia GNU GPL v3
Rec
ursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""


def main():
    valor_trm = ingresar_entero("Ingresar el valor del TRM: ")
    mensaje = generar_mensaje_trm(valor_trm)
    mostrar_mensaje(mensaje)


def ingresar_entero(mensaje):
    entero = int(input(mensaje))
    return entero


def generar_mensaje_trm(valor_trm):
    mensaje = f"El valor del TRM es {valor_trm}"
    return mensaje


def mostrar_mensaje(mensaje):
    print(mensaje)


main()
