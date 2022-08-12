#include<stdio.h>
void max_num(int *num1,int *num2)
{
	if((*num1)>(*num2))
	{
		printf("\n The max number in %d and %d is %d \n",(*num1),(*num2),(*num1));
	}
	else 
	{
		printf("\n The max number in %d and %d is %d \n",(*num1),(*num2),(*num2));
	}
}
int main()
{
	int num1;
	int num2;
	printf("\n Enter the number num1 :");
	scanf("%d",&num1);
	printf("\n Enter the number num2 :");
	scanf("%d",&num2);
	max_num(&num1,&num2);
	return 0;
}
