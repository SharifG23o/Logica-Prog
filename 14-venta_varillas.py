"""
Programa que determina la cantidad de vehículos necesarios 
para llevar un pedido
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

from apoyo import ingresar_entero, mostrar_mensaje

MAXIMO_VEHICULOS = 10
MAXIMA_CAPACIDAD_VEHICULO = 100


def main():
    cantidad_varillas_vendidas = ingresar_entero(
        "Ingrese la cantidad de varillas vendidas: ")
    cantidad_vehiculos = calcular_cantidad_vehiculo(cantidad_varillas_vendidas)
    mensaje = generar_mensaje_venta(cantidad_vehiculos)
    mostrar_mensaje(mensaje)


def calcular_cantidad_vehiculo(cantidad_varillas):
    cantidad_vehiculos = cantidad_varillas//MAXIMA_CAPACIDAD_VEHICULO
    return cantidad_vehiculos


def generar_mensaje_venta(cantidad_vehiculos):

    if cantidad_vehiculos <= MAXIMO_VEHICULOS:
        mensaje = f"La cantidad de vehículos es: {cantidad_vehiculos}"

    else:
        mensaje = "Se cancela el pedido"

    return mensaje


main()
