#include<stdio.h>
char input()
{
	char ch;
	printf("\n Enter the upper case alphabet :");
	scanf("%c",&ch);
	return ch;
}
char lower_case(char ch)
{
	return (ch + 32);
}
int main()
{
	char a = input();
	char l = lower_case(a);
	printf("\n Lower case alphabet : %c \n",l);
	return 0;
}
