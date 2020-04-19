main(){
printf(" ");
for(int k=3; k<10; k++){
	int b,n=k;
    for(int i=1; i<(k*2); i+=2){
    	for(int j=0; j<i; j++){
        	while(b<n){
          		printf(" ");
          		b++;
        	}
        	printf("*");
      	}
      	b=0;
      	n--;
      	printf("\n");
    }
    while(b<k){
    	printf(" ");
      	b++;
    }
    b=0;
    printf("*\n\n");  
  }
}