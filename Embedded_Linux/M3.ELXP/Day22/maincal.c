#include <stdio.h>
#include "cal.h"
int main()
{
    int num1, num2;
    printf("Enter num1 : ");
    scanf("%d",&num1);
    printf("Enter num2 : ");
    scanf("%d",&num2);
    int res1 = add(num1, num2);
    int res2 = sub(num1, num2);
    printf("Add is : %d\n",res1);
    printf("Sub is : %d\n",res2);
    return 0;
}