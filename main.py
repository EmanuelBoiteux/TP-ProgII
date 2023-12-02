import sys

def readArchivo(nombre):
    rutaArchivo = f"Entradas/{nombre}.txt"
    fLectura = open(rutaArchivo, 'r')
    fLectura.close()

def completaFrase(nombre):
    rutaArchivo = f"Frases/{nombre}.txt"
    frasesArchivo = open(rutaArchivo, 'r')
    frasesArchivo.close()

def main():
    if len(sys.argv) != 2:
        print("Numero de argumentos incorrecto")
    else:
        readArchivo(sys.argv[1])
        completaFrase(sys.argv[1])

if __name__ == "__main__":
    main()