#include<stdio.h>
int main()
{
	// fopen will load the file in RAM and returns a pointer to that file
	FILE *fd = fopen("data.txt","r+");
	char data[100];
	// reading from file
	fread(data,8,1,fd);
	printf("Data from file : %s \n",data);
	// writing into the file
	char str[100];
	printf("\n Enter some data to write into the file : \n");
	scanf("%s",str);
	int ret = fwrite(str,8,1,fd);
	printf("\n Return value of ret : %d \n",ret);
	return 0;
}
