#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <ctype.h>

void getArchivos(char nombre[]);
// getArchivos recibe el nombre de una persona y crea un archivo de texto que en cada linea tiene el nombre 
// de los archivos que se encuentran en la carpeta Textos/<nombre recibido>. Utiliza la funcion system.

void getNombre(char persona[]);
// Esta funcion recibe el nombre de una persona y lee el archivo creado por la funcion getArchivos() linea por linea.
// A cada linea leida, le elimina el caracter '\0'. Luego, llama a la funcion limpiaTexto.

void limpiaTexto(FILE* archivo, char persona[]);
// Esta funcion recibe un puntero a un archivo de texto y el nombre de una persona, y luego crea un nuevo archivo de texto
// donde solo hay caracteres correspondinetes a letras minusculas y saltos de linea. Se eliminan los caracteres especiales, simbolos,
// y las letras mayusculas son pasadas a minusculas. Este archivo es creado en la carpeta Entradas con el nombre de la persona recibida.

void inicializePython(char nombre[]);
// Esta funcion se encarga de llamar al programa de Python. Utiliza para ello la funcon system.
