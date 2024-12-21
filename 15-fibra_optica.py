"""
Programa que calcula la cantidad de rollos de fibra óptica y
los metros faltantes para un siguiente rollo
para llevar un pedido
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

from apoyo import ingresar_entero, mostrar_mensaje

MAX_METRO_ROLLO = 50


def main():
    metros_vendidos = ingresar_entero("Ingrese los metros vendidos: ")
    cantidad_rollos = calcular_cantidad_rollos(metros_vendidos)
    cantidad_adicional_fibra = calcular_cantidad_adicional_fibra(
        metros_vendidos)
    mensaje = generar_mensaje_venta_fibra(
        cantidad_rollos, cantidad_adicional_fibra)
    mostrar_mensaje(mensaje)


def calcular_cantidad_rollos(metros_vendidos):
    cantidad_rollos = metros_vendidos//MAX_METRO_ROLLO
    return cantidad_rollos


def calcular_cantidad_adicional_fibra(metros_vendidos):
    cantidad_adicional_fibra = MAX_METRO_ROLLO-metros_vendidos % MAX_METRO_ROLLO
    return cantidad_adicional_fibra


def generar_mensaje_venta_fibra(cantidad_rollos, cantidad_adicional_fibra):
    if cantidad_adicional_fibra != MAX_METRO_ROLLO:
        mensaje = f"La cantidad de rollos es {cantidad_rollos} y necesita {
            cantidad_adicional_fibra} metro(s) para completar otro rollo"

    else:
        mensaje = f"La cantidad de rollos es {cantidad_rollos}"

    return mensaje


main()
