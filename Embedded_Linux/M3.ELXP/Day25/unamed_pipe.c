#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/wait.h>
#define MAX_MSG_SIZE 100
char *msg1 = "Pipes are used for one way communication";
char *msg2 = "First need to write data in buffer";
char *msg3 = "Then read data from buffer";

char buffer[MAX_MSG_SIZE];
int p[2],nbytes;
int main()
{   
    pid_t pid;
    int ret = pipe(p);//pipe created
    if(ret == -1 )
    {
        perror("Pipe not created\n");
        exit(1);
    }
    pid=fork();
    if(pid < 0)
    {

            perror("Child process not created\n");
    }
    else if(pid > 0)
    {
        close(p[0]);
        write(p[1],msg1,MAX_MSG_SIZE);
        write(p[1],msg2,MAX_MSG_SIZE);
        write(p[1],msg3,MAX_MSG_SIZE);
        close(p[1]);
        wait(NULL);//till child process ends
    }
    else
    {
        close(p[1]);
        while((nbytes = read(p[0],buffer,MAX_MSG_SIZE)) > 0)//read from buffer and print nbytes stores no of bytes read from buffer
        {
            printf("%s\n",buffer);
            printf("%d\n",nbytes);
        }
            close(p[0]);
    }
         printf("Finshed reading\n");
         return 0;
}