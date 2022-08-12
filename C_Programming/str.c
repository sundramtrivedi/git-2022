#include<stdio.h>
int main()
{
	struct A
	{
		int x;
		char *str; // (or) char str[20];
	};
	struct A a1 = { 101, 'abc' } , a2;
	a1.x=10;
	a1.str='hello'; //works?
	scanf("\n %d \n %s \n",&a1.x,a1.str); //works?
	a2 = a1; //shallow copy or deep copy?
	return 0;
}
