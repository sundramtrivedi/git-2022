#include <stdio.h>
void binary_octal(long int *num)
{
	long int octalnum = 0;
	long int i = 1; 
	long int rem;
	while ((*num) != 0)
	{
		rem = (*num) % 10;
		octalnum = octalnum + (rem * i);
		i = i * 2;
		(*num) = (*num) / 10;
	}
	printf("\n Equivalent octal value: %lo \n", octalnum);
}
int main()
{
	long int num;
	long int octalnum = 0;
	long int i = 1; 
	long int rem;
	printf("Enter the value for  binary number: ");
	scanf("%ld", &num);
	binary_octal(&num);
	return 0;
}
