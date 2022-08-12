#include<stdio.h>
#include<stdlib.h>
int main()
{
	int *x = malloc(sizeof(char));
	x = realloc(x,sizeof(int)); // reallocating the memory 1 to 4 bytes
	scanf("%d",x);
	printf("\n Data = %d \n",*x);
	return 0;
}
