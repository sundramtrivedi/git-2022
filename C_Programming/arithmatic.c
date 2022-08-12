#include<stdio.h>
int main()
{
	int a;
	int b;
	int sum=0;
	int substraction=0;
	int multiplication=0;
	int division=0;
	int modulas=0;
	int ch;
	FILE *fd = fopen("arith.txt","r+");
	fscanf(fd,"\n %d \n",&a);
	fscanf(fd,"\n %d \n",&b);
	printf("\n [1] Addition");
	printf("\n [2] Substraction");
	printf("\n [3] Multiplication");
	printf("\n [4] Division");
	printf("\n [5] Modulas");
	printf("\n [6] Exit");
	printf("\n Enter the choice :");
	scanf("%d",&ch);
	if(ch==1)
	{
		sum = a + b;
		fprintf(fd,"Sum is : %d \n",sum);
		printf("Sum of %d & %d : %d \n",a,b,sum);
	}
	else if(ch==2)
	{
		substraction = a - b;
		fprintf(fd,"Substraction is : %d \n",substraction);
		printf("Substraction of %d & %d : %d \n",a,b,substraction);
	}
	else if(ch==3)
	{
		multiplication = a * b;
		fprintf(fd,"Multiplication is : %d \n",multiplication);
		printf("Multiplication of %d & %d : %d \n",a,b,multiplication);
	}
	else if(ch==4)
	{
		division = a / b;
		fprintf(fd,"Division is : %d \n",division);
		printf("Division of %d & %d : %d \n",a,b,division);
	}
	else if(ch==5)
	{
		modulas = a % b;
		fprintf(fd,"Modulas is : %d \n",modulas);
		printf("Modulas of %d & %d : %d \n",a,b,modulas);
	}
	return 0;
}
