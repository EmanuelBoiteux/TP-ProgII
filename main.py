import sys
import json


def listaPalabras(archivo) -> list:
    palabras = []
    for linea in archivo:
        linea = linea.split(' ')
        largo = len(linea)
        for i in range(0, largo):
            if i == largo - 1:
                if linea[i] == '\n': # en el caso de tener '.... \n' '\n' quedara como elemento de la lista y debemos eliminarlo
                    linea = linea[:-1]
                else:
                    linea[i] = linea[i][:-1] # elimino los \n de las palabras que los tengan
                    palabras.append(linea[i])
                palabras.append('-') # coloco un guion para saber que en esa posicion se encontraria un salto de linea
            else:
                palabras.append(linea[i])
    return palabras


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
    return dictPalabras


def mayorFrecuencia(palabrasList: list) -> str:
    for palabra in palabrasList:
        if palabra == '-':
            palabrasList.remove(palabra)
    masFrecuente = max(palabrasList, key=palabrasList.count)
    return masFrecuente


def palabrasAntePos(palabra: str, listaPalabras: list, n: int) -> dict:
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


def completaFrase(nombre: str, diccionarioPalabras: dict, palabraRepetida: str):
    frasesArchivo = open(f"Frases/{nombre}.txt", 'r')
    salida = salida = open(f"Salidas/{nombre}.txt", "a")
    cantLineas = len(frasesArchivo.readlines())
    i = 1
    frasesArchivo.seek(0)

    while i <= cantLineas:
        linea = frasesArchivo.readline()
        if linea[-1] == '\n': # evitamos quitar el guion cuando tenemos _EOF, en cualquier otro caso, quitamos el \n del final de la linea
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

        remplazaGuion(palabraAnterior, palabraSiguiente, diccionarioPalabras, linea, palabraRepetida, salida)
        i += 1
    frasesArchivo.close()
    salida.close()


def remplazaGuion(anterior: str, siguiente: str, palabrasDict: dict[dict], linea: str, masFrecuente: str, archivoSalida):
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

    archivoSalida.write(linea)


def masRepetida(dictPalabras: dict[str]) -> str:
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
        rutaArchivo = f"Entradas/{sys.argv[1]}.txt"
        fLectura = open(rutaArchivo, 'r')
        palabrasList = listaPalabras(fLectura)
        diccionarioPalabras = getPalabras(fLectura, palabrasList)
        """
        with open('diccionario.json', 'w') as archivo_salida:
            json.dump(diccionarioPalabras, archivo_salida, indent=2)
        """
        completaFrase(sys.argv[1], diccionarioPalabras, mayorFrecuencia(palabrasList))
        fLectura.close()

if __name__ == "__main__":
    main()