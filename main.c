#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <ctype.h>

FILE* limpiaTexto(FILE* archivo){
    FILE* salida;
    salida = fopen("Textos/Entradas/Fito_Paez.txt", "w");

    char linea[255];

    for (int i = 0; fgets(linea, 255, archivo) != NULL; i++){
        for (int j = 0; j < strlen(linea) - 1; j++){
            if (isalpha(linea[j]) || isspace(linea[j])){
                fputc(linea[j], salida);
            }
            else if (linea[j] == '.'){
                fputs(".\n", salida);
            }
            else if (linea[j] == '\n'){
                fputc(' ', salida);
            }
        }
    }

    return salida;
}


char* creaRuta(char persona[]){
    char* ruta = malloc(100);
    strcpy(ruta, "Textos/");
    strcat(strcat(strcat(strcat(ruta, persona), "/"), persona), ".txt");
    return ruta;
}

void creaRutaTest(){
    char *ruta_test = creaRuta("Cerati");
    assert(strcmp(ruta_test, "Textos/Cerati/Cerati.txt") == 0);
    strcpy(ruta_test, creaRuta("Leo_Messi"));
    assert(strcmp(ruta_test, "Textos/Leo_Messi/Leo_Messi.txt") == 0);
    free(ruta_test);
}

int main(int argc, char *argv[]){
    FILE *archivo;

    // TEST
    creaRutaTest();
    // END TEST

    char* direc = creaRuta(argv[1]);
    archivo = fopen(direc, "r");

    limpiaTexto(archivo);
    /*
    char linea[255];
    fgets(linea, 255, archivo);
    printf("%s\n", linea);
    */

    //int r = system("cd Textos && ls");
    //printf("%d\n", r);

    free(direc);
    fclose(archivo);
    return 0;
}