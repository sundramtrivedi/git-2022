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
	int i=0;
	int flag=0;
	if(num > 1)
	{
		for(i=2;i<num;i++)
		{
			if( num % i == 0)
			{
				flag = 1;
			}
		}
		if(flag == 0)
		{
			printf("\n The number is prime number \n");
		}
		else
		{
			printf("\n The number is not prime number \n");
		}
	}	
}
int main()
{
	int a = input();
	prime(a);
	return 0;
}
