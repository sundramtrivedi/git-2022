#include<stdio.h>
int input()
{
	int num;
	printf("\n Enter the value of num : ");
	scanf("%d",&num);
	return num;
}
void half_pyramid(int num)
{
	int i=0;
	int j=0;
	for(i=0;i<=num;i++)
	{
		for(j=1;j<=i;j++)
		{
			printf("*");
		}
		printf("\n");
	}
}
void inverted_half_pyramid(int num)
{
	int i=0;
	int j=0;
	for(i=0;i<num;i++)
	{
		for(j=num;j>i;j--)
		{
			printf("*");
		}
		printf("\n");
	}
}
void hollow_inverted_half_pyramid(int num)
{
	int i=0;
	int j=0;
	for(i=0;i<=num;++i)
	{        
		for(j=i;j<=num;++j)        
		{
			if((i==0)||(j==i)||(j==num))            
			{           
				printf("*");
			}
			else
			{
				printf(" ");
			}
		}
		printf("\n");
	}
}
void full_pyramid(int num)
{
	int i=0;
	int j=0;
	int k=0;
	for(i=0;i<=num;i++)
	{
		for(j=i;j<num;j++)
		{
			printf(" ");
		}
		for (k=1;k<=(2*i-1);k++)  
        	{  
            		printf("*"); 
        	} 
		printf("\n");
	}
}
void inverted_full_pyramid(int num)
{
	int i=0;
	int j=0;
	int k=0;
	for(i=num;i>=1;i--) 
	{
		for(j=0;j<=num-i;j++ ) 
		{
			printf(" ");    	
		}
		k = 0;
		while(k != (2*i-1))
		{
			printf("*"); 
			k++;
		}
		printf("\n");
	}
}
void hollow_full_pyramid(int num)
{
	int i=0;
	int j=0;
	int k=0;
	for(i=1;i<=num;i++)
	{
		for(j=i;j<num;j++)
		{
		    printf(" ");
		}
		for(j=1;j<=(2*i-1);j++)
		{
			if(i==num || j==1 || j==(2*i-1))
			{
				printf("*");
			}
			else
			{
				printf(" ");
			}
		}
		printf("\n");
	    }
}
void solid_diamond(int num)
{
	int i=0;
	int j=0;
	int k=0;
	for(i=1;i<=num;i++)
	{
		for(j=i;j<=num;j++)
		{
			printf(" ");
		}
		for(k=1;k<=(2*i-1);k++)
		{
			printf("*");
		}
		printf("\n");
	}
	for(i=num-1;i>=1;i--)
	{
		for(j=num;j>=i;j--)
		{
			printf(" ");
		}
		for(k=1;k<=(2*i-1);k++)
		{	
			printf("*");
		}       
		printf("\n");
	}
}
void hollow_diamond(int num)
{
	int i=0;
	int j=0;
	int k=0;
	for(i=1;i<=num;i++)
	{
		for(j=i;j<=num;j++)
		{
			printf(" ");
		}
		for(k=1;k<=(2*i-1);k++)
		{
			if(k==1 || k==(2*i-1))
			{
				printf("*");
			}
			else 
			{
				printf(" ");
			}     
		}
		printf("\n");
	}
	for(i=num-1;i>=1;i--)
	{
		for(j=num;j>=i;j--)
		{
			printf(" ");
		}
		for(k=1;k<=(2*i-1);k++)
		{	
			if(k==1 || k==2*i-1) 	
			{
				printf("*");
			}       
			else 
			{
				printf(" ");
			}
     		}
		printf("\n");
	}
}
void solid_half_diamond(int num)
{
	int i=0;
	int j=0;
	int star;
	for(i=1;i<num*2;i++)
	{
		if(i < num) 
		{
			star = i;
		}
    		else 
		{
			star = (2*num-i);
		}
    		for(j=1;j<=star;j++)
    		{
			printf("*"); 
		}
    		printf("\n"); 
	}
}
int main()
{
	int a = input();
	half_pyramid(a);
	printf("\n");
	printf("\n");
	inverted_half_pyramid(a);
	printf("\n");
	printf("\n");
	hollow_inverted_half_pyramid(a);
	printf("\n");
	printf("\n");
	full_pyramid(a);
	printf("\n");
	printf("\n");
	inverted_full_pyramid(a);
	printf("\n");
	printf("\n");
	hollow_full_pyramid(a);
	printf("\n");
	printf("\n");
	solid_diamond(a);
	printf("\n");
	printf("\n");	
	hollow_diamond(a);
	printf("\n");
	printf("\n");
	solid_half_diamond(a);
	printf("\n");
	printf("\n");
	return 0;
}
