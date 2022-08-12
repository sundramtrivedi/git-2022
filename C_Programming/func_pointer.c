#include<stdio.h>
int add(int a, int b)
{
	return (a+b);
}
int sub(int a, int b)
{
	return (a-b);
}
int mul(int a, int b)
{
	return (a*b);
}
int div(int a, int b)
{
	return (a/b);
}
int function(int (*f)(int,int), int a, int b) //wrapper function
{
	return f(a,b);
}
int main()
{
	int a;
	int b;
	int ch;
	int (*fun) (int,int); // add function declaration
	int (*fun1) (int,int);
	int (*fun2) (int,int);
	int (*fun3) (int,int);
	fun = &add;
	fun1 = &sub; // function calling
	fun2 = &mul;
	fun3 = &div;
	printf("\n [1] Addition ");
	printf("\n [2] Substraction ");
	printf("\n [3] Multiplication ");
	printf("\n [4] Division ");
	printf("\n [5] Exit ");
	printf("\n Enter the choice : ");
	scanf("%d",&ch);
	printf("\n Enter the value of a :");
	scanf("%d",&a);
	printf("\n Enter the value of b :");
	scanf("%d",&b);
	if(ch == 1)
	{
		int res = function(add,a,b);
		printf("\n Result add (%d + %d) : %d \n",a,b,res);
	}
	else if(ch == 2)
	{
		int res1 = function(sub,a,b);
		printf("\n Result sub (%d - %d) : %d \n",a,b,res1);
	}
	else if(ch == 3)
	{
		int res2 = function(mul,a,b);
		printf("\n Result mul (%d - %d) : %d \n",a,b,res2);
	}
	else if(ch == 4)
	{
		int res3 = function(div,a,b);
		printf("\n Result div (%d - %d) : %d \n",a,b,res3);
	}
	return 0;
}
