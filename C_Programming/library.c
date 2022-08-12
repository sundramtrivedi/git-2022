#include<stdio.h>
typedef struct library
{
	int bookID;
	char bookName[100];
	int ISBN;
	char author[100];
}lib;
void input(lib *l, int *num_lib)
{
	printf("\n Enter the bookID : ");
	scanf("%d",&l[(*num_lib)].bookID);
	printf("\n Enter the bookName : ");
	scanf("%s",l[(*num_lib)].bookName);
	printf("\n Enter the ISBN : ");
	scanf("%d",&l[(*num_lib)].ISBN);
	printf("\n Enter the author : ");
	scanf("%s",l[(*num_lib)].author);
	++(*num_lib);
}
void display(lib *l, int *num_lib)
{
	for(int i=0;i<(*num_lib);i++)
	{
		printf("\n %d | %s | %d | %s \n",l[i].bookID,l[i].bookName,l[i].ISBN,l[i].author);
	}
}
void search(lib *l, int *num_lib)
{
	int id=0;
	printf("\n Enter the ISBN number to search book :");
	scanf("%d",&id);
	for(int i=0;i<(*num_lib);i++)
	{
		if(id==l[i].ISBN)
		{
			printf("\n %d | %s | %d | %s \n",l[i].bookID,l[i].bookName,l[i].ISBN,l[i].author);
		}
	}
}
void change_name(lib *l, int *num_lib)
{
	int id=0;
	printf("\n Enter the ISBN for change the name of book :");
	scanf("%d",&id);
	for(int i=0;i<(*num_lib);i++)
	{
		if(id==l[i].ISBN)
		{
			printf("\n %d | %s | %d | %s \n",l[i].bookID,l[i].bookName,l[i].ISBN,l[i].author);
			printf("\n Enter the new book name : ");
			scanf("%s",l[i].bookName);
			printf("\n %d | %s | %d | %s \n",l[i].bookID,l[i].bookName,l[i].ISBN,l[i].author);
		}
	}
}
void delete(lib *l, int *num_lib)
{
	
}
int menu_choice(){
	int ch =0;
	printf("\n");
	printf("[1] Add Book \n");
	printf("[2] Display Book \n");
	printf("[3] Search Book (by ISBN) \n");
	printf("[4] Change name of given book (by ISBN) \n");
	printf("[5] Delete the data (by ISBN) \n");
	printf("[6] Exit\n");
	printf("Enter choice : ");
	scanf("%d",&ch);
	printf("\n");
	return ch;
}
int main()
{
	lib l[100];
	int num_lib=0;
	int ch=0;
	do{
		ch = menu_choice();
		if(ch == 1)
		{
			input(l,&num_lib);
		}
		else if (ch == 2)
		{
			display(l,&num_lib);
		}
		else if (ch == 3)
		{
			search(l,&num_lib);
		}
		else if (ch == 4)
		{
			change_name(l,&num_lib);
		}
		else if (ch == 5)
		{
			delete(l,&num_lib);
		}
		else if (ch == 6)
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
