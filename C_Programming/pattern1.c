#include<stdio.h>
int main()
{
	int num;
	int i=0;
	int j=0;
	printf("Enter the number=");
	scanf("%d",&num);
	for(i=0;i<=num;i++)
	{
		for(j=1;j<=i+1;j++)
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}
