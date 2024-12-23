"""
Programa que calcula el salario neto de un empleado
considerando los descuentos por salud y pensión
para llevar un pedido
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

from apoyo import ingresar_entero, mostrar_mensaje

PORCENTAJE_DESCUENTO_SALUD = 0.04
PORCENTAJE_DESCUENTO_PENSION = 0.05
SUBSIDIO_TRANSPORTE = 250000
SALARIO_INICIAL_SUBSIDIO = 1000000
SALARIO_FINAL_SUBSIDIO = 2000000


def main():

    salario = ingresar_entero("Ingrese el salario base del empleado: ")
    descuento_salario = calcular_descuento(
        salario, PORCENTAJE_DESCUENTO_SALUD+PORCENTAJE_DESCUENTO_PENSION)
    salario_neto = calcular_salario_neto(salario, descuento_salario)
    mensaje = generar_mensaje_salario(salario_neto, descuento_salario)
    mostrar_mensaje(mensaje)


def calcular_descuento(salario, descuento):
    descuento = salario*descuento
    return descuento


def calcular_salario_neto(salario, descuento_salario):
    salario_neto = salario-descuento_salario
    return salario_neto


def generar_mensaje_salario(salario_neto, descuento_salario):

    mensaje = (f"El descuento aplicado es {descuento_salario} "
               f"y el salario neto a pagar es {salario_neto}")

    if salario_neto >= SALARIO_INICIAL_SUBSIDIO and salario_neto <= SALARIO_FINAL_SUBSIDIO:
        mensaje += f"Más un subsidio de transporte por {SUBSIDIO_TRANSPORTE}"
    return mensaje


main()
