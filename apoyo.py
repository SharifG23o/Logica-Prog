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
    repetir = True
    while repetir:
        try:
            valor = int(input(mensaje))
            repetir = False
        except:
            print("No es una entrada válida para un número entero")
    return valor

# INGRESAR REAL


def ingresar_real(mensaje):
    repetir = True
    while repetir:
        try:
            valor = float(input(mensaje))
            repetir = False
        except:
            print("No es una entrada válida para un número real")
    return valor


# CALCULAR PROMEDIO

def calcular_promedio(valor1, valor2, valor3, valor4, valor5):
    promedio = (valor1+valor2+valor3+valor4+valor5)/5
    return promedio

# DETERMINAR SALARIO EMPLEADO


def calcular_salario_empleado(horas_trabajadas, valor_hora):
    salario = horas_trabajadas*valor_hora
    return salario


# OBTENER MAYOR

def obtener_mayor(a, b):
    mayor = a
    if b > mayor:
        mayor = b

    return mayor


# INGRESAR REAL RANGO


def ingresar_real_rango(mensaje, valor_minimo, valor_maximo):
    repetir = True
    while repetir:
        valor = ingresar_real(mensaje)
        if valor < valor_minimo or valor > valor_maximo:
            print(f"El valor no está entre {valor_minimo} y {valor_maximo} ")
        else:
            repetir = False
    return valor


# INGRESAR ENTERO RANGO

def ingresar_entero_rango(mensaje, valor_minimo, valor_maximo):
    repetir = True
    while repetir:
        valor = ingresar_entero(mensaje)
        if valor < valor_minimo or valor > valor_maximo:
            print(f"El valor no está entre {valor_minimo} y {valor_maximo} ")
        else:
            repetir = False
    return valor


# INGRESAR ENTERO MAYOR QUE 

def ingresar_entero_mayor_que(mensaje, valor_minimo):
    repetir = True
    while repetir:
        valor = ingresar_entero(mensaje)
        if valor <= valor_minimo:
            print(f"El valor no es mayor que {valor_minimo}")

        else:
            repetir = False
    return valor
