import sys
import json

def readArchivo(nombre):
    rutaArchivo = f"Entradas/{nombre}.txt"
    fLectura = open(rutaArchivo, 'r')
    listaPrueba = listaPalabras(fLectura)
    getPalabras(fLectura, listaPrueba)
    fLectura.close()
    

### TESTEAR ###
def listaPalabras(archivo):
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
def palabrasAntePos(palabra, listaPalabras, n):
    if n != 1 and n != -1:
        print("ERROR funcion: palabrasAntePos")

    antePos = []
    largo = len(listaPalabras)
    i = 0
    while i < largo:
        if i != 0 and i != largo - 1:
            if listaPalabras[i] == palabra and listaPalabras[i - n] != '-':
                antePos.append(listaPalabras[i - n])
        elif i == 0 and listaPalabras[0] == palabra and n == -1 and listaPalabras[1] != '-': # primera palabra de la lista igual a la palabra, y busco la palabra posterior
                antePos.append(listaPalabras[i - n])
        elif i == largo - 1 and listaPalabras[largo - 1] == palabra and n == 1 and listaPalabras[largo - 2] != '-': # ultima palabra de la lista igual a la palabra, y busco la palabra anterior
                antePos.append(listaPalabras[i - n])
        i += 1
    return antePos


### TESTEAR ###
def getPalabras(archivo, lista):
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

def completaFrase(nombre):
    rutaArchivo = f"Frases/{nombre}.txt"
    frasesArchivo = open(rutaArchivo, 'r')

    i = 0
    linea = frasesArchivo.readline()
    while linea != '':
        linea = linea[:-1]
        linea = linea.split(' ')
        largo = len(linea)
        posGuion = linea.index('_')
        print(linea)
        if posGuion == 0:
            print('posicion 0')
            palabraAnterior = []
            palabraSiguiente = linea[posGuion + 1]
        elif posGuion == largo - 1:
            print('posicion final')
            palabraAnterior = linea[posGuion - 1]
            palabraSiguiente = []
        else:
            print('tercera opcion')
            palabraAnterior = linea[posGuion - 1]
            palabraSiguiente = linea[posGuion + 1]

        print(palabraAnterior)
        print(palabraSiguiente)

        linea = frasesArchivo.readline()
        i += 1



    frasesArchivo.close()


def main():
    if len(sys.argv) != 2:
        print("Numero de argumentos incorrecto")
    else:
        #readArchivo(sys.argv[1])
        completaFrase(sys.argv[1])

if __name__ == "__main__":
    main()


""" esto iba en completa frase
    lista_diccionarios = []

    for linea in lineasArchivo:
        linea = linea.split(' ')
        for i in range(len(linea)):
            if(linea[i] == '_'):
                if(linea[i-1]):
                    palabra_anterior = linea[i-1]
                else:
                    palabra_anterior = null

                if(linea[i+1]):
                    palabra_siguiente = linea[i+1]
                else:
                    palabra_siguiente = null

                diccionario = {
                    palabra_anterior: palabra_anterior,
                    palabra_siguiente: palabra_siguiente,
                    posibles_valores: [(de,2), (para,5)]
                }
                lista_diccionarios.append(diccionario)
    """
