"""
Programa que determina el curso de acción de un policía
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Enero de 2025
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

from apoyo import ingresar_real, mostrar_mensaje

LIMITE1 = 0.0
LIMITE2 = 0.75  # 45 minutos / 60
LIMITE3 = 1.50
LIMITE4 = 2.00
TIEMPO_INDETERMINADO = -1


def main():
    velocidad_infractor = ingresar_real(
        "Ingrese la velocidad del infractor en km/h: ")
    tiempo_infraccion = ingresar_real(
        "Ingrese el tiempo de la infracción en horas: ")
    velocidad_policia = ingresar_real(
        "Ingrese la velocidad del policía en km/h: ")
    tiempo_intercepcion = calcular_tiempo_intercepcion(
        velocidad_infractor, velocidad_policia, tiempo_infraccion)
    mensaje_policia = generar_mensaje_intercepcion(tiempo_intercepcion)
    mostrar_mensaje(mensaje_policia)


def calcular_tiempo_intercepcion(velocidad_infractor, velocidad_policia, tiempo_infraccion):
    diferencia_velocidades = velocidad_policia-velocidad_infractor
    if diferencia_velocidades != 0.0:
        tiempo_intercepcion = (velocidad_infractor *
                               tiempo_infraccion)/(diferencia_velocidades)
    else:
        tiempo_intercepcion = TIEMPO_INDETERMINADO
    return tiempo_intercepcion


def generar_mensaje_intercepcion(tiempo_intercepcion):
    if tiempo_intercepcion < LIMITE1:
        mensaje = "No hay forma de alcanzar al infractor"
    else:
        mensaje = f"El tiempo necesario de intercepción es de {
            tiempo_intercepcion:.1f} horas, por tanto debes "
        if tiempo_intercepcion <= LIMITE2:
            mensaje += "SALIR EN PERSECUCIÓN"
        elif tiempo_intercepcion <= LIMITE3:
            mensaje += "LLAMAR AL SIGUIENTE PUESTO DE CONTROL Y SALIR EN PERSECUCIÓN"
        elif tiempo_intercepcion <= LIMITE4:
            mensaje += "ÚNICAMENTE LLAMAR AL SIGUIENTE PUESTO DE CONTROL"
        else:
            mensaje += "IGNORAR EL CASO"
    return mensaje


main()
