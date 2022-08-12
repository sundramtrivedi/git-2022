#include<stdio.h>
#include<stdlib.h>
int main()
{
	// dynamic memory allocation
	// heap
	// malloc : simply allocates a single block of memory
	// calloc : allocates block of memory and block contains multiple memory
	// realoc : realllocate memory
	// free : free the memory
	int *x = malloc(sizeof(int));
	printf("\n Enter the int data");
	scanf("%d",x);
	printf("\n Data : %d \n",*(int *)x);
	free(x);
	return 0;
}
