#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
int main()
{
	int num;
	printf("\n Enter the value of number : ");
	scanf("%d",&num);
	int s = sqrt(pow(2,abs(num)));
	printf("\n The square root of given number is %d \n",s);
	
	char ch;
	printf("\n Enter the character : ");
	scanf("%c",&ch);
	scanf("%c",&ch);
	char c = toupper(ch);
	printf("\n Upper case : %c \n",c);
	return 0;
}
