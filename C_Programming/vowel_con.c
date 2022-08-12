#include<stdio.h>
#include<string.h>
void count(char *str)
{
	int i;
	int len;
	int vowel = 0;
	int consonant = 0;
	len = strlen(str);
	for(i=0;i<len;i++)
	{
		if(str[i] >= 'a' && str[i] <= 'z' || str[i] >= 'A' && str[i] <= 'Z')
		{
			if(str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u' || str[i] == 'A' || str[i] == 'E' || str[i] == 'I' || str[i] == 'O' || str[i] == 'U')
			{
				vowel++;
			}
			else
			{
				consonant++;
			}
		}
	}
	printf("\n Vowels count : %d \n",vowel);
	printf("\n Consonants count : %d \n",consonant);
}
int main()
{
	char str[100];
	printf("\n Enter the string : ");
	scanf("%s",str);
	count(&str);
	return 0;
}
