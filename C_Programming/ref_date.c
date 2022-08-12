#include<stdio.h>
int dayFromDate(int date,int month,int year)
{
	int magic[] = {0,3,2,5,0,3,5,1,4,6,2,4};
	year -= month<3;
	return (year + year / 4 - year / 100 + year / 400 + magic [month-1] + date) % 7;
}
int main()
{
	int date;
	int month;
	int year;
	printf("\n Enter the Day of date : \n");
	scanf("%d",&date);
	printf("\n Enter the Month of date : \n");
	scanf("%d",&month);
	printf("\n Enter the Year of date : \n");
	scanf("%d",&year);
	int day = dayFromDate(date,month,year);
	if(day == 0)
	{
		printf("\n Sunday \n");
	}
	else if(day == 1)
	{
		printf("\n Monday \n");
	}
	else if(day == 2)
	{
		printf("\n Tuesday \n");
	}
	else if(day == 3)
	{
		printf("\n Wednesday \n");
	}
	else if(day == 4)
	{
		printf("\n Thursday \n");
	}
	else if(day == 5)
	{
		printf("\n Friday \n");
	}
	else 
	{
		printf("\n Saturday \n");
	}
	return 0;
}
