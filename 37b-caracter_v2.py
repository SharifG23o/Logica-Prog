"""
Programa que realiza un dibujo dependiendo de un valor n
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Enero de 2025
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""


from apoyo import ingresar_entero_mayor_que, mostrar_mensaje

MINIMO_VALOR = 0

def main():
 
    n=ingresar_entero_mayor_que("Ingrese el valor de n: ",MINIMO_VALOR)
    dibujo=generar_dibujo(n)
    mostrar_mensaje(dibujo)


def generar_dibujo(n):
    dibujo = ""
    for j in range (0,n):
        dibujo+= repetir_caracter("*",n-j)
        dibujo+=repetir_caracter(".", 2*j)
        dibujo+=repetir_caracter("*", n-j)
        dibujo+="\n"

    dibujo+= repetir_caracter("*", 2*n)

    return dibujo

def repetir_caracter(caracter, cantidad):
    mensaje= caracter*cantidad
    return mensaje



main()