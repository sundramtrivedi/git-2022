#include<stdio.h>
typedef struct data
	{
		int prn;
		char name[100];
		int day;
		int month;
		int year;
	}d;
int main()
{
	FILE *s = fopen("struct.txt","r+");
	d *ptr = calloc(sizeof(d),100);
	printf("\n Enter the PRN :");
	scanf("%d",&ptr->prn);
	printf("\n Enter the Name :");
	scanf("%s",ptr->name);
	printf("\n Enter the Day of Birthdate :");
	scanf("%d",&ptr->day);
	printf("\n Enter the Month of Birthdate :");
	scanf("%d",&ptr->month);
	printf("\n Enter the Year of Birthdate :");
	scanf("%d",&ptr->year);
	fprintf(s,"\n PRN : %d \n",ptr->prn);
	fprintf(s,"\n Name : %s \n",ptr->name);
	fprintf(s,"\n DOB : %d.%d.%d \n",ptr->day,ptr->month,ptr->year);
	return 0;
}
