#include<stdio.h>
#include<stddef.h>
int main()
{
	union A
	{
		int x;
		int y;
		char ch;
	};
	union A a1;
	printf("\n sizeof(a1) -> %d \n",sizeof(a1));
	
	a1.x = 10;
	printf("\n a1.x = %d \n",a1.x); //10
	printf("\n a1.y = %d \n",a1.y); //10
	printf("\n a1.ch = %d \n",a1.ch); //10
	
	a1.ch = 'A';
	printf("\n a1.x = %d \n",a1.x); //10
	printf("\n a1.y = %d \n",a1.y);
	printf("\n a1.ch = %d \n",a1.ch);
	
	a1.x = 0xfff;
	printf("\n a1.x = %d \n",a1.x);
	printf("\n a1.y = %d \n",a1.y);
	printf("\n a1.ch = %d \n",a1.ch);
	
	a1.ch = 0x1a;
	printf("\n a1.x = %d \n",a1.x);
	printf("\n a1.y = %d \n",a1.y);
	printf("\n a1.ch = %d \n",a1.ch);
	
	printf("\n Address of a1.x = %d \n",&a1.x);
	printf("\n Address of a1.y = %d \n",&a1.y);
	printf("\n Address of a1.ch = %d \n",&a1.ch);
	
	int b = offsetof(union A,x);
	printf("\n offset : %x \n",b);
	return 0;
}
