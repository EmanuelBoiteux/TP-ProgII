#include "main.h"

/*
void creaRutaTest(){
    char *ruta_test = creaRuta("Cerati");
    assert(strcmp(ruta_test, "Textos/Cerati/Cerati.txt") == 0);
    strcpy(ruta_test, creaRuta("Leo_Messi"));
    assert(strcmp(ruta_test, "Textos/Leo_Messi/Leo_Messi.txt") == 0);
    free(ruta_test);
}
*/

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

/*
void test_getNombre(){

}
*/

void test_limpiaTexto(){
    char ruta[255] = "Textos/Abel_Pintos/motivos.txt";
    char rutaTest[255] = "Test Salidas/motivosSalida.txt";
    FILE* resultado = fopen(ruta, "r");
    FILE* archivoTest = fopen(rutaTest, "r");

    limpiaTexto(resultado, "Abel_Pintos");

    FILE* archivoSalida = fopen("Entradas/Abel_Pintos.txt", "r");
    
    char salida = fgetc(archivoSalida);
    char test = fgetc(archivoTest);
    
    while (salida != EOF && test != EOF){
        printf("%c %c\n", salida, test);
        assert(salida == test);
        salida = fgetc(archivoSalida);
        test = fgetc(archivoTest);
    }

    fclose(resultado);
    fclose(archivoTest);
}

int main(){
    //test_getArchivos();
    test_limpiaTexto();
    return 0;
}