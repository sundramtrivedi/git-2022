#include<stdio.h>
extern int data; // don't declare data variable its already declare
int main()
{
	printf("\n Value of data : %d \n",data);
	printf("\n Value of &data : %d \n",&data);
	printf("\n Value of sizeof(data) : %d \n",sizeof(data));
	return 0;
}
