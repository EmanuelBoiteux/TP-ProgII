#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <ctype.h>

void limpiaTexto(FILE* archivo, char persona[]){
    FILE* salida;
    char direc[255], linea[255];

    snprintf(direc, 255, "Entradas/%s.txt", persona);
    salida = fopen(direc, "a");
    /*
    int punto = 1;
    
    for (int i = 0; fgets(linea, 255, archivo) != NULL; i++){
        fputc(tolower(linea[0]), salida);
        for (int j = 1; j < strlen(linea); j++){
            if(linea[j] == '\n' && punto == 0){
                fputc(' ', salida);
            }
            else if ((isalpha(linea[j]) || isspace(linea[j])) && linea[j] != '\n'){
                if (isupper(linea[j])){
                    if (punto == 0){
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
             FUNCIONA CON CALAMARO
            else if (linea[j] == '.'){
                punto = 1;
                fputc('\n', salida);
                linea[j++] = '\0';
            }
            
            else if (linea[j] == '.'){

            }
        }
    }*/
    int punto = 1;
    int espacio = 0;
    for (int i = 0; fgets(linea, 255, archivo) != NULL; i++){
        fputc(tolower(linea[0]), salida);
        for (int j = 1; j < strlen(linea); j++){
            if (isspace(linea[j]) && punto == 0 && espacio == 0){
                fputc(' ', salida);
                espacio = 1;
            }
            else if (linea[j] == '\n' && punto == 0 && espacio == 0){
                fputc(' ', salida);
                espacio = 1;
            }
            else if (linea[j] == '.'){
                fputc('\n', salida);
                punto = 1;
                espacio = 0;
            }
            else if (isalpha(linea[j]) && linea[j] != '\n'){
                fputc(tolower(linea[j]), salida);
                punto = 0;
                espacio = 0;
            }
        }
    }

    fclose(salida);
}


char* creaRuta(char persona[]){
    char* ruta = malloc(100);
    strcat(strcat(strcpy(ruta, "Textos/"), persona), "/archivo.txt");
    return ruta;
}

void getArchivos(char nombre[]){
    char comando[100];
    strcat(strcat(strcpy(comando, "cd Textos/"), nombre), " && ls -I archivo.txt > archivo.txt");
    system(comando); 
}

void getNombre(char* persona){
    FILE* archivo = fopen(creaRuta(persona), "r");
    char linea[255];

    while(fgets(linea, 255, archivo) != NULL){
        char direc[255];
        snprintf(direc, 255, "Textos/%s/%s", persona, linea);
        direc[strlen(direc) - 1] = '\0';
        FILE* leeTexto = fopen(direc, "r");
        limpiaTexto(leeTexto, persona);
        fclose(leeTexto);
    }
}


int main(int argc, char *argv[]){

    getArchivos(argv[1]);
    getNombre(argv[1]);

    return 0;
}