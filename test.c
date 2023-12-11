#include "main.h"


void test_getArchivos(){
    // test 1
    getArchivos("Abel_Pintos");
    FILE* archivo = fopen("Textos/Abel_Pintos/archivo.txt", "r");
    char linea[255];
    fgets(linea, sizeof(linea), archivo);
    assert(strcmp(linea, "motivos.txt\n\0") == 0);
    fgets(linea, sizeof(linea), archivo);
    assert(strcmp(linea, "sinprincipionifinal.txt\n\0") == 0);
    fclose(archivo);

    // test 2
    getArchivos("Gustavo_Cerati");
    FILE* archivo2 = fopen("Textos/Gustavo_Cerati/archivo.txt", "r");
    char linea2[255];
    fgets(linea2, sizeof(linea2), archivo2);
    assert(strcmp(linea2, "adios.txt\n\0") == 0);
    fgets(linea2, sizeof(linea2), archivo2);
    assert(strcmp(linea2, "crimen.txt\n\0") == 0);
    fclose(archivo2);
}

void test_limpiaTexto(){
    char rutaTest1[255] = "Textos/Abel_Pintos/motivos.txt";
    char rutaTest2[255] = "Textos/Abel_Pintos/sinprincipionifinal.txt";
    char salidaEsperada[255] = "Test/Test C/Abel_Pintos.txt";
    FILE* archivoTest1 = fopen(rutaTest1, "r");
    FILE* archivoTest2 = fopen(rutaTest2, "r");
    FILE* archivoSalidaEsperada = fopen(salidaEsperada, "r");

    limpiaTexto(archivoTest1, "Abel_Pintos");
    limpiaTexto(archivoTest2, "Abel_Pintos");

    FILE* archivoSalida = fopen("Entradas/Abel_Pintos.txt", "r");
    
    char salida = fgetc(archivoSalidaEsperada);
    char test = fgetc(archivoSalida);
    
    while (salida != EOF && test != EOF){
        //printf("%c %c\n", salida, test);
        assert(salida == test);
        salida = fgetc(archivoSalidaEsperada);
        test = fgetc(archivoSalida);
    } // TESTEAR TERMINAR UNA LINEA CON MUCHOS ESPACIO A VER QUE PASA

    fclose(archivoTest1);
    fclose(archivoTest2);
    fclose(archivoSalida);
}


void test_getNombre(){
    getNombre("Gustavo_Cerati");
    FILE* archivoS = fopen("Entradas/Gustavo_Cerati.txt", "r");
    char linea[255];
    // Test 1
    fgets(linea, sizeof(linea), archivoS);
    assert(strcmp(linea, "archivo abierto correctamente\n") == 0);
    // Test 2
    fgets(linea, sizeof(linea), archivoS);
    assert(strcmp(linea, "segundo archivo abierto correctamente\n") == 0);
    fclose(archivoS);
}

int main(){
    test_getArchivos();
    test_limpiaTexto();
    test_getNombre();
    return 0;
}