#include<stdio.h>
int input()
{
	int num;
	printf("\n Enter the number : ");
	scanf("%d",&num);
	return num;
}
void check_palindrome(int num)
{
	int temp;
	int rev=0;
	int rem;
	temp = num;
	while(num != 0)
	{
		rem = num % 10;
		rev = (rev * 10) + rem;
		num = num / 10;
	}
	if(rev == temp)
	{
		printf("\n Given number is palindrome \n");
	}
	else
	{
		printf("\n Given number is not palindrome \n");
	}
}
int main()
{
	int a = input();
	check_palindrome(a);	
	return 0;
}
