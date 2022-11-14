# -*- coding: utf-8 -*-

from stackoverflow import *
import time
################################################################
#  Funciones de test
################################################################

def test_filtrar_por_anyo(preguntas, anyo):
    pregs = filtrar_por_anyo(preguntas, anyo)
    print(f"   - Número de preguntas en '{anyo}': {len(pregs)}")
    print(f"   - Las tres primeras son:")
    mostrar_iterable_enumerado(pregs[:3])


def test_obtener_etiquetas(preguntas):

    etiquetas = obtener_etiquetas(preguntas)
    print('   - Número de etiquetas: {}'.format(len(etiquetas)))
    print("   - Diez primeras: {}\n".format(sorted(etiquetas)[:10]))


def test_obtener_preguntas_mejor_valoradas(preguntas, n=5):
    preguntas_mejor_valoradas = obtener_preguntas_mejor_valoradas(preguntas, n)
    for p in preguntas_mejor_valoradas:
        print("   [{}] - {}".format(p[1], p[0]))
    print()
    

def test_frecuencia_etiquetas(preguntas):
    frecuencias = frecuencia_etiquetas(preguntas)
    etiquetas = sorted(frecuencias, key=frecuencias.get, reverse=True)
    for etiqueta in etiquetas[:5]:
        print("   {} -> {}".format(etiqueta, frecuencias[etiqueta]))
    print()
    

def test_mostrar_distribucion_etiquetas(preguntas, etiquetas):
    
    mostrar_distribucion_etiquetas(preguntas, etiquetas)
    
    
def test_obtener_palabras_clave(titulo, stopwords):
    print("   - Dejando stopwords: {}".format(obtener_palabras_clave(titulo)))
    print("   - Quitando stopwords: {}\n".format(obtener_palabras_clave(titulo, stopwords)))


def test_frecuencia_palabras_clave(preguntas, stopwords):
    print("   (solo las 5000 primeras preguntas para que la prueba sea más rápida)")
    frecuencias = frecuencia_palabras_clave(preguntas[:5000], stopwords)
    print('   - Número de palabras: {}'.format(len(frecuencias)))
    print("   - Diez primeras: {}\n".format(frecuencias[:10]))

    
def test_agrupar_preguntas_por_anyo(preguntas):  
    preguntas_por_anyo = agrupar_preguntas_por_anyo(preguntas)
    for anyo in preguntas_por_anyo:
        print("   {} -> {} preguntas".format(anyo, len(preguntas_por_anyo[anyo])))
    print()


def test_mostrar_evolucion_etiquetas(preguntas, etiquetas):
    inicio = time.time()
    mostrar_evolucion_etiquetas(preguntas, etiquetas)
    fin = time.time()
    print(f"Tiempo ejecución {fin-inicio}")

def test_mostrar_evolucion_etiquetas2(preguntas, etiquetas):
    inicio = time.time()
    mostrar_evolucion_etiquetas2(preguntas, etiquetas)
    fin = time.time()
    print(f"Tiempo ejecución {fin-inicio}")
    
def test_leer_preguntas(preguntas):
    print(f"Se han leido {len(preguntas)} preguntas")
    print("Las diez primeras son:")
    mostrar_iterable_enumerado(preguntas[:10])

def mostrar_iterable_enumerado(iterable):
    for ind, elem in enumerate(iterable, 1):
        print(f"\t\t{ind}-{elem}")

################################################################
#  Programa principal
################################################################
def main():
    with open('data/stopwords.txt') as f:
        stopwords = [p.strip() for p in f]

    preguntas = leer_preguntas('data/stackoverflow_python_questions.csv')
    test_leer_preguntas(preguntas)

    print("TEST de 'filtrar_por_anyo'")
    test_filtrar_por_anyo(preguntas,2009)
    test_filtrar_por_anyo(preguntas,2015)
    
    print("TEST de 'obtener_etiquetas'")
    test_obtener_etiquetas(preguntas)
    
    print("TEST de 'obtener_preguntas_mejor_valoradas'")
    test_obtener_preguntas_mejor_valoradas(preguntas)

    print("TEST de 'frecuencia_etiquetas'")
    test_frecuencia_etiquetas(preguntas)
    print("TEST de 'mostrar_distribucion_etiquetas'\n")
    etiquetas = ['list', 'file', 'string']
    test_mostrar_distribucion_etiquetas(preguntas, etiquetas)

    print("TEST de 'obtener_palabras_clave'")
    titulo = 'How do I make a menu that does not require the user to press [enter] to make a selection ?'
    test_obtener_palabras_clave(titulo, stopwords)
    
    print("TEST de 'frecuencia_palabras_clave'")
    test_frecuencia_palabras_clave(preguntas, stopwords)

    print("TEST de 'agrupar_preguntas_por_anyo'")
    test_agrupar_preguntas_por_anyo(preguntas)

    print("TEST de 'mostrar_evolucion_etiquetas'\n")
    etiquetas = ['list', 'file', 'string']
    test_mostrar_evolucion_etiquetas(preguntas, etiquetas)
    
    print("TEST de 'mostrar_evolucion_etiquetas2'\n")
    test_mostrar_evolucion_etiquetas2(preguntas, etiquetas)

if __name__== "__main__":
    main()


