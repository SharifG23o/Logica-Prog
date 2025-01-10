"""
Programa que genera una tabla de multiplicar
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Enero de 2025
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""


from apoyo import ingresar_entero_rango,generar_mensaje_tabla_multiplicar,mostrar_mensaje


MINIMO_VALOR_TABLA = 0
MAXIMO_VALOR_TABLA = 10

MINIMA_TABLA = 0
MAXIMA_TABLA = 20


def main():
    numero_tabla = ingresar_entero_rango(
        "Ingrese la tabla a generar: ", MINIMA_TABLA, MAXIMA_TABLA)
    mensaje_tabla = generar_mensaje_tabla_multiplicar(
        numero_tabla, MINIMO_VALOR_TABLA, MAXIMO_VALOR_TABLA)
    mostrar_mensaje(mensaje_tabla)





main()
