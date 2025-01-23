"""
Programa que cuenta cuántos términos de la sucesión de Fibonacci hay
entre dos valores 
Autor: Julián Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Enero de 2025
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""


from apoyo import ingresar_entero_mayor_que,mostrar_mensaje

MIN_VALOR=0

def main():
    limite_inferior=ingresar_entero_mayor_que("Ingrese el límite inferior: ", MIN_VALOR)
    limite_superior=ingresar_entero_mayor_que("Ingrese el límite superior: ", limite_inferior)
    cantidad_fibonacci= contar_terminos_fibonacci(limite_inferior, limite_superior)
    mensaje_fibonacci= generar_mensaje_fibonacci(limite_inferior,limite_superior,cantidad_fibonacci)
    mostrar_mensaje(mensaje_fibonacci)

def contar_terminos_fibonacci(limite_inferior,limite_superior):
    cantidad_terminos = 0
    a=1
    b=1
    while a <= limite_superior:
        if a >= limite_inferior:
            cantidad_terminos = cantidad_terminos+1
        c = a+b
        a = b
        b = c
    return cantidad_terminos


def generar_mensaje_fibonacci(limite_inferior,limite_superior,cantidad_fibonacci):
    mensaje = f"Entre {limite_inferior} y {limite_superior} hay {cantidad_fibonacci} términos de la sucesión de Fibonacci"
    return mensaje




    
main()