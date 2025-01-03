"""
Programa que determina el porcentaje de aumento del salario de 
un empleado dependiendo de sus años de experiencia
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Enero de 2025
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

from apoyo import ingresar_entero, mostrar_mensaje


def main():
    salario_actual = ingresar_entero("Ingresar salario actual: ")
    experiencia = ingresar_entero("Ingrese la experiencia en años: ")
    porcentaje_aumento = determinar_porcentaje_aumento(experiencia)
    salario_final = calcular_salario_final(salario_actual, porcentaje_aumento)
    mensaje_salario = generar_mensaje_salario(
        experiencia, porcentaje_aumento, salario_final)
    mostrar_mensaje(mensaje_salario)


def determinar_porcentaje_aumento(tiempo):
    if tiempo >= 2 and tiempo <= 5 or tiempo >= 8 and tiempo <= 12:
        porcentaje_aumento = 0.10
    elif tiempo >= 21 and tiempo <= 25:
        porcentaje_aumento = 0.15
    else:
        porcentaje_aumento = 0.0
    return porcentaje_aumento


def calcular_salario_final(salario, aumento):
    salario_final = salario+salario*aumento
    return salario_final


def generar_mensaje_salario(experiencia, porcentaje_aumento, salario_final):
    mensaje = (f"Con {experiencia} años de experiencia, obtiene un aumento de"
               f"{porcentaje_aumento*100:.1f}% y su salario final es de {salario_final}"


               )

    return mensaje


main()