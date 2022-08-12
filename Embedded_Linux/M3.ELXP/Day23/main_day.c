#include<stdio.h>
#include<day.h>

int main()
{
    int num1;
    printf("Enter Number=");
    scanf("%d",&num1);
    switch(num1)
    {
        case 1:
           mon(num1);
           break;
        case 2:   
            tue(num1);  
            break;
       default:
            printf("select 1 or 2");
        
    }
    return 0;
}