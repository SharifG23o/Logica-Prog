"""
Programa que genera las tablas de multiplicar en un rango
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Enero de 2025
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

from apoyo import ingresar_entero_rango, generar_mensaje_tabla_multiplicar, mostrar_mensaje

MINIMO_VALOR_TABLA = 0
MAXIMO_VALOR_TABLA = 10
MINIMA_TABLA = 0
MAXIMA_TABLA = 20


def main():

    limite_inferior = ingresar_entero_rango(
        "Ingrese el límite inferior: ", MINIMA_TABLA, MAXIMA_TABLA)
    limite_superior = ingresar_entero_rango(
        "Ingrese el límite superior: ", limite_inferior, MAXIMA_TABLA)
    mensaje_tablas = generar_tablas_multiplicar(
        limite_inferior, limite_superior, MINIMO_VALOR_TABLA, MAXIMO_VALOR_TABLA)
    mostrar_mensaje(mensaje_tablas)


def generar_tablas_multiplicar(limite_inferior, limite_superior, valor_minimo, valor_maximo):
    mensaje_tablas = f"TABLAS DE MULTIPLICACIÓN ENTRE {limite_inferior} y {limite_superior} \n"
    i = limite_inferior
    while i <= limite_superior:
        mensaje_tabla = f"\n TABLA DE MULTIPLICAR DEL {i} \n \n"
        j = valor_minimo
        while j <= valor_maximo:

            producto = i * j
            mensaje_tabla += f"{i:2d} x {j:2d} = {producto:3d} \n"
            j += 1

        mensaje_tablas += mensaje_tabla
        i += 1

    return mensaje_tablas


main()
