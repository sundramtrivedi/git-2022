#include<pthread.h>
#include<stdio.h>
#include<unistd.h>
#include"routin1.h"
#include"routin2.h"
int main(int argc, char* argv[])
{
	pthread_t t1;
	pthread_t t2;
	 
	//thread creation
	pthread_create(&t1,NULL,routine1,NULL);
	pthread_join(t1,NULL);
	pthread_create(&t2,NULL,routine2,NULL);
	pthread_join(t2,NULL);
	//system("echo $PWD");
	//system("echo $$");
	//system("echo $HOME");
	//system("ps -a | grep a.out");
	//system("ps -T -p");
}
