#include "main.h"

void limpiaTexto(FILE* archivo, char persona[]){
    FILE* salida;
    char direc[50];

    snprintf(direc, sizeof(direc), "Entradas/%s.txt", persona);
    salida = fopen(direc, "a");
    
    int espacio = 0;
    int letra = 0;
    char c = fgetc(archivo);
    while(c != EOF){
        if (c == '\r'){
            c = fgetc(archivo);
        } 
        else if (isspace(c) && c != '\n'){
            while(c == ' '){
                c = fgetc(archivo);
            }
            ungetc(c, archivo);
            fputc(' ', salida);
            espacio = 1;
            letra = 0;
        }
        else if (c == '\n' && isalpha(c = fgetc(archivo)) && espacio == 0 && letra == 1){
            fputc(' ', salida);
            ungetc(c, archivo);
            espacio = 1;
            letra = 0;
        }
        else if (c == '.'){
            if ((c = fgetc(archivo)) != ' ' && c != '\n'){
                ungetc(c, archivo);
            }
            fputc('\n', salida);
            espacio = 0;
            letra = 0;
        }
        else if (isalpha(c)){
            fputc(tolower(c), salida);
            espacio = 0;
            letra = 1;
        }
        c = fgetc(archivo);
    }

    fclose(salida);
}

void getArchivos(char nombre[]){
    char comando[255];
    snprintf(comando, sizeof(comando), "cd Textos/%s && ls -I archivo.txt > archivo.txt", nombre);
    system(comando); 
}

void getNombre(char persona[]){

    char ruta[100];
    snprintf(ruta, sizeof(ruta), "Textos/%s/archivo.txt", persona);
    FILE* archivo = fopen(ruta, "r");
    char linea[255];

    while(fgets(linea, sizeof(linea), archivo) != NULL){
        char direc[300];
        snprintf(direc, sizeof(direc), "Textos/%s/%s", persona, linea);
        direc[strlen(direc) - 1] = '\0';
        FILE* leeTexto = fopen(direc, "r");
        limpiaTexto(leeTexto, persona);
        fclose(leeTexto);
    }
    fclose(archivo);
}

void inicializePython(char nombre[]){
    char rutaPython[100];
    snprintf(rutaPython, sizeof(rutaPython), "python main.py %s", nombre);
    system(rutaPython);
}