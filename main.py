import sys

def readArchivo(nombre):
    rutaArchivo = f"Entradas/{nombre}.txt"
    fLectura = open(rutaArchivo, 'r')
    #print(fLectura.readlines())
    listaPalabras(fLectura)
    #getPalabras(fLectura)
    fLectura.close()

def completaFrase(nombre):
    rutaArchivo = f"Frases/{nombre}.txt"
    frasesArchivo = open(rutaArchivo, 'r')
    lineasArchivo = frasesArchivo.readlines()
    frasesArchivo.close()
    """
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

def listaPalabras(archivo):
    palabras = []
    for linea in archivo:
        linea = linea.split(' ')
        largo = len(linea)
        for i in range(0, largo):
            if linea[i] not in palabras:
                if i == largo - 1:
                    palabras.append(linea[i][:-1])
                else:
                    palabras.append(linea[i])

def getPalabras(archivo):
    texto = archivo.readlines()
    dictPalabras = {}
    palabras = []
    for linea in texto:
        palabras = linea.split(' ')

        for palabra in palabras:
            if palabra not in dictPalabras and palabra != '\n':
                #print(palabra)
                palabrasAnteriores(palabra, archivo)
                dictPalabras[palabra] = {"anterior": 1, "siguiente": 2}
    #print(dictPalabras)

def palabrasAnteriores(palabra, archivo):
    anteriores = []
    texto = archivo.readlines()
    print(texto)
    for linea in texto:
        palabras = linea.split(' ')
        print(palabras)

    return anteriores


def main():
    if len(sys.argv) != 2:
        print("Numero de argumentos incorrecto")
    else:
        readArchivo(sys.argv[1])
        completaFrase(sys.argv[1])

if __name__ == "__main__":
    main()
