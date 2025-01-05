"""
Programa que genera un listado de asistencia
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Enero de 2025
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

from apoyo import ingresar_entero_mayor_que, mostrar_mensaje

VALOR_INICIAL = 0


def main():
    valor_inicial = ingresar_entero_mayor_que(
        "Ingrese el valor inicial: ", VALOR_INICIAL)
    valor_final = ingresar_entero_mayor_que(
        "Ingrese el valor final: ", valor_inicial)
    listado = generar_listado(valor_inicial, valor_final)
    mostrar_mensaje(listado)


def generar_listado(valor_inicial, valor_final):
    listado = " "
    for i in range(valor_inicial, valor_final+1):
        listado += f"{i:2d}.__________________ \n"
    return listado


main()
