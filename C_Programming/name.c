#include<stdio.h>
int main()
{
	FILE *fd = fopen("name.txt","r+");
	char ch[100];
	printf("\n Enter the Name of user :");
	scanf("%s",ch);
	fprintf(fd,"%s",ch);
	return 0;
}
