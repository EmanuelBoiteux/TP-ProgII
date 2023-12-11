from main import *
import json


def test_listaPalabras():
    # Test 1
    ruta = f"Test/Test Python/palabrasTest1.txt"
    archivo1 = open(ruta, "r")
    resultado = listaPalabras(archivo1)
    lista = ['sabes', 'sabes', 'sabes', '-', 'mi', 'mi', 'nunca', 'nunca', '-', 'nunca', 'nunca', 'nunca','-']
    assert resultado == lista
    archivo1.close()

    # Test 2
    ruta = f"Test/Test Python/palabrasTest2.txt"
    archivo2 = open(ruta, "r")
    resultado = listaPalabras(archivo2)
    lista = ["en", "un", "pequeno", "pueblo", "habia", "un", "antiguo", "puente", "de", "madera", "que", 
                "cruzaba", "un", "sereno", "rio", '-', "los", "lugarenos", "solian", "cruzar", "el", "puente", "todos", 
                "los", "dias", "para", "llegar", "a", "sus", "trabajos", "o", "simplemente", "pasear", '-', "un", "dia", "un", 
                "grupo", "de", "ninos", "decidio", "explorar", "la", "zona", "y", "descubrieron", "un", "escondite", "secreto", 
                "debajo", "del", "puente",'-', "el", "escondite", "estaba", "lleno", "de", "tesoros", "olvidados", "y", "juguetes", "rotos", '-',
                "los", "ninos", "decidieron", "compartir", "sus", "hallazgos", "con", "el", "resto", "de", "la", "comunidad", '-', "la", 
                "noticia", "se", "extendio", "rapidamente", "y", "pronto", "el", "puente", "se", "convirtio", "en", "un", "lugar", 
                "de", "encuentro", "donde", "la", "gente", "intercambiaba", "historias", "y", "risas", '-', "el", "antiguo", "puente", 
                "con", "sus", "recuerdos", "repetidos", "se", "convirtio", "en", "un", "simbolo", "de", "unidad", "para", "el", "pueblo",'-']
    assert resultado == lista
    archivo2.close()


def test_palabrasAntePos():
    listaPalabras = ["sol", "fuego", "en", "luna", "cielo", "mar", "aire", "flor", "hoja", "arbol", "puente", "fuego", "en", "rio", 
                  "arena", "fuego", "en", "gato", "perro", "pajaro", "pez", "nieve", "fuego", "solucion", 
                  "camino", "puente", "ventana", "flor", "coche", "bicicleta", "sombrero", "zapato", 
                  "mesa", "silla", "cama","fuego", "en", "planta", "libro", "lapiz", "papel", "hombre", "mujer", 
                  "nino", "nina", "amigo", "puente", "trabajo", "juego", "tiempo", "espacio", 
                  "mente", "corazon", "cuerpo", "vida", "luna", "mar", "fuego", "en", "aire", "flor", "hoja",
                  "arbol", "perro", "amigo", "puente", "fuego", "piedra"]

    # Test 1
    resultado = palabrasAntePos("puente", listaPalabras, 1)
    resultadoEsperado = {"arbol": 1, "camino": 1, "amigo": 2}
    assert resultado == resultadoEsperado

    # Test 2
    resultado = palabrasAntePos("fuego", listaPalabras, -1)
    resultadoEsperado = {"en": 5, "solucion": 1, "piedra": 1}
    assert resultado == resultadoEsperado

    # Test 3
    resultado = palabrasAntePos("sol", listaPalabras, 1)
    resultadoEsperado = {}
    assert resultado == resultadoEsperado

    # Test 4
    resultado = palabrasAntePos("piedra", listaPalabras, -1)
    resultadoEsperado = {}
    assert resultado == resultadoEsperado

    # Test 5
    listaVacia = []
    resultado = palabrasAntePos("puente", listaVacia, 1)
    resultadoEsperado = {}
    assert resultado == resultadoEsperado


