#include<stdio.h>
struct date
{
	int day;
	int month;
	int year;
};
struct address
{
	int flat_no;
	char city[100];
	char state[100];
};
struct employee
{
	char name[100];
	int EMPID;
	struct date dob;
	struct address add;
};
void input(struct employee *em, int *num_em)
{
	printf("\n Enter the name of Employee : ");
	scanf("%s",em[(*num_em)].name);
	printf("\n Enter the Employee ID : ");
	scanf("%d",&em[(*num_em)].EMPID);
	printf("\n Enter the day of DOB : ");
	scanf("%d",&em[(*num_em)].dob.day);
	printf("\n Enter the month of DOB : ");
	scanf("%d",&em[(*num_em)].dob.month);
	printf("\n Enter the year of DOB : ");
	scanf("%d",&em[(*num_em)].dob.year);
	printf("\n Enter the flat number of your address : ");
	scanf("%d",&em[(*num_em)].add.flat_no);
	printf("\n Enter the city of your address : ");
	scanf("%s",em[(*num_em)].add.city);
	printf("\n Enter the state of your address : ");
	scanf("%s",em[(*num_em)].add.state);
	++(*num_em);
}
void display(struct employee *em, int *num_em)
{
	for(int i=0;i<(*num_em);i++)
	{
		printf("\n %d | %s | %d | %d/%d/%d | %d | %s | %s \n",i,em[i].name,em[i].EMPID,em[i].dob.day,em[i].dob.month,
		em[i].dob.year,em[i].add.flat_no,em[i].add.city,em[i].add.state);
	}
}
void search(struct employee *em, int *num_em)
{
	int id=0;
	printf("\n Enter the EMPID you want to search : ");
	scanf("%d",&id);
	for(int i=0;i<(*num_em);i++)
	{
		if(id==em[i].EMPID)
		{
			printf("\n %d | %s | %d | %d/%d/%d | %d | %s | %s \n",i,em[i].name,em[i].EMPID,em[i].dob.day,em[i].dob.month,
		em[i].dob.year,em[i].add.flat_no,em[i].add.city,em[i].add.state);
		}
	}
}
void change_name(struct employee *em, int *num_em)
{
	int id=0;
	printf("\n Enter the EMPID of employee : ");
	scanf("%d",&id);
	for(int i=0;i<(*num_em);i++)
	{
		if(id==em[i].EMPID)
		{
			printf("\n %d | %s | %d | %d/%d/%d | %d | %s | %s \n",i,em[i].name,em[i].EMPID,em[i].dob.day,em[i].dob.month,
		em[i].dob.year,em[i].add.flat_no,em[i].add.city,em[i].add.state);
			printf("\n Enter the new Employee name :");
			scanf("%s",em[i].name);
			printf("\n %d | %s | %d | %d/%d/%d | %d | %s | %s \n",i,em[i].name,em[i].EMPID,em[i].dob.day,em[i].dob.month,
		em[i].dob.year,em[i].add.flat_no,em[i].add.city,em[i].add.state);
		}
	}
}
int menu_choice(){
	int ch =0;
	printf("\n");
	printf("[1] Add Employee \n");
	printf("[2] Display Employee Data \n");
	printf("[3] Search Employee by EMPID \n");
	printf("[4] Change name of given employee(by EMPID) \n");
	printf("[5] Exit\n");
	printf("Enter choice : ");
	scanf("%d",&ch);
	printf("\n");
	return ch;
}
int main()
{
	struct employee em[100];
	int num_em = 0;
	int ch=0;
	do{
		ch = menu_choice();
		if(ch == 1)
		{
			input(em,&num_em);
		}
		else if (ch == 2)
		{
			display(em,&num_em);
		}
		else if (ch == 3)
		{
			search(em,&num_em);
		}
		else if (ch == 4)
		{
			change_name(em,&num_em);
		}
		else if (ch == 5)
		{
			break;
		}
		else 
		{
			printf("Wrong Choice");
		}		
	}while(1);
	return 0;
}
