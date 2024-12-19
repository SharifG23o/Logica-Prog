"""
Programa que calcula el promedio de ventas de chocolates de las últimas 5 semanas 
Autor: Julian Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

from apoyo import ingresar_entero,mostrar_mensaje


def main():
    venta_semana1 = ingresar_entero("Ingrese las ventas de la semana 1: ")
    venta_semana2 = ingresar_entero("Ingrese las ventas de la semana 2: ")
    venta_semana3 = ingresar_entero("Ingrese las ventas de la semana 3: ")
    venta_semana4 = ingresar_entero("Ingrese las ventas de la semana 4: ")
    venta_semana5 = ingresar_entero("Ingrese las ventas de la semana 5: ")
    promedio_ventas = calcular_promedio(
        venta_semana1, venta_semana2, venta_semana3, venta_semana4, venta_semana5)
    mensaje = generar_mensaje_ventas(promedio_ventas)
    mostrar_mensaje(mensaje)


def calcular_promedio(valor1, valor2, valor3, valor4, valor5):
    promedio = (valor1+valor2+valor3+valor4+valor5)/5
    return promedio


def generar_mensaje_ventas(promedio_ventas):
    mensaje = f"El promedio de ventas es {promedio_ventas}"
    return mensaje


main()