def test_getPalabras():
    #Test 1
    archivo = open("Test/Test Python/diccionarioTest1.txt", "r")
    palabras = listaPalabras(archivo)

    resultado = getPalabras(archivo, palabras)
    resultadoEsperado = {"tus": {"anteriores": {"noche": 1},"siguientes": {"casa": 1, "pedidos": 1}},
                        "casa": {"anteriores": {"tus": 1, "sol": 1},"siguientes": {"mascota": 1, "en": 1}},
                        "mascota": {"anteriores": {"casa": 1, "noche": 1},"siguientes": {"sol": 2}},
                        "sol": {"anteriores": {"mascota": 2},"siguientes": {"casa": 1,"luna": 1}},
                        "en": {"anteriores": {"casa": 1}, "siguientes": {"la": 1}},
                        "la": {"anteriores": {"en": 1}, "siguientes": {}},
                        "ciudad": {"anteriores": {"pedidos": 1},"siguientes": {"noche": 2}},
                        "noche": {"anteriores": {"ciudad": 2},"siguientes": {"mascota": 1, "tus": 1}},
                        "luna": {"anteriores": {"sol": 1},"siguientes": {}},
                        "pedidos": {"anteriores": {"tus": 1},"siguientes": {"ciudad": 1}}}
    assert resultado == resultadoEsperado

    # Test 2
    archivo = open("Test/Test Python/diccionarioTest2.txt", "r")
    palabras = listaPalabras(archivo)

    resultado = getPalabras(archivo, palabras)
    resultadoEsperado = {"sol": {"anteriores": {"espacio": 1, "ciudad": 1},"siguientes": {"espacio": 2, "ciudad": 1}},
                        "espacio": {"anteriores": {"sol": 2, "perro": 1},"siguientes": {"sol": 1, "hoja": 1}},
                        "ciudad": {"anteriores": {"sol": 1, "flor": 1, "tiempo": 1, "perro": 1},"siguientes": {"sol": 1, "flor": 1,"hoja": 1}},
                        "perro": {"anteriores": {},"siguientes": {"espacio": 1, "ciudad": 1}},
                        "hoja": {"anteriores": {"espacio": 1,"ciudad": 1},"siguientes": {"tiempo": 1}},
                        "tiempo": {"anteriores": {"hoja": 1, "flor": 1},"siguientes": {"flor": 1, "ciudad": 1}},
                        "flor": {"anteriores": {"tiempo": 1, "ciudad": 1},"siguientes": {"ciudad": 1,"tiempo": 1}}}
    assert resultado == resultadoEsperado

    archivo.close()


def test_mayorFrecuencia():
    # Test 1
    listaTest1 = ["sol", "fuego", "en", "luna", "cielo", "mar", "aire", "flor", "hoja", "arbol", "puente", "fuego", "en", "rio", 
                  "arena", "fuego", "en", "gato", "perro", "pajaro", "pez", "nieve", "fuego", "solucion", 
                  "camino", "puente", "ventana", "flor", "coche", "bicicleta", "sombrero", "zapato", 
                  "mesa", "silla", "cama","fuego", "en", "planta", "libro", "lapiz", "papel", "hombre", "mujer", 
                  "nino", "nina", "amigo", "puente", "trabajo", "juego", "tiempo", "espacio", 
                  "mente", "corazon", "cuerpo", "vida", "luna", "mar", "fuego", "en", "aire", "flor", "hoja",
                  "arbol", "perro", "amigo", "puente", "fuego", "piedra"]
    resultado1 = mayorFrecuencia(listaTest1)
    assert resultado1 == "fuego"

    # Test 2
    listaTest2 = ["en", "un", "pequeno", "pueblo", "habia", "un", "antiguo", "puente", "de", "madera", "que", 
                "cruzaba", "un", "sereno", "rio", '-', "los", "lugarenos", "solian", "cruzar", "el", "puente", "todos", 
                "los", "dias", "para", "llegar", "a", "sus", "trabajos", "o", "simplemente", "pasear", '-', "un", "dia", "un", 
                "grupo", "de", "ninos", "decidio", "explorar", "la", "zona", "y", "descubrieron", "un", "escondite", "secreto", 
                "debajo", "del", "puente",'-', "el", "escondite", "estaba", "lleno", "de", "tesoros", "olvidados", "y", "juguetes", "rotos", '-',
                "los", "ninos", "decidieron", "compartir", "sus", "hallazgos", "con", "el", "resto", "de", "la", "comunidad", '-', "la", 
                "noticia", "se", "extendio", "rapidamente", "y", "pronto", "el", "puente", "se", "convirtio", "en", "un", "lugar", 
                "de", "encuentro", "donde", "la", "gente", "intercambiaba", "historias", "y", "risas", '-', "el", "antiguo", "puente", 
                "con", "sus", "recuerdos", "repetidos", "se", "convirtio", "en", "un", "simbolo", "de", "unidad", "para", "el", "pueblo",'-']
    resultado2 = mayorFrecuencia(listaTest2)
    assert resultado2 == "un"


