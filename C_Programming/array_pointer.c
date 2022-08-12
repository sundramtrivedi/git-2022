#include <stdio.h>
void array_num(int *num)
{
	int arr[100];
	printf("\n Enter %d number of elements in the array :\n",(*num));
	for(int i=0;i<(*num);i++)
	{
		printf("\n Enter the array arr[%d] : ",i);
		scanf("%d",arr+i);
	}
	printf("\n The array you entered are : \n");
	for(int i=0;i<(*num);i++)
	{
		printf("\n arr[%d] : %d \n",i,*(arr+i));
	}
}
int main()
{
	int arr[100];
	int i;
	int num;    
	printf("\n Enter the value of num : ");
	scanf("%d",&num);
	array_num(&num);
	return 0;
}
