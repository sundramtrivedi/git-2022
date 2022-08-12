#include<stdio.h>
typedef struct student
{
	int prn;
	char name[100];
	int marks[4];
}stud;
void input(stud *s,int *num_stud)
{
	printf("Enter the PRN of student :");
	scanf("%d",&s[(*num_stud)].prn);
	printf("Enter the Name of student :");
	scanf("%s",s[(*num_stud)].name);
	for(int i = 0 ; i < 4 ; i++)
	{
		printf("Enter the Marks of Subject[%d] :",i+1);
		scanf("%d",&s[(*num_stud)].marks[i]);
	}
	++(*num_stud);
}
void display(stud *s,int *num_stud) 
{
	printf("\n PRN : %d \n",s->prn);
	printf("\n Name : %s \n",s->name);
	for(int i = 0 ; i < 4 ; i++)
	{
		printf("\n Subject[%d] : %d \n",i+1,s->marks[i]);
	}
}
void sum(stud *s,int *num_stud)
{
	int sum = 0;
	for(int i = 0 ; i < 4 ; i++)
	{
		sum += s->marks[i];
	}
	printf("\n Sum of all subjects = %d \n",sum);
}
void avg(stud *s,int *num_stud)
{
	int sum = 0;
	int avg = 0;
	for(int i = 0 ; i < 4 ; i++)
	{
		sum += s->marks[i];
		avg = sum / 4;
	}
	printf("\n Average of all marks = %d \n",avg);
}
int main()
{
	stud s[100];
	int num_stud = 0;
	input(s,&num_stud);
	display(s,&num_stud);
	sum(s,&num_stud);
	avg(s,&num_stud);
	return 0;
}
