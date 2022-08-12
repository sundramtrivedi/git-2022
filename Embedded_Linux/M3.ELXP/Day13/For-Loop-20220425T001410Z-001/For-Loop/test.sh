#!/bin/bash
multiplcation()
{
    mulres=`expr $1 \* $2`
    echo $mulres                
}
# take input from the user
read -p "Enter first number : "  number1
read -p "Enter second number : " number2


#call the function 1 and store the value in variable retval
retval=`multiplcation $number1 $number2`
echo $retval
