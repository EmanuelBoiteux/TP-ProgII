import sys

def readArchivo(nombre: str):
    rutaArchivo = f"Entradas/{nombre}.txt"
    fLectura = open(rutaArchivo, 'r')
    palabrasList = listaPalabras(fLectura)
    diccionarioPalabras = getPalabras(fLectura, palabrasList)
    completaFrase(nombre, diccionarioPalabras, mayorFrecuencia(palabrasList))
    fLectura.close()
    
def mayorFrecuencia(palabrasList: list) -> str:
    for palabra in palabrasList:
        if palabra == '-':
            palabrasList.remove(palabra)
    masFrecuente = max(palabrasList, key=palabrasList.count)
    return masFrecuente


def listaPalabras(archivo) -> list:
    palabras = []
    for linea in archivo:
        linea = linea.split(' ')
        largo = len(linea)
        for i in range(0, largo):
            if i == largo - 1:
                linea[i] = linea[i][:-1] # elimino los \n de las palabras que los tengan
                palabras.append(linea[i])
                palabras.append('-') # coloco un guion para saber que en esa posicion se encontraria un salto de linea
            else:
                palabras.append(linea[i])
    return palabras


### TESTEAR ###
# n = 1: palabra anterior
# n = -1: palabra posterior
def palabrasAntePos(palabra: str, listaPalabras: list, n: int) -> dict:
    if n != 1 and n != -1:
        print("ERROR funcion: palabrasAntePos")

    antePos = {}
    largo = len(listaPalabras)
    i = 0
    while i < largo:
        if i != 0 and i != largo - 1:
            if listaPalabras[i] == palabra and listaPalabras[i - n] != '-':
                if listaPalabras[i - n] not in antePos:
                    antePos[listaPalabras[i - n]] = 1
                else:
                    antePos[listaPalabras[i - n]] += 1
        elif i == 0 and listaPalabras[0] == palabra and n == -1 and listaPalabras[1] != '-': # primera palabra de la lista igual a la palabra, y busco la palabra posterior
                if listaPalabras[i - n] not in antePos:
                    antePos[listaPalabras[i - n]] = 1
                else:
                    antePos[listaPalabras[i - n]] += 1
        elif i == largo - 1 and listaPalabras[largo - 1] == palabra and n == 1 and listaPalabras[largo - 2] != '-': # ultima palabra de la lista igual a la palabra, y busco la palabra anterior
                if listaPalabras[i - n] not in antePos:
                    antePos[listaPalabras[i - n]] = 1
                else:
                    antePos[listaPalabras[i - n]] += 1
        i += 1

    return antePos


"""
recibe un archivo y una lista y crea un diccionario donde cada palabra de la lista recibida
es una clave del diccionario y los valores son dos diccionarios, el primero almacena otro diccionario
con las palabras que preceden a la palabra, y el segundo es otro diccionario con las palabras que le
suceden a la palabra
"""
def getPalabras(archivo, lista: list) -> dict:
    archivo.seek(0) # Vuelve al principio del archivo
    texto = archivo.readlines()
    dictPalabras = {}
    for linea in texto:
        linea = linea[:-1]
        palabras = linea.split(' ')
        for palabra in palabras:
            if palabra not in dictPalabras:
                dictPalabras[palabra] = {"anteriores": palabrasAntePos(palabra, lista, 1), "siguientes": palabrasAntePos(palabra, lista, -1)}
    """
    with open("SalidasDict/salidaDict.txt", 'w') as archivo_salida:
        json.dump(dictPalabras, archivo_salida, indent=1)
    """

    return dictPalabras

"""
completaFrase recibe el nombre de una persona, un diccionario de palabras y una palabra. Lee linea a linea el texto con las
frases correspondientes a la persona pasada como argumento y cuando encuentra un guion almacena la palabra anterior y posterior al mismo,
si las hubiere, caso contrario guarda un string vacio segun corresponda.
"""
def completaFrase(nombre: str, diccionarioPalabras: dict, palabraRepetida: str):
    rutaArchivo = f"Frases/{nombre}.txt"
    frasesArchivo = open(rutaArchivo, 'r')

    cantLineas = len(frasesArchivo.readlines())
    i = 1
    frasesArchivo.seek(0)

    while i <= cantLineas:
        linea = frasesArchivo.readline()
        if linea[-1] != '_': # evitamos quitar el guion cuando tenemos _EOF, en cualquier otro caso, quitamos el \n del final de la linea
            linea = linea[:-1]
        linea = linea.split(' ')
        largo = len(linea)
        posGuion = linea.index('_')
        if posGuion == 0 and largo == 1:
            palabraAnterior = ''
            palabraSiguiente = ''
        elif posGuion == 0:
            palabraAnterior = ''
            palabraSiguiente = linea[posGuion + 1]
        elif posGuion == largo - 1:
            palabraAnterior = linea[posGuion - 1]
            palabraSiguiente = ''
        else:
            palabraAnterior = linea[posGuion - 1]
            palabraSiguiente = linea[posGuion + 1]

        remplazaGuion(palabraAnterior, palabraSiguiente, diccionarioPalabras, linea, nombre, palabraRepetida)
        i += 1
    #remplazaGuion('me', 'en', diccionarioPalabras, frasesArchivo, nombre)

    frasesArchivo.close()

def remplazaGuion(anterior: str, siguiente: str, palabrasDict: dict, linea: str, persona: str, masFrecuente: str):
    salida = open(f"Salidas/{persona}.txt", "a")
    if anterior != '' and anterior in palabrasDict and palabrasDict[anterior]["siguientes"] != {}:
        palabra = masRepetida(palabrasDict[anterior]["siguientes"])
        linea[linea.index('_')] = palabra
        linea = ' '.join(linea) + '\n'
    elif siguiente != '' and siguiente in palabrasDict and palabrasDict[siguiente]["anteriores"] != {}:
        palabra = masRepetida(palabrasDict[siguiente]["anteriores"])
        linea[linea.index('_')] = palabra
        linea = ' '.join(linea) + '\n'
    else:
        linea[linea.index('_')] = masFrecuente # si las palabras anteriores y siguientes no estan en la lista agrego la mas frecuente del texto pasado
        linea = ' '.join(linea) + '\n'

    salida.write(linea)

def masRepetida(dictPalabras: dict) -> str:
    maxFrecuencia = 0
    maxPalabra = ''
    
    for palabra, frecuencia in dictPalabras.items():
        if frecuencia > maxFrecuencia:
            maxFrecuencia = frecuencia
            maxPalabra = palabra

    return maxPalabra


def main():
    if len(sys.argv) != 2:
        print("Numero de argumentos incorrecto")
    else:
        readArchivo(sys.argv[1])

if __name__ == "__main__":
    main()