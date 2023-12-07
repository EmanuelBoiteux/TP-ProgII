#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <ctype.h>
#include "head.h"
//#include "programa.h"

void creaRutaTest(){
    char *ruta_test = creaRuta("Cerati");
    assert(strcmp(ruta_test, "Textos/Cerati/Cerati.txt") == 0);
    strcpy(ruta_test, creaRuta("Leo_Messi"));
    assert(strcmp(ruta_test, "Textos/Leo_Messi/Leo_Messi.txt") == 0);
    free(ruta_test);
}
