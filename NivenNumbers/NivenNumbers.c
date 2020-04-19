#include<stdio.h>
main(){
  char j[3];
  int k = 0;
  for(int i=1; i<101; i++){
    sprintf(j, "%d", i); 
    for(int l=0; l<=sizeof(j); l++){
    	k += (int)j[l];
    }
    if (i%k==0)
    	printf("%s\n", j);
  }
}