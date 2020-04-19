main(){
  int n,b,t;
  for(int j=0;j<51;j++){
    while(n>1){
      n=j/2;
      b=j%2;
      t+=b;
      if(t%2!=0)
      	printf("%d\n",t);
    }
  }
}