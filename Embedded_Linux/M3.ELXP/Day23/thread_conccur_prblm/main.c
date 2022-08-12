#include<pthread.h>
#include<stdio.h>
#include<unistd.h>
#include"routiune.h"
//#include"routin2.h"

int countval=0;//critical section 
pthread_mutex_t mutex;
void* routine1(void *msg)
{
    for(int i =0; i<100000; i++)
    {
        pthread_mutex_lock(&mutex);
        countval++;
        pthread_mutex_unlock(&mutex);
    }
}

int main(int argc, char* argv[])
{
    pthread_t t1;
    pthread_t t2;
    pthread_mutex_init(&mutex,NULL);//mutex initialisation
    //thread creation
    if(pthread_create(&t1,NULL,routine1,NULL)!=0)
    {
        return 10;
    }
    if(pthread_create(&t2,NULL,routine1,NULL)!=0)
    {
        return 20;
    }
    if(pthread_join(t1,NULL)!=0)
    {
        return 30;
    }
    if(pthread_join(t2,NULL)!=0)
    {
        return 40;
    }
    pthread_mutex_destroy(&mutex);
    printf("loop executed for %d times\n",countval);
    return 0;
}

