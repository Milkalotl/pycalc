#include <stdlib.h>
//#include <stdio.h>
#include <string.h>

int main(int argc, char** argv){
  char * allparams;
  char * pyparam = "python3 pycalc.py";
  size_t argvsize = 0;
  
  for(int e = 1; e < argc; e++){
    argvsize +=(strlen(argv[e]));
  }
  allparams = malloc((argvsize + strlen(pyparam)+ argc)* sizeof(char) + 2);
  strcat(allparams, pyparam);
  for(int e = 1; e < argc; e++){
    strcat(allparams, " ");
    strcat(allparams, argv[e]);
  }
  //printf("%ld", argvsize);
  //printf("\n%s", allparams);
  system(allparams);
  free(allparams);
  return 0;
}
