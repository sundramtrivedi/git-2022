#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct iot_device_data
{
	int deviceID;
	char device_name[100];
	char device_type[100];
	float voltage;
};
typedef struct iot_home_data
{
	int homeID;
	char homeOwner[100];
	char address[100];
	struct iot_device_data device[2];
}home;
void input(home *h, int *num_home, int *num_device)
{
	printf("\n Enter the Home ID : ");
	scanf("%d",&h[(*num_home)].homeID);
	printf("\n Enter the name of Home Owner : ");
	scanf("%s",h[(*num_home)].homeOwner);
	printf("\n Enter the address of Home : ");
	scanf("%s",h[(*num_home)].address);
	printf("\n Enter the no of device you want to enter :");
	scanf("%d",num_device);
	if(*num_device<2)
	{
		for(int i=0;i<(*num_device);i++)
		{
			printf("Enter device details of %d devices: ",i+1);
			printf("\n Enter Device ID : ");
			scanf("%d",&h[*(num_home)].device[i].deviceID);
			printf("\n Enter Device Name :");
			scanf("%s",h[*(num_home)].device[i].device_name);
			printf("\n Enter Device Type :");
			scanf("%s",h[*(num_home)].device[i].device_type);
			printf("\n Enter Device Voltage :");
			scanf("%f",&h[*(num_home)].device[i].voltage);
		}
	}
	else
	{
		printf("\n Sorry you can connect only 2 devices. ");
	}
	(*num_home)++;
}
void display(home *h, int *num_home, int *num_device)
{
	for(int i=0;i<(*num_home);i++)
	{
		printf("\n  %d | %s | %s \n",h[i].homeID,h[i].homeOwner,h[i].address);
	
	for(int j=0;j<(*num_device);j++)
	{
		printf("\n  %d | %s | %s | %f \n",h[i].device[j].deviceID,h[i].device[j].device_name,h[i].device[j].device_type,h[i].device[j].voltage);
	}
	}
}
void search_by_homeOwner(home *h, int *num_home, int *num_device)
{
	char str[100];
	printf("\n Enter the Home Owner name you want to search :");
	scanf("%s",str);
	for(int i=0;i<(*num_home);i++)
	{
		if(strcmp(str, h[i].homeOwner)==0)
		{
			printf("\n %d | %s | %s \n",h[i].homeID,h[i].homeOwner,h[i].address);
		}
	}
}
void search_by_deviceName(home *h, int *num_home, int *num_device)
{
	char str[100];
	printf("\n Enter the Device Name you want to search :");
	scanf("%s",str);
	for(int i=0;i<(*num_home);i++)
	{
		for(int j=0;j<(*num_device);j++)
		{
			if(strcmp(str, h[i].device[j].device_name)==0)
			{
				printf("\n  %d | %s | %s | %f \n",h[i].device[j].deviceID,h[i].device[j].device_name,h[i].device[j].device_type,h[i].device[j].voltage);
			}
		}
	}
}
void change_device_name(home *h, int *num_home, int *num_device)
{
	char str[100];
	printf("\n Enter the Device Name you want to search :");
	scanf("%s",str);
	for(int i=0;i<(*num_home);i++)
	{
		for(int j=0;j<(*num_device);j++)
		{
			if(strcmp(str, h[i].device[j].device_name)==0)
			{
				printf("\n  %d | %s | %s | %f \n",h[i].device[j].deviceID,h[i].device[j].device_name,h[i].device[j].device_type,h[i].device[j].voltage);
				printf("\n Enter the New Device Name : \n");
				scanf("%s",h[i].device[j].device_name);
				printf("\n  %d | %s | %s | %f \n",h[i].device[j].deviceID,h[i].device[j].device_name,h[i].device[j].device_type,h[i].device[j].voltage);
				
			}
		}
	}
}
int main_menu_choice(){
	int ch =0;
	printf("\n");
	printf("[1] Add New Home \n");
	printf("[2] Display Home \n");
	printf("[3] Search Home by Home Owner \n");
	printf("[4] Search Device by Device Name \n");
	printf("[5] Change Device Name \n");
	printf("[6] Exit\n");
	printf("Enter choice : ");
	scanf("%d",&ch);
	printf("\n");
	return ch;
}
int main()
{
	home *h = calloc(sizeof(home),100);
	int num_home=0;
	int num_device=0;
	int ch=0;
	do{
		ch = main_menu_choice();
		if(ch == 1)
		{
			input(h,&num_home,&num_device);
		}
		else if (ch == 2)
		{
			display(h,&num_home,&num_device);
		}
		else if (ch == 3)
		{
			search_by_homeOwner(h,&num_home,&num_device);
		}
		else if (ch == 4)
		{
			search_by_deviceName(h,&num_home,&num_device);
		}
		else if (ch == 5)
		{
			change_device_name(h,&num_home,&num_device);
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
