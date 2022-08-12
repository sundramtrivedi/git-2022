#include<stdio.h>
int input()
{
	int n;
	printf("\n Enter the value of n : ");
	scanf("%d",&n);
	return n;
}
void n_even(int n)
{
	int i;
	for(i=0;i<n;i++)
	{
		if(i % 2 == 0)
		{
			printf("\n %d ",i);
		}
	}
}
int main()
{
	int a = input();
	n_even(a);
	return 0;
}
