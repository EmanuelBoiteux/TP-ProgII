#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <ctype.h>

void limpiaTexto(FILE* archivo, char persona[]){
    FILE* salida;
    char direc[255];

    snprintf(direc, 255, "Entradas/%s.txt", persona);
    salida = fopen(direc, "a");
    
    char c = fgetc(archivo);
    while(c != EOF){
        if (isspace(c)){
            while((c = fgetc(archivo)) == ' ');
            ungetc(c, archivo);
            fputc(' ', salida);
        }
        else if (c == '\n'){
            fputc(' ', salida);
        }
        else if (c == '.'){
            if ((c = fgetc(archivo)) != ' ' && c != '\n'){
                ungetc(c, archivo);
            }
            fputc('\n', salida);
        }
        else if (isalpha(c)){
            fputc(tolower(c), salida);
        }
        c = fgetc(archivo);
    }

    fclose(salida);
}


char* creaRuta(char persona[]){
    char* ruta = malloc(100);
    //snprintf(ruta, sizeof(ruta), "Textos/%s/archivo.txt", persona);
    strcat(strcat(strcpy(ruta, "Textos/"), persona), "/archivo.txt");
    return ruta;
}

void getArchivos(char nombre[]){
    char comando[100];
    snprintf(comando, sizeof(comando), "cd Textos/%s && ls -I archivo.txt > archivo.txt", nombre);
    //strcat(strcat(strcpy(comando, "cd Textos/"), nombre), " && ls -I archivo.txt > archivo.txt");
    system(comando); 
}

void getNombre(char persona[]){

    /*
    FILE* archivo = fopen(creaRuta(persona), "r");
    char linea[255];
    */

    char ruta[100];
    snprintf(ruta, sizeof(ruta), "Textos/%s/archivo.txt", persona);
    FILE* archivo = fopen(ruta, "r");
    char linea[255];

    while(fgets(linea, 255, archivo) != NULL){
        char direc[300];
        snprintf(direc, 300, "Textos/%s/%s", persona, linea);
        direc[strlen(direc) - 1] = '\0';
        FILE* leeTexto = fopen(direc, "r");
        limpiaTexto(leeTexto, persona);
        fclose(leeTexto);
    }
    fclose(archivo);
}


int main(int argc, char *argv[]){

    getArchivos(argv[1]);
    getNombre(argv[1]);

    return 0;
}