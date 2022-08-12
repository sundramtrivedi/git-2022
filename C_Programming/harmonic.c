#include<stdio.h>
void harmonic(int num)
{
	int i;
	double sum=0.0;
	for(i=1;i<=(num);i++)
	{
		sum = sum + (1.0 / i) ;
	}
	printf("\n Sum : %f \n",sum);
}
int main()
{
	int num;
	printf("\n Enter the number :");
	scanf("%d",&num);
	harmonic(num);
	return 0;
}
