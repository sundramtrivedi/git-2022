#include<stdio.h>
char input()
{
	char ch;
	printf("\n Enter the lower case alphabet :");
	scanf("%c",&ch);
	return ch;
}
char upper_case(char ch)
{
	return (ch - 32);
}
int main()
{
	char a = input();
	char u = upper_case(a);
	printf("\n Upper case alphabet : %c \n",u);
	return 0;
}
