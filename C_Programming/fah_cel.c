#include<stdio.h>
float input()
{
	float fah;
	printf("\n Enter the Fahrenheit temp : ");
	scanf("%f",&fah);
	return fah;
}
float cel(float fah)
{
	return ((fah-32) * 5) / 9;
}
int main()
{
	float temp;
	temp = input();
	float c = cel(temp);
	printf("\n Celcius : %f \n",c);
	return 0;
}
