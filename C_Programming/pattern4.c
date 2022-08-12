#include<stdio.h>
int main()
{
	int num;
	int i=0;
	int j=0;
	int k=0;
	printf("Enter the number = ");
	scanf("%d",&num);
	for(i=1;i<=num;i++)
	{
		for(j=i;j<num;j++)
		{
			printf(" ");
		}
		for(k=1;k<=i;k++)
		{
			printf("%d",i);
		}
		printf("\n");
	}
	return 0;
}
