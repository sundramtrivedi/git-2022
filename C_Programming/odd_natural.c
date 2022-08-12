#include<stdio.h>
void odd(int *num)
{
	for(int i = 1 ; i <= (*num) ; i++)
	{
		if((i % 2) != 0)
		{
			printf("\n %d",i);
		}
	}
}
void sum_odd(int *num)
{
	int sum=0;
	for(int i = 1 ; i <= (*num) ; i++)
	{
		if((i % 2) != 0)
		{
			sum = sum + i;
		}
	}
	printf("\n Sum of odd natural numbers : %d \n",sum);
}
int main()
{
	int num;
	int sum=0;
	printf("\n Enter the number :");
	scanf("%d",&num);
	odd(&num);
	sum_odd(&num);
	return 0;
}
