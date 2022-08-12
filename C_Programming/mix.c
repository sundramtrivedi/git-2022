#include<stdio.h>

int str_len(char* str) //char* str: We are using pointer so we can access the variable(one) in the main function.Pointer holds the address.
			// data type of address is char pointer.Char* str = 8 bytes beacuse it is char pointer and it holds address.
{ 
	int i = 0;
		while(str[i] != '\0')
		{
		i++;
		}
	return i;
}

int str_cmp(char* stri, char* strj)
{
	int i=0;
	while (stri[i] != '\0')
	{
		if( stri[i] != strj[i] )
		{
			break;
		}
		i++;
	}
	if( stri[i] == '\0' && strj[i] == '\0')
	{
		return 1; //true
	} 
	return 0; // false
}

int rev(char *string)
{
 	char temp;
	int i,j,n;
	n = str_len(string);

	for(i=0,j=n - 1;i<j;++i,j--)
	{
		temp=string[j];
		string[j]=string[i];
		string[i]=temp;
	}
}

void str_con(char *str1, char *str2,char *str3)
{ 
	int i=0,j=0;
	
	while(str1[i] != '\0')
	{
		str3[j]=str1[i];
		i++;
		j++;
	}
	i=0;
	while(str2[i] != '\0')
	{
		str3[j]=str2[i];
		i++;
		j++;
		
	}
	str3[j] = '\0';

 }

int str_ocu(char *str,char ch)
{
	int i=0,flag=0;
	while(str[i] != '\0')
	{
		if(str[i]==ch)
		{
			flag++;
			break;
			
		}
		i++;
	}
	if(flag==0)
	{
		printf("Not found");
	}
	else			
	return i;
}

int str_ocu1(char *st,char c)
{
	int i=0,flag=0;
	while(st[i] != '\0')
	{
		if(st[i] == c)
		{
			flag++;
			flag=i;
			
		}
		i++;
	}
	if(flag == 0)
	{
		printf("Not found");
	}
	else		
	return flag;
}			

int str_ocu2(char *stra,char cha)
{
	int i=0,flag=0;
	while(stra[i] != '\0')
	{
		if(stra[i] == cha)
		{
			flag++;
			
		}
	i++;	
	}
				
	return flag;
}

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




	

			
