#include<stdio.h>
#include<string.h>
#include<stdlib.h>
void count_word(char *str)
{
	int i;
	int count = 0;
	int len = strlen(str);
	for(i=0;i<len;i++)
	{
		if(((int)str[i]) >= 65 && ((int)str[i]) <= 90 || ((int)str[i]) >= 97 && ((int)str[i]) <= 122)
		{
			count++;
		}
	}
	printf("\n Word count : %d \n",count);
}
int main()
{
	char *str = malloc(sizeof(char)*100);
	printf("\n Enter the string : ");
	fgets(str,100,stdin);
	count_word(str);
	return 0;
}
