#include<stdio.h>
int main()
{
	FILE *fd = fopen("calc.txt","r+");
	int a=3;
	int b=2;
	fscanf(fd,"%d%d",&a,&b);
	printf("\n a=%d,b=%d \n",a,b);
	fprintf(fd,"Sum is : %d \n",a+b);
	printf("Sum is : %d \n",a+b);
	return 0;
}
