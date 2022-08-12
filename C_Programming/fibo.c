#include<stdio.h>
int input()
{
	int num;
	printf("\n Enter the value of n :");
	scanf("%d",&num);
	return num;
}
void fibo(int num)
{
	int i=0;
	int t1=0;
	int t2=1;
	int next_term=t1+t2;
	printf("\n %d ",t1);
	printf("\n %d ",t2);
	printf("\n %d ",next_term);
	for(i=3;i<=num;i++)
	{
		t1 = t2;
		t2 = next_term;
		next_term = t1 + t2;
		printf("\n %d ",next_term);
	}
}
int main()
{
	int a = input();
	fibo(a);
	return 0;
}
