"""
Programa que muestra un mensaje 
Autor: Julian Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

MENSAJE = "Bienvenidos a Python, programa de Ingeniería de Sistemas y Computación"


def main():  # Bloque principal

    # Componentes del bloque principal

    mostrar_mensaje(MENSAJE)  # MENSAJE es un argumento

# Función de mostrar mensaje definida


def mostrar_mensaje(mensaje):  # Aquí mensaje es recibido como parámetro
    """
    Función para mostrar un mensaje en pantalla
    Parámetros:
    -Mensaje a mostrar
    """
    print(mensaje)  # El parámetro es impreso


main()
