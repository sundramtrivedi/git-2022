#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>
#include<stdlib.h>
int main(int argc, char* argv[])
{
	pid_t ret;
	int final_value=0;
	ret = fork();
	if(ret == 0)//fork return 0 for child process
	{
	//Child Process Block
		 for(int i=0;i<=100;i++)
		 {
		     printf("Child count = %d\n",i);
		     final_value -= 1; 
		 }
	  exit(0);
	}
	else if(ret > 0)//fork return 1 for parent process
	{
	//Parent Process Block
		for(int j=0;j<=100;j++)
		{
			printf("Parent count = %d\n",j);
			final_value += 1; 
		}
	}
	else
	{
		printf("Failed to create child process\n");
	}

	printf("Final value is = %d\n",final_value);
	return 0;
}
 
