#include<stdio.h>
#include<stdlib.h>
void input(int *c,int *d)
{
	printf("\n Enter the 1st array \n");
	for(int i=0;i<10;i++)
	{
		printf("\n Enter the array a[%d] = ",i);
		scanf("%d",&c[i]);
	}
	printf("\n Enter the 2nd array \n");
	for(int i=0;i<10;i++)
	{
		printf("\n Enter the array b[%d] = ",i);
		scanf("%d",&d[i]);
	}
	printf("\n 1st array \n");
	for(int i=0;i<10;i++)
	{  
		printf("\n %d -> %d \n",i,c[i]);
	}
	printf("\n 2nd array \n");
	for(int i=0;i<10;i++)
	{
		printf("\n %d -> %d \n",i,d[i]);
	}
}
void add(int *c,int *d)
{
	printf("\n Addition of two array \n");
	for(int i=0;i<10;i++)
	{
		printf("\n Sum : c[%d] + d[%d] -> %d \n",i,i,(c[i] + d[i]));
	}
}
int main()
{
	int *c = malloc(sizeof(int)*10);
	int *d = malloc(sizeof(int)*10);
	input(c,d);
	add(c,d);
	return 0;
}
