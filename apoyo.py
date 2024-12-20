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

# INGRESAR REAL


def ingresar_real(mensaje):
    valor = float(input(mensaje))
    return valor


# CALCULAR PROMEDIO

def calcular_promedio(valor1, valor2, valor3, valor4, valor5):
    promedio = (valor1+valor2+valor3+valor4+valor5)/5
    return promedio

# DETERMINAR SALARIO EMPLEADO


def calcular_salario_empleado(horas_trabajadas, valor_hora):
    salario = horas_trabajadas*valor_hora
    return salario
