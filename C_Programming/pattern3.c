#include<stdio.h>
int main()
{
	int num;
	int i=0;
	int j=0;
	printf("Enter the number = ");
	scanf("%d",&num);
	for(i=1;i<=num;i++)
	{
		for(j=2;j<=i+1;j++)
		{
			printf("%d",i);	
		}
		printf("\n");
	}
	return 0;
}
