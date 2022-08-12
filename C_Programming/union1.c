#include<stdio.h>
int main()
{
	union A
	{
		int x;
		float y;
		double z;
		int arr[2];
	}a1;
	a1.y=6.25f;
	printf("\n x = %x \n",a1.x);
	a1.z=0.15625;;
	printf("\n a1.arr[1] = %x \n\n a1.arr[0] = %x\n",a1.arr[1],a1.arr[0]);	
	return 0;
}
