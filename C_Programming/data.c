#include<stdio.h>
int main()
{
	FILE *d = fopen("data.txt","r+");
	int prn;
	char name[100];
	int day;
	int month;
	int year;
	printf("\n Enter the PRN :");
	scanf("%d",&prn);
	printf("\n Enter the Name :");
	scanf("%s",name);
	printf("\n Enter the Day of Birthdate :");
	scanf("%d",&day);
	printf("\n Enter the Month of Birthdate :");
	scanf("%d",&month);
	printf("\n Enter the Year of Birthdate :");
	scanf("%d",&year);
	fprintf(d,"\n %d | %s | %d.%d.%d \n",prn,name,day,month,year);
	return 0;
}
