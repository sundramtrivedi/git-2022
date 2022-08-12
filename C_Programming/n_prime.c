#include<stdio.h>
int input()
{
	int num;
	printf("\n Enter the value of n :");
	scanf("%d",&num);
	return num;
}
void prime(int num)
{
	int i;
	int j;
	int flag=0;
	if(num > 1)
	{
		for(i=2;i<num;i++)
		{
			for(j=2;j<num;j++)
			{
				if( i % j == 0)
				{
					break;
				}
			}
			if(i == j)
			{
				printf("\n %d ",i);	
			}
		}
	}
}
int main()
{
	int a = input();
	prime(a);
	return 0;
}
