"""
Programa que 
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Enero de 2025
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

from apoyo import ingresar_texto, mostrar_mensaje


def main():

    mensaje=ingresar_texto("Ingrese un mensaje: ")
    codigos_ascii_mensaje=obtener_codigos_ascii(mensaje)
    mensaje_ascii=generar_mensaje_ascii(mensaje, codigos_ascii_mensaje)
    mostrar_mensaje(mensaje_ascii)


def obtener_codigos_ascii(mensaje):
    codigos_ascii_mensaje=" "
    for letra in mensaje:
        codigos_ascii_mensaje+=f"{ord(letra)}"
    return codigos_ascii_mensaje

def generar_mensaje_ascii(mensaje, codigos_ascii_mensaje):
    mensaje_ascii=f"El mensaje \"{mensaje}\" usa los códigos ASCII: {codigos_ascii_mensaje} \t"
    return mensaje_ascii

    

main()