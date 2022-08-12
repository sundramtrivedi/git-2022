#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>
int main(int argc, char *argv[])
{
	pid_t payal;
	printf("--> Hello Payal I am in -->");
	if(fork() && fork())
	{
		payal = fork();
	}
	printf("\n --> Hello --> \n");
}
