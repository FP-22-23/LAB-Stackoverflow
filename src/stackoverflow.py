# -*- coding: utf-8 -*-
''' Análisis de preguntas sobre Python en stackoverflow

AUTOR: José A. Troyano
REVISOR: Toñi Reina
ÚLTIMA MODIFICACIÓN: 14/11/2022

En este proyecto trabajaremos con preguntas sobre el lenguaje Python. Los datos están
extraídos de stackoverflow, y se corresponden con una colección de preguntas desde 2008 hasta
2016 relacionadas con Python. La colección completa está disponible en Kaggle datasets
(https://www.kaggle.com/stackoverflow/pythonquestions). Los datos con los que trabajaremos incluyen
distintas informaciones sobre las preguntas y, a partir de ellos, generaremos una serie de 
informes y gráficas que resumirán aspectos relevantes de las temáticas más consultadas.


FORMATO DE ENTRADA:
-------------------
El formato de entrada es CSV. Cada registro del fichero de entrada ocupa una línea y contiene
cuatro informaciones sobre las preguntas (puntuación, título, anyo y  etiqueta principal). 
Estas son las primeras líneas de un fichero de entrada:

    score,title,year,tag
    21,How can I find the full path to a font from its display name on a Mac?,2008,photoshop
    27,Get a preview JPEG of a PDF on Windows?,2008,pdf
    40,Continuous Integration System for a Python Codebase,2008,extreme-programming
    25,cx_Oracle: How do I iterate over a result set?,2008,cx-oracle
    28,Using 'in' to match an attribute of Python objects in an array,2008,iteration
    30,Class views in Django,2008,oop
    20,Python and MySQL,2008,bpgsql


FUNCIONES A IMPLEMENTAR:
------------------------
- leer_preguntas(fichero):
    lee el fichero de preguntas y devuelve una lista de tuplas con nombre
- filtrar_por_anyo(preguntas, anyo):
    recibe una lista de preguntas y devuelve solo las del anyo recibido como parámetro
- calcular_etiquetas(preguntas):
    calcula el conjunto de etiquetas usadas en la colección de preguntas
- obtener_preguntas_mejor_valoradas_preguntas_mejor_valoradas(preguntas, n=10):
    calcula las preguntas con las puntuaciones más altas
- frecuencia_etiquetas(preguntas):
    calcula las frecuencias de las etiquetas de una lista de preguntas
- mostrar_distribucion_etiquetas(preguntas, etiquetas):
    muestra un diagrama de tarta con la distribución de uso de varias etiquetas
- obtener_palabras_clave(titulo, stopwords=[]):
    calcula la lista de palabras clave del título de una pregunta
- frecuencia_palabras_clave(preguntas, stopwords=[]):
    calcula las frecuencias de las palabras clave usadas en una lista de preguntas
- agrupar_preguntas_por_anyo(preguntas):
    calcula un diccionario con una lista de preguntas por cada anyo
- mostrar_evolucion_etiquetas(preguntas, etiquetas):
    muestra la evolución del uso de etiquetas a lo largo del tiempo
'''

import csv
from collections import namedtuple, Counter
from itertools import groupby
import graficas

