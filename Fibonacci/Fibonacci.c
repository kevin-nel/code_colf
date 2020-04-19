void fib(int n){
	static int i=0, j=1, k;
    if(n>0){
      k = i + j;
      printf("%d\n", k);
      i = j;
      j = k;
      fib(n-1);
    }
}
int main(){
    printf("%d\n%d\n",0,1);
    fib(29);
}