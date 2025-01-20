"""
Programa que cifra y descifra un mensaje
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Enero de 2025
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

from apoyo import ingresar_texto, mostrar_mensaje


CONSTANTE_CIFRADO = 1

def main():

    mensaje=ingresar_texto("Ingrese el mensaje a cifrar: ")
    mensaje_cifrado=cifrar_mensaje(mensaje,CONSTANTE_CIFRADO)
    mensaje_descifrado=descifrar_mensaje(mensaje_cifrado,CONSTANTE_CIFRADO)
    mensaje_cifrado_cesar=generar_mensaje_cifrado_cesar(mensaje, mensaje_cifrado,mensaje_descifrado)
    mostrar_mensaje(mensaje_cifrado_cesar)


def cifrar_mensaje(mensaje, desplazamiento):
    cifrado=""
    for letra in mensaje:
        cifrado+=chr(ord(letra)+desplazamiento)

    return cifrado

def descifrar_mensaje(mensaje, desplazamiento):
    descifrado=""
    for letra in mensaje:
        descifrado+= chr(ord(letra)-desplazamiento)
    return descifrado


def generar_mensaje_cifrado_cesar(mensaje, mensaje_cifrado,mensaje_descifrado):
    mensaje=f"Mensaje original \"{mensaje}\" \n Mensaje cifrado: \"{mensaje_cifrado}\" \n Mensaje descifrado: \"{mensaje_descifrado}\""
    return mensaje

main()