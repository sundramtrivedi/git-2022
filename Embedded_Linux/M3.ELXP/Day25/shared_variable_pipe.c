//Interprocess Communication
#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/wait.h>
int shared_val=4;//global variable to be shared in two processes
int main()
{   
    int buffer;
    int p[2];//always must be p[2] is even as pipe need to read and write p[0]-> for read and p[1]-> write
    pid_t pid;//process created
    int ret = pipe(p);//pipe created
    if(ret == -1 )//if pipe is not created then below will be printed and when created 0 will be returned  
    {
        perror("Pipe not created\n");
        exit(1);
    }
    pid = fork();//creates child and parent process
    if(pid < 0)
    {

            perror("Child process not created\n");
    }
    else if(pid == 0)
    {
        close(p[0]);//here below we are writing so we need too close read as pipe has one way communication
        int wbytes = write(p[1],&shared_val,sizeof(shared_val));//shared_val value is stored in p[1] process 
        printf("no of bytes written=%d\n",wbytes);
        close(p[1]);
        
    }
    else
    {
        wait(NULL);//till child process ends
        close(p[1]);//here below we are redaing so we need too close write as pipe has one way communication
        while((read(p[0],&buffer,sizeof(buffer))) > 0)//and due to pipe p[1] value is give as input to p[0] process 
        //so here value read from p[0] is stored in buffer variable
        {
            printf("Vlaue passed by process p1=%d\n",buffer);
        }
        buffer=buffer+2;
        shared_val=buffer;
        printf("Value processed by process p2=%d\n",shared_val);
        close(p[0]);
    }
         printf("Finshed reading\n");
         return 0;
}