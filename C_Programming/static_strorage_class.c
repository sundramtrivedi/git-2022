#include<stdio.h>
static int b; // global static variable // on data segment
void process_data()
{
	//	printf("\n Value of a = %d \n",a); // can not accesss local static variable outside of function
	//	printf("\n Address of a = %x \n",&a);
	//	printf("\n Size of a = %d \n",sizeof(a));
	
	printf("\n Value of b = %d \n",b);
	printf("\n Address of b = %x \n",&b);		
	printf("\n Size of b = %d \n",sizeof(b));
}
void process()
{
	// int x = 10; // on stack
	static int x = 10; // on data segment
	x++;
	printf("\n Value of x = %d \n",x);
}
int main()
{
	static int a = 10; // local static variable // on data segment
	//	printf("\n Value of a = %d \n",a);
	//	printf("\n Address of a = %x \n",&a);
	//	printf("\n Size of a = %d \n",sizeof(a));
	//	process_data();
	process();
	process();
	process();
	return 0;
}
