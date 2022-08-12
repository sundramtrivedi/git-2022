#include<stdio.h>
#include<stdlib.h>
int main()
{
	int a;
	printf("\n * Enter the integer number :");
	scanf("%d",&a);
	void *pt;
	pt = &a;
	printf("\n Value of pointer in integer : %d \n",*(int *)pt);
	char ch;
	printf("\n * Enter the character :");
	scanf("%s",&ch);
	void *b;
	b = &ch;
	printf("\n Value of pointer in character : %d \n",*(char *)b);
	float c;
	printf("\n * Enter the float number :");
	scanf("%f",&c);
	void *d;
	d = &c;
	printf("\n Value of pointer : %f \n",*(float *)d);
	return 0;
}
