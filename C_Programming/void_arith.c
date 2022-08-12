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
	
	int p;
	printf("\n * Enter the integer number :");
	scanf("%d",&p);
	void *rt;
	rt = &p;
	printf("\n Value of pointer in integer : %d \n",*(int *)rt);
	
	char ch;
	printf("\n * Enter the character :");
	scanf("%c",&ch);
	scanf("%c",&ch);
	void *b;
	b = &ch;
	printf("\n Value of pointer in character : %d \n",*(char *)b);
	
	char vh;
	printf("\n * Enter the character :");
	scanf("%c",&vh);
	scanf("%c",&vh);
	void *q;
	q = &vh;
	printf("\n Value of pointer in character : %d \n",*(char *)q);
	
	float c;
	printf("\n * Enter the float number :");
	scanf("%f",&c);
	void *d;
	d = &c;
	printf("\n Value of pointer : %f \n",*(float *)d);
	
	float k;
	printf("\n * Enter the float number :");
	scanf("%f",&k);
	void *l;
	l = &k;
	printf("\n Value of pointer : %f \n",*(float *)l);
	
	printf("\n Arithmatic Operations on void pointer");
	printf("\n Addition of void pointer (int) : %d \n",((*(int *)pt) + (*(int *)rt)));
	
	printf("\n Arithmatic Operations on void pointer");
	printf("\n Addition of void pointer (char) : %c \n",((*(char *)b) + (*(char *)q)));
	
	printf("\n Arithmatic Operations on void pointer");
	printf("\n Addition of void pointer (float) : %f \n",((*(float *)d) + (*(float *)l)));
	return 0;
}
