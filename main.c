#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <ctype.h>

void limpiaTexto(FILE* archivo){
    FILE* salida;
    salida = fopen("Entradas/Fito_Paez.txt", "w");

    char linea[255];
    int punto = 1;
    for (int i = 0; fgets(linea, 255, archivo) != NULL; i++){
        for (int j = 0; j < strlen(linea) - 1; j++){
            if (isalpha(linea[j]) || isspace(linea[j])){
                if (isupper(linea[j])){
                    if (punto == 0){
                        fputc(' ', salida);
                        fputc(tolower(linea[j]), salida);
                    }
                    else {
                        fputc(tolower(linea[j]), salida);
                        punto = 0;
                    }
                }
                else {
                    fputc(linea[j], salida);
                    punto = 0;
                }
            }
            else if (linea[j] == '.'){
                punto = 1;
                fputc('\n', salida);
            }
        }
    }
    fclose(salida);
}


char* creaRuta(char persona[]){
    char* ruta = malloc(100);
    strcat(strcpy(ruta, "Textos/"), persona);
    return ruta;
}



int main(int argc, char *argv[]){
    FILE *archivo;

    // TEST
    //creaRutaTest();
    // END TEST

    char* direc = creaRuta(argv[1]);
    archivo = fopen(direc, "r");

    printf("%s\n", direc);
    char ruta[30];
    strcat(strcat(strcpy(ruta, "cd "), direc), " && ls");
    printf("%s\n", ruta);

    int r = system(ruta);
    printf("%d\n", r);

    limpiaTexto(archivo);
    
    free(direc);
    fclose(archivo);
    return 0;
}