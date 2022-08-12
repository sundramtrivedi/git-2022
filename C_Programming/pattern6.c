#include<stdio.h>
int main()
{
	int num;
	int i=0;
	int j=0;
	int k=0;
	int l=0;
	printf("Enter the number = ");
	scanf("%d",&num);
	for(i=1;i<=num;i++)
	{
		for(j=i;j<num;j++)
		{
			printf("1");
		}
		for(k=1;k<=(2*i-1);k++)
		{
			printf("*");
		}
		for(l=0;l<(num-i);l++)
		{
			printf("1");
		}
		printf("\n");
	}
	return 0;
}
