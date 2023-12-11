"""
Documentacion para las funciones en main.py
"""

def listaPalabras(archivo) -> list:
    """
    listaPalabras recibe un archivo de texto y devuelve una lista con las palabras del archivo. Por cada salto de linea agrega un '-'
    a la lista indicando que en esa posicion termina una linea.
    """
    pass

def getPalabras(archivo, lista: list) -> dict:
    """
    Esta funcion recibe un archivo y una lista y crea un diccionario donde cada palabra de la lista recibida
    es una clave del diccionario y los valores son dos diccionarios, el primero almacena otro diccionario
    con las palabras que preceden a la palabra, y el segundo es otro diccionario con las palabras que le
    suceden a la palabra
    """
    pass

def palabrasAntePos(palabra: str, listaPalabras: list, n: int) -> dict:
    """
    Esta funcion recibe una palabra, una lista de palabras y un entero n, y devuelve un diccionacio de acuerdo a:
    - si n = 1 devuelve un diccionario cuyas claves son las palabras de la lista que se encuentran en una posicion i - 1 respecto a las ocurrencias en la lista
    de la palabra pasada, siendo i su indice.
    - si n = -1 devuelve un diccionario cuyas claves son las palabras de la lista que se encuentran en una posicion i + 1 respecto a las ocurrencias en la lista
    de la palabra pasada, siendo i su indice.
    En cualquier caso, los valores del diccionario son las ocurrencias de cada palabra. Si la palabra pasada no tiene palabras anteriores o posteriores se devuelve {}.
    """
    pass

def mayorFrecuencia(palabrasList: list) -> str:
    """
    mayorFrecuencia recibe un a lista de palabras que contiene guiones, elimina estos guiones y devuelve la palabra que mas veces aparecio en la lista.
    """
    pass

def completaFrase(nombre: str, diccionarioPalabras: dict, palabraRepetida: str):
    """
    completaFrase recibe el nombre de una persona, un diccionario de palabras y una palabra. Lee linea a linea el texto con las
    frases correspondientes a la persona pasada como argumento y cuando encuentra un guion almacena la palabra anterior y posterior al mismo,
    si las hubiere, caso contrario guarda un string vacio segun corresponda.
    """
    pass

def remplazaGuion(anterior: str, siguiente: str, palabrasDict: dict, linea: str, masFrecuente: str, archivoSalida):
    """
    Esta funcion recibe una palabra anterior y una palabra siguiente a un guion, un diccionario de palabras, la linea donde se encuentra el guion,
    la palabra mas frecuente del archivo de texto y ese archivo. Se encarga de remplazar en el archivo pasado como argumento
    las posiciones de los guiones por palabras de acuerdo al siguiente criterio: 
    - si la palabra anterior al guion se encuentra en el diccionario pasado y en el texto hay palabras que le siguen, entonces se coloca en la posicion del la palabra
    que mas veces siguio despues de esta palabra
    - si la palabra siguiente al guion se encuentra en el diccionario pasado y en el texto hay palabras que le anteceden, entonces se coloca en la posicion del guion la palabras
    que mas veces precedio a la palabra
    - en caso de que ni la palabra anterior ni la siguiente al guion esten en el diccionario, se coloca la palabra mas frecuente pasada como argumento
    """
    pass

def masRepetida(dictPalabras: dict) -> str:
    """
    Esta funcion recibe un diccionario cuyas claves son palabras y los valores de cada palabra son enteros que corresponden a su ocurrencia.
    masRepedida devuelve la palabra del diccionario con mayor ocurrencia.
    """
    pass