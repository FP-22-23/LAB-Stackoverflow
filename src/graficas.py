from matplotlib import pyplot as plt


## 5.b) Función auxiliar
def dibujar_grafica_tartas(etiquetas, frecuencias ):
    '''Dadas una lista con etiquetas y una lista de números enteros que 
    representa la frecuencia con la que aparecen esas etiquetas, dibuja
    una gráfica de tartas con un sector por cada una de las etiquetas

    :param etiquetas: Lista de etiquetas con cada uno de los elementos a representar
    :type etiquetas: [str]
    :param frecuencias: Lista de enteros con las frecuencias de los elementos a representar
    :type frecuencias: [int]
    
    Se usarán las siguientes instrucciones para generar la gráfica:
        plt.pie(frecuencias, labels=etiquetas, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.legend()
        plt.show()

    donde la lista 'frecuencias' debe estar alineada con la lista de etiquetas.  
    '''
    plt.pie(frecuencias, labels=etiquetas, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.legend()
    plt.show()



def dibuja_grafica_lineas(nombre_serie, etiquetas_x, valores_y, rotacion=80):
    '''Dadas una lista de cadenas `nombre_serie` con los nombres de las series que se van a representar en la gráfica;
    una lista de cadenas `etiquetas_x` con las etiquetas que se van a poner en el eje X,
    una lista de listas de enteros con los valores a dibujar en el eje y para cada una de las series,
    y el ángulo de rotación de las etiquetas del eje X, dibuja una gráfica
    de líneas con esas tres series. Por ejemplo, si nombre_serie = ['list', 'file', 'string']
    y etiquetas_x= [2008,2009],  valores_y = [[50, 30, 20], [10,5,6]]
    Se representará una gráfica que en el eje X tendrá las etiquetas
    2008 y 2009, en la que se dibujarán 3 series (una para list, otra
    para file y otra para string). La lista de listas valores_y 
    indica que en el año 2008 la palabra 'list' apareció 50 veces, 
    'file' 30 veces y 'string' 20 veces. Y en el año 2009, 'list' apareció 10 veces; 'file', 5; y 'string', 6. 

    @param nombre_serie: Lista de cadenas con el nombre de cada una de las
    series a dibujar en la gráfica
    @type nombre_serie: [str]
    @param etiquetas_x: Lista de cadenas con las etiquetas que se van
    a representar en el eje X.
    @type etiquetas_x: [str]
    @param valores_y: Lista de listas de enteros con los valores
    a representar en el eje y la lista tendrá tantas listas
    como etiquetas haya en el eje X, y cada una de esas listas
    tendrá tantos elementos como series se vayan a representar.
    @type valores_y: [[int]]]
    @param rotation: rotación de las etiquetas del eje X, defaults to 80
    @type rotation: int, optional
    '''
    for serie, valores_serie in zip(nombre_serie, valores_y):
        plt.plot(valores_serie, label=serie)
    plt.xticks(range(len(etiquetas_x)), etiquetas_x, rotation=rotacion, fontsize=10)
    plt.legend()
    plt.show()
