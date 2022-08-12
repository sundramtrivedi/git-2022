#include<stdio.h>
int main()
{
	// we don't need to mention auto
	auto int a = 10; // local variable // stack // scope only function // lifetime function
	printf("\n Value of a = %d \n",a);
	printf("\n Address of a = %x \n",&a);
	printf("\n Size of a = %d \n",sizeof(a));
	printf("\n ***************************************************** \n");
	register int b = 100;
	printf("\n Value of b = %d \n",b);
	//	printf("\n Address of b = %x \n",&b);		can not type compile time error
	printf("\n Size of b = %d \n",sizeof(b));
	printf("\n ***************************************************** \n");
	struct student 
	{
		int a;
		int b;
		int c;
	};
	register struct student s1;
	printf("\n Value of s1 = %d \n",s1);
	//	printf("\n Address of s1 = %x \n",&s1);		can not type compile time error
	printf("\n Size of s1 = %d \n",sizeof(s1));
	printf("\n ***************************************************** \n");
	register int arr[100];
	arr[0] = 100;
	//	printf("\n Value of &arr = %d \n",&arr);
	return 0;
}
