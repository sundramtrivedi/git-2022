#include<stdio.h>
float area(float r)
{
	float a;
	a = 3.14 * r * r ;
	return a;

}
float circum(float r)
{
	float c;
	c = 2 * 3.14 * r;
	return c;
}
	
 int main()
{
	float r,a,c;
	printf("\n Enter the radius: \n");
	scanf("%f",&r);
	float pi = 3.14;
	float x = area(r);
	printf("\n area : %f",x);
	float y = circum(r);
	printf("\n circum : %f",y);

	return 0;
}
