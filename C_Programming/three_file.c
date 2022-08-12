/*
Q5. Define your own iterative functions for
(using array notation as well as exclusively using pointers)
a) finding length
b) concatenation
c) comparision
d) reversing in memory
e) finding first occurrence of given character
f)finding last occurrence of given character
h)counting no.of occurences of a given character
i) finding a substring in a main string
*/
#include<stdio.h>
#include<string.h>
#include"header.h"
int main()
{	//Input	
	char one[100];
	char two[100];
	printf("Enter first string: ");
	scanf("%s",one);
	printf("Enter second string: ");
	scanf("%s",two);

	//Length
	int len = str_len(one);
	printf("\nLength of string %s is %d \n",one,len);

	//Compare
	int res = str_cmp(one,two);
	if(res)
	{
		printf("\nCompared String matched\n");
	}
	else
	{
		printf("\nCompared String did not matched\n");
	}

	//Reverse
	rev(one);
	printf("\nString After Reverse\n: %s",one);

	//Concatination
	char three[100];
	str_con(one,two,three);
	printf("\nThe concatenated string is %s\n",three);

	//	
	rev(one);
	char ch;
	printf("Enter character to be searched: ");
	scanf("%c",&ch);
	scanf("%c",&ch);
	int k = str_ocu(one,ch);
	printf("\n First occurenece: %d \n",k);

	char c;
	printf("\nEnter character to be searched: \n");
	scanf("%c",&c);
	scanf("%c",&c);
	int m = str_ocu1(one,c);
	printf("\nLast occurenece: %d \n",m);

	char cha;
	printf("Enter character to be searched: ");
	scanf("%c",&cha);
	scanf("%c",&cha);
	int n = str_ocu2(one,cha);
	printf("\nNumber of occurenece: %d\n",n);


	return 0;
}
