#include<stdio.h>
float input1()
{
	float p;
	printf("\n Enter the principal :");
	scanf("%f",&p);
	return p;
}
float input2()
{
	float t;
	printf("\n Enter the time :");
	scanf("%f",&t);
	return t;
}
float input3()
{
	float r;
	printf("\n Enter the rate per year :");
	scanf("%f",&r);
	return r;
}
float s_interest(float p, float t, float r)
{
	return (p*t*r)/100;
}
int main()
{
	float a = input1();
	float b = input2();
	float c = input3();
	float d= s_interest(a,b,c);
	printf("\n Simple Interest : %f \n",d);
	return 0;
}
