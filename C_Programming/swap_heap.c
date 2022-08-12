#include<stdio.h>
#include<stdlib.h>
void swap( int *c, int *d)
{
	int temp;
	temp = *c;
	*c = *d;
	*d = temp;
}
int main()
{
	int a;
	int b;
	int *c = malloc(sizeof(a));
	int *d = malloc(sizeof(b));
	printf("\n Enter the number a :");
	scanf("%d",&a);
	printf("\n Enter the number b :");
	scanf("%d",&b);
	printf("Before swap : a = %d \t b = %d\n",a,b);
	swap(&a,&b);
	printf("After swap : a = %d \t b = %d \n",a,b);
	free(c);
	free(d);
	return 0;
}
