"""
Programa que imprime el valor de la temperatura
Autor: Julian Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""
from apoyo import mostrar_mensaje


def main():
    temperatura = ingresar_real("Ingrese el valor de la temperatura: ")
    mensaje = generar_mensaje_temperatura(temperatura)
    mostrar_mensaje(mensaje)


def ingresar_real(mensaje):
    valor = float(input(mensaje))
    return valor


def generar_mensaje_temperatura(temperatura):
    mensaje = f"La temperatura es {temperatura:.2f} °C"
    return mensaje


main()