def test_completaFrase_remplazaGuion():
    # Test 1
    archivo1 = open("Test/Test Python/diccionarioTest1.txt", "r")
    palabras = listaPalabras(archivo1)
    diccionarioPalabras = getPalabras(archivo1, palabras)
    completaFrase("frasesTest1", diccionarioPalabras, mayorFrecuencia(palabras))
    archivoSalida = open("Salidas/frasesTest1.txt", "r")
    assert archivoSalida.readline() == "ciudad noche oscura\n"
    assert archivoSalida.readline() == "tranquila ciudad noche\n"
    assert archivoSalida.readline() == "brilla mascota sol\n"
    frec = mayorFrecuencia(palabras)
    assert archivoSalida.readline() == f"la {frec} estaba tranquila\n"
    assert archivoSalida.readline() == "tus\n"
    archivo1.close()

    # Test 2
    archivo2 = open("Test/Test Python/diccionarioTest2.txt", "r")
    palabras = listaPalabras(archivo2)
    diccionarioPalabras = getPalabras(archivo2, palabras)
    completaFrase("frasesTest2", diccionarioPalabras, mayorFrecuencia(palabras))
    archivoSalida = open("Salidas/frasesTest2.txt", "r")
    assert archivoSalida.readline() == "sol espacio\n"
    assert archivoSalida.readline() == "sol espacio\n"
    frec = mayorFrecuencia(palabras)
    assert archivoSalida.readline() == f"{frec} perro\n"
    assert archivoSalida.readline() == "hoja tiempo\n"
    assert archivoSalida.readline() == "sol ciudad\n"
    assert archivoSalida.readline() == "montana ciudad noche\n"
    archivo2.close()

def test_masRepetida():
    archivo1 = open("Test/Test Python/diccionarioTest1.txt", "r")
    palabras = listaPalabras(archivo1)
    diccionarioTest1 = getPalabras(archivo1, palabras)

    # Test 1
    masRepetida1= masRepetida(diccionarioTest1["ciudad"]["siguientes"])
    assert masRepetida1 == "noche"

    # Test 2
    masRepetida2= masRepetida(diccionarioTest1["casa"]["siguientes"])
    assert masRepetida2 == "mascota"

    archivo1.close()

    archivo2 = open("Test/Test Python/diccionarioTest2.txt", "r")
    palabras = listaPalabras(archivo2)
    diccionarioTest1 = getPalabras(archivo2, palabras)

    # Test 3
    masRepetida3= masRepetida(diccionarioTest1["espacio"]["anteriores"])
    assert masRepetida3 == "sol"

    # Test 4
    masRepetida4= masRepetida(diccionarioTest1["perro"]["anteriores"])
    assert masRepetida4 == ""

    archivo2.close()