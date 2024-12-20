"""
Programa para calcular el salario de un empleado
Estudiante: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

from apoyo import ingresar_entero, mostrar_mensaje

MAX_SALARIO = 2500000


def main():

    horas_trabajadas = ingresar_entero(
        "Ingrese la cantidad de horas trabajadas: ")
    valor_hora = ingresar_entero("Ingrese el valor de la hora: ")
    salario = calcular_salario_empleado(horas_trabajadas, valor_hora)
    salario_final = determinar_salario_final(salario)
    mensaje = generar_mensaje_salario(salario_final)
    mostrar_mensaje(mensaje)


def calcular_salario_empleado(horas_trabajadas, valor_hora):
    salario = horas_trabajadas*valor_hora
    return salario


def determinar_salario_final(salario):

    if salario > MAX_SALARIO:
        salario_final = MAX_SALARIO
    else:
        salario_final = salario

    return salario_final


def generar_mensaje_salario(salario_final):
    mensaje = f"Su salario final es de $ {salario_final}"
    return mensaje


main()
