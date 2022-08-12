#include<stdio.h>
typedef struct Employee
{
	int empID;
	char name[100];
	int salary;
	int (*tax)(int);
}employee;
int get_tax(int sal)
{
	return (0.10 * salary);
}
employee* create object()
{
	employee *temp = malloc(sizeof(employee));
	temp->tax = &get_tax;
	return temp;
}
int main()
{
	employee e1 = {1,"sid",1000,&get_tax};
	employee e2;
	e2.tax = &get_tax;
	employee *emp = create_object();
	float a = get_tax(salary);
	printf("\n get_tax : %f \n",a);
	return 0;
}
