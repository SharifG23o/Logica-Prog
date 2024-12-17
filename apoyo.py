"""
Módulo de apoyo con funciones  
Autor: Julian Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

# MOSTRAR MENSAJE


def mostrar_mensaje(mensaje):  # Aquí mensaje es recibido como parámetro
    """
    Función para mostrar un mensaje en pantalla
    Parámetros:
    -Mensaje a mostrar
    """
    print(mensaje)  # El parámetro es impreso


# INGRESAR TEXTO

def ingresar_texto(mensaje):
    texto = input(mensaje)
    return texto

# INGRESAR ENTERO


def ingresar_entero(mensaje):
    entero = int(input(mensaje))
    return entero
