#include<stdio.h>
int main()
{
	struct Student
	{
		int a;
		char b;
		int c;
		short d;
		long long int e;
	};
	struct Student s1;
	printf("\n sizeof Student : %d \n",sizeof(struct Student));
	printf("\n Address of a : %d \n",&s1.a);
	printf("\n Address of b : %d \n",&s1.b);
	printf("\n Address of c : %d \n",&s1.c);
	printf("\n Address of d : %d \n",&s1.d);
	printf("\n Address of e : %d \n",&s1.e);
	return 0;
}
