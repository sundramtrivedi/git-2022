#include<stdio.h>
// int main(count of argument,argument array)
int main(int argc,char *argv[])
{
	printf("\n Number of arguments : %d \n",argc);
	for(int i=0;i<argc;i++)
	{
		printf("\n argv : %s \n",argv[i]);
	}
	return 0;
}