# EJERCICIO 1:
Pregunta = namedtuple('Pregunta', 'puntuacion, titulo, anyo, etiqueta')
def leer_preguntas(fichero):
    '''     Dado el nombre (y ruta) de un fichero, lee el fichero de preguntas y devuelve una lista de tuplas de tipo 'Pregunta' con los datos leidos del fichero.    
    
    @param fichero: nombre del fichero de entrada 
    @type fichero: str 
    @return: lista de preguntas Pregunta(puntuacion, titulo, anyo, etiqueta)
    @rtype: [Pregunta(int, str, int, str)]
    '''
    with open(fichero, 'r', encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        preguntas = [Pregunta(int(puntuacion), titulo, int(anyo), etiqueta) 
                     for puntuacion, titulo, anyo, etiqueta in lector]
    return preguntas


# EJERCICIO 2:
def filtrar_por_anyo(preguntas, anyo):
    '''Dadas una lista una lista de preguntas y un anyo, devuelve una lista de las preguntas del anyo recibido como parámetro.
    
    @param preguntas: lista de preguntas Pregunta(puntuacion, titulo, anyo, etiqueta)
    @type preguntas:[Pregunta(int, str, int, str)]
    @param anyo: Año del que se seleccionarán las preguntas 
    @type anyo:int
    @return:lista de preguntas seleccionadas 
    @rtype: [Pregunta(int, str, int, str)]
    '''
    return [p for p in preguntas if p.anyo==anyo]


# EJERCICIO 3:
def obtener_etiquetas(preguntas):
    ''' Dada una lista de preguntas, devuelve el conjunto de etiquetas usadas en esas preguntas
    
    @param preguntas: lista de preguntas Pregunta(puntuacion, titulo, anyo, etiqueta)
    @type preguntas:[Pregunta(int, str, int, str)]
    @return: conjunto de etiquetas encontradas 
    @rtype: {str}
    '''
    return set(p.etiqueta for p in preguntas)


# EJERCICIO 4:
def obtener_preguntas_mejor_valoradas(preguntas, n=10):
    ''' dadas una lista de preguntas y un número n, devuelve una lista de tuplas (titulo, puntuacion) con el título y la puntuación de las n preguntas con las puntuaciones más altas. Si no se proporciona n, tomará como valor por defecto 10.
    
    @param preguntas: lista de preguntas Pregunta(puntuacion, titulo, anyo, etiqueta)
    @type preguntas:[Pregunta(int, str, int, str)]
    @param n: número de preguntas a recuperar 
    @type n: int
    @return:  lista de tuplas (titulo, puntuacion) ordenadas de mayor a menor puntuacion
    @rtype: [(str, int)]
    '''
    resultado = [(p.titulo, p.puntuacion) for p in preguntas]
    resultado.sort(key=lambda x:x[1], reverse=True)
    if len(resultado)> n:
        resultado = resultado[:n]
    return resultado


def obtener_preguntas_mejor_valoradas2(preguntas, n=10):
    resultado = sorted (((p.titulo, p.puntuacion) for p in preguntas), \
                           key=lambda x:x[1], reverse=True)
    if len(resultado)> n:
        resultado = resultado[:n]
    return resultado

# EJERCICIO 5:

## 5.a) Función auxiliar
def frecuencia_etiquetas(preguntas):
    ''' Dada una lista de preguntas, devuelve un diccionario en el que las claves son las 
    etiquetas de las preguntas, y los valores el número de veces (frecuencia) que aparece 
    esa etiqueta en las preguntas.
    
    @param preguntas: lista de preguntas Pregunta(puntuacion, titulo, anyo, etiqueta)
    @type preguntas:[Pregunta(int, str, int, str)]
    @return: diccionario cuyas claves son las etiquetas y los valores las frecuecias
    @rtype: {str: int}
    '''
    frecuencias = Counter(p.etiqueta for p in preguntas)
    return dict(frecuencias)

def frecuencia_etiquetas2(preguntas):
    res = dict()
    for p in preguntas:
        clave = p.etiqueta
        if clave in res:
            res[clave]+= 1
        else:
            res[clave]=1
    return res

def mostrar_distribucion_etiquetas(preguntas, etiquetas):
    ''' Muestra un diagrama de tarta con la distribución de uso de varias etiquetas.
       El diagrama de tarta tendrá un sector por cada etiqueta recibida.
    
    @param preguntas: lista de preguntas Pregunta(puntuacion, titulo, anyo, etiqueta)
    @type preguntas:[Pregunta(int, str, int, str)]
    @param etiquetas: lista de etiquetas que se inlcuirán en la gráfica
    @type etiquetas: [str]    
    '''
    frecuencias = frecuencia_etiquetas(preguntas)
    frec_etiquetas = [frecuencias.get(e,0) for e in etiquetas]
    graficas.dibujar_grafica_tartas(etiquetas, frec_etiquetas)




# EJERCICIO 6:
def obtener_palabras_clave(titulo, stopwords=[]):
    ''' Dadas una cadena de caracteres que representa un título, y una lista
    de palabras huecas (_stopwords_), devuelve ula lista con las palabras claves del título.
    

    @param titulo: cadena en la que se buscan las palabras clave
    @type titulo: str
    @param stopwords: palabras huecas, consideradas no relevantes como palabras clave
    @type stopwords: [str]    
    @return:  lista de palabras clave encontradas en el título
    @rtype: [str]
    Cuestiones a tener en cuenta:
       - Debes trabajar con el título en minúsculas
       - Debes descomponer el título en una lista de términos separados por espacios
       - Debes eliminar los siguientes símbolos de los términos: '¿?[](){}¡!-+/*,;.<>='
       - Debes dejar en la lista de términos solo aquellos que estén compuestos por letras
       - Debes eliminar de la lista los términos que aparezcan el la lista de stopwords
    '''
    simbolos = '¿?-+/*[](){},;.<>='
    titulo = titulo.lower()
    terminos = [t.strip().strip(simbolos) for t in titulo.split(' ')]
    terminos = [t for t in terminos if t.isalpha() and t not in stopwords]
    return terminos

def frecuencia_palabras_clave(preguntas, stopwords=[]):
    ''' Dadas una lista de preguntas y una lista con palabras huecas, devuelve una lista de tuplas (palabra_clave, frecuencia) ordenada de mayor a menor frecuencia. Las palabras clave son aquéllas que aportan significado, es decir, que no son palabras huecas  
    @param preguntas: lista de preguntas Pregunta(puntuacion, titulo, anyo, etiqueta)
    @type preguntas:[Pregunta(int, str, int, str)]
    @param stopwords: palabras huecas, consideradas no relevantes como palabras clave
    @type stopwords: [str]
    @return: lista de tuplas (palabra_clave, frecuencia) ordenada de mayor a menor frecuencia
    @rtype: [(str, int)]
    '''
    palabras = sum((obtener_palabras_clave(p.titulo, stopwords) for p in preguntas),[])
    frecuencias = Counter(palabras)
    return sorted(frecuencias.items(),key=lambda x:x[1], reverse=True)


# EJERCICIO 7:
def agrupar_preguntas_por_anyo(preguntas):
    ''' Devuelve un diccionario cuyas claves son los años, 
    y cuyos valores son listas de preguntas que se hicieron ese año.
    
    @param preguntas: lista de preguntas Pregunta(puntuacion, titulo, anyo, etiqueta)
    @type preguntas:[Pregunta(int, str, int, str)]

    SALIDA: 
       - diccionario cuyas claves son los anyos y los valores la lista de preguntas de cada anyo  
                               -> {int: [Pregunta(int, str, int, str)]}
    '''
    preguntas_por_anyo = dict()
    for p in preguntas:
        preguntas_por_anyo.setdefault(p.anyo, []).append(p)
    return preguntas_por_anyo
    '''
    #Solución alternativa sin usar setdefault
    preguntas_por_anyo = dict()
    for p in preguntas:
        if p.anyo not in preguntas_por_anyo.keys():
            preguntas_por_anyo[p.anyo] = [p]
        else:
            preguntas_por_anyo[p.anyo].append(p)
    return preguntas_por_anyo
    '''
    '''
    # Solución alternativa usando groupby de itertools
    preguntas_ordenadas = sorted(preguntas, key=lambda x:x.anyo)
    grupos = groupby(preguntas_ordenadas, key=lambda x:x.anyo)
    preguntas_por_anyo = {clave: [v for v in valores] for clave, valores in grupos}
    return dict(preguntas_por_anyo)
    '''

# EJERCICIO 10: 
def mostrar_evolucion_etiquetas(preguntas, etiquetas):
    ''' Muestra la evolución del uso de etiquetas a lo largo del tiempo
    
    @param preguntas: lista de preguntas Pregunta(puntuacion, titulo, anyo, etiqueta)
    @type preguntas:[Pregunta(int, str, int, str)]
       - etiquetas: lista de etiquetas que se inlcuirán en la gráfica
    SALIDA EN PANTALLA: 
       - gráfica con una línea para cada etiqueta con su evolución temporal
    
    Se usarán las siguientes instrucciones para generar la gráfica:
        for etiqueta, evolucion in zip(etiquetas, evoluciones):
            plt.plot(evolucion, label=etiqueta)
        plt.xticks(range(len(anyos)), anyos, rotation=80, fontsize=10)
        plt.legend()
        plt.show()

    Donde 'anyos' y 'evoluciones' son dos listas con la siguiente información:
       - anyos: lista de los anyos incluidos en la colección de preguntas, ordenados de menor a mayor
       - evoluciones: lista con la evolución de uso de cada etiqueta, alineada con la lista de etiquetas. 
                      Cada evolución consiste en una lista de frecuencias, alineada con la lista de anyos, 
                      correspondientes con el número de veces que la etiqueta ha sido usada cada anyo.   
    '''
   
    preguntas_por_anyo = agrupar_preguntas_por_anyo(preguntas)
    anyos = sorted(preguntas_por_anyo)
    evoluciones = []
    for etiqueta in etiquetas:
        evolucion = []
        for _, lista_preguntas in preguntas_por_anyo.items():
            frecuencia = len([p for p in lista_preguntas if p.etiqueta==etiqueta])
            evolucion.append(frecuencia)
        evoluciones.append(evolucion)
    
    graficas.dibuja_grafica_lineas(etiquetas, anyos, evoluciones)


def mostrar_evolucion_etiquetas2(preguntas, etiquetas):

   
    preguntas_por_anyo = agrupar_preguntas_por_anyo(preguntas)
    anyos = sorted(preguntas_por_anyo)
    num_preguntas_por_anyo_y_etiqueta = {anyo:contar_por_etiqueta(lista_preguntas, etiquetas)\
                                          for anyo, lista_preguntas in preguntas_por_anyo.items()}
    evoluciones = []
    for etiqueta in etiquetas:
        evolucion = [dicc.get(etiqueta,0) for año,dicc in num_preguntas_por_anyo_y_etiqueta.items()]
        evoluciones.append(evolucion)

    graficas.dibuja_grafica_lineas(etiquetas,  anyos, evoluciones)

def contar_por_etiqueta (lista_preguntas, etiquetas):
    return Counter(p.etiqueta for p in lista_preguntas if p.etiqueta in etiquetas)
    
    
def contar_por_etiqueta2 (lista_preguntas, etiquetas):
    res = dict()
    for p in lista_preguntas:
        if p.etiqueta in etiquetas:
            if p.etiqueta in res:
                res[p.etiqueta]+=1
            else:
                res[p.etiqueta]=1
    return res

    
    
def agrupar_por_etiqueta (lista_preguntas, etiquetas):
    res = dict()
    for p in lista_preguntas:
        if p.etiqueta in etiquetas:
            if p.etiqueta in res:
                res[p.etiqueta].append(p)
            else:
                res[p.etiqueta]=[p]
    return res