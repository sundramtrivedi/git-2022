#include<stdio.h>
int main()
{
	const int a = 10;
	printf("\n Value of a = %d \n",a);
	// a = 100;	can not change constant variable
	printf("\n Value of a = %d \n",a);
	printf("\n ***************************************************** \n");
	int x = 100;
	const int *pt = &x;
	printf("\n Value of x = %d \n",x);
	printf("\n Value of x : pt = %d \n",pt);
	x = 12312;
	pt = 22222;
	printf("\n Value of x = %d \n",x);
	printf("\n Value of x : pt = %d \n",pt);
	printf("\n ***************************************************** \n");
	int * const p = &x;
	printf("\n Value of x = %d \n",x);
	printf("\n Value of x : pt = %d \n",p);
	*p = 123;
	//	p = 22222;	not possible because p memory is constant
	printf("\n Value of x = %d \n",x);
	printf("\n Value of x : pt = %d \n",p);
	printf("\n ***************************************************** \n");
	int const *s = &x;
	printf("\n Value of x = %d \n",x);
	printf("\n Value of x : pt = %d \n",s);
	//	*s = 123;	not possible dereference is constant
	s = 22222;	
	printf("\n Value of x = %d \n",x);
	printf("\n Value of x : pt = %d \n",s);
	printf("\n Value of x : (float *)s = %d \n",(float *)s);
	printf("\n Value of x : (float *)s = %f \n",(float *)s);
	return 0;
}
