"""
Programa que determina en qué etapa del ciclo de la vida
se encuentra una persona
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""


from apoyo import ingresar_entero, mostrar_mensaje


def main():
    edad = ingresar_entero("Ingrese la edad de la persona: ")
    ciclo_vida = determinar_ciclo_vida(edad)
    mensaje_ciclo_vida = generar_mensaje_ciclo_vida(edad, ciclo_vida)
    mostrar_mensaje(mensaje_ciclo_vida)


def determinar_ciclo_vida(edad):

    if edad <= 5:
        etapa = "PRIMERA INFANCIA"
    elif edad <= 11:
        etapa = "INFANCIA"
    elif edad <= 18:
        etapa = "ADOLESCENCIA"
    elif edad <= 26:
        etapa = "JUVENTUD"
    elif edad <= 59:
        etapa = "ADULTEZ"
    elif edad <= 74:
        etapa = "ADULTO MAYOR"
    else:
        etapa = "ANCIANO"
    return etapa


def generar_mensaje_ciclo_vida(edad, ciclo_vida):
    mensaje = f"Según su edad de {
        edad} años su ciclo de vida es {ciclo_vida}"
    return mensaje


main()
