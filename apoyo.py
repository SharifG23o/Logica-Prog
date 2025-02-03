"""
Módulo de apoyo con funciones  
Autor: Julian Esteban Gutiérrez
Estudiante: Sharif Giraldo Obando
Fecha: Diciembre de 2024
Licencia GNU GPL v3
Recursos de información: https://www.youtube.com/@infraestructura-linux-programa
"""

USAR_TK= True

if USAR_TK:
    from tkinter import Tk, messagebox, simpledialog
    tk = Tk()
    tk.geometry("0x0")



# MOSTRAR MENSAJE


def mostrar_mensaje(mensaje):  # Aquí mensaje es recibido como parámetro
    """
    Función para mostrar un mensaje en pantalla
    Parámetros:
    -Mensaje a mostrar
    """
    if USAR_TK:
        messagebox.showinfo("Información", mensaje)

    else:
        print(mensaje)  # El parámetro es impreso


# MOSTRAR ERROR

def mostrar_error(mensaje):  # Aquí mensaje es recibido como parámetro

    if USAR_TK:
        messagebox.showerror("Error", mensaje)

    else:
        print(mensaje)  # El parámetro es impreso



# INGRESAR TEXTO

def ingresar_texto(mensaje):

    
    if USAR_TK:
        texto = simpledialog.askstring("Entrada", mensaje)
    else:

        texto = input(mensaje)
    return texto

# INGRESAR ENTERO


def ingresar_entero(mensaje):



    repetir = True
    while repetir:
        try:
            valor = int(ingresar_texto(mensaje))
            repetir = False
        except:
            mostrar_error("No es una entrada válida para un número entero")
    return valor

# INGRESAR REAL


def ingresar_real(mensaje):
    repetir = True
    while repetir:
        try:
            valor = float(ingresar_texto(mensaje))
            repetir = False
        except:
            mostrar_error("No es una entrada válida para un número real")
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
            mostrar_error(f"El valor no está entre {valor_minimo} y {valor_maximo} ")
        else:
            repetir = False
    return valor


# INGRESAR ENTERO RANGO

def ingresar_entero_rango(mensaje, valor_minimo, valor_maximo):
    repetir = True
    while repetir:
        valor = ingresar_entero(mensaje)
        if valor < valor_minimo or valor > valor_maximo:
            mostrar_error(f"El valor no está entre {valor_minimo} y {valor_maximo} ")
        else:
            repetir = False
    return valor


# INGRESAR ENTERO MAYOR QUE

def ingresar_entero_mayor_que(mensaje, valor_minimo):
    repetir = True
    while repetir:
        valor = ingresar_entero(mensaje)
        if valor <= valor_minimo:
            mostrar_error(f"El valor no es mayor que {valor_minimo}")

        else:
            repetir = False
    return valor


# TABLA DE MULTIPLICAR

def generar_mensaje_tabla_multiplicar(numero_tabla, minimo_valor, maximo_valor):
    mensaje_tabla = f"\n TABLA DE MULTIPLICAR DEL {numero_tabla} \n \n"
    i = minimo_valor
    while i <= maximo_valor:
        producto = numero_tabla*i
        mensaje_tabla += f"{numero_tabla:2d} x {i:2d} = {producto:3d} \n"
        i += 1
    return mensaje_tabla



#VERIFICAR ES VOCAL



def verificar_es_vocal(letra):
    es_vocal = letra.lower() in "aeiou"
    return es_vocal


#VERIFICAR ES VOCAL V2

def verificar_es_vocal2(letra):
    letra= letra.lower()
    es_vocal= letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u"
    return es_vocal



# INGRESAR TEXTO LONGITUD


def ingresar_texto_longitud(mensaje, longitud):

  repetir=True

  while repetir:
     
     texto= ingresar_texto(mensaje)
     if len(texto) != longitud:
        mostrar_error(f"El número no tiene una longitud de {longitud}")

     else:


        repetir= False

  return texto
     
     


