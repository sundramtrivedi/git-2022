#include<stdio.h>
#include<unistd.h>
int main(int argc,char* argv[])
{
    for(int count = 0; count<10; count++)
    {
        printf("Basic Process Creation in c\n");
        sleep(5);//blocking for every 1o sec process goes into blocking state and then goes to read and then again to runningq
       
    }
    return  0;
}

