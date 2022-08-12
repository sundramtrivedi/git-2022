#!/bin/bash
greatest()
{
    if [ $num1 -gt $num2 ] && [ $num1 -gt  $num3 ]
    then
         echo "$num1 is greater"
    elif [ $num2 -gt $num3 ]
    then 
        echo "$num2 is greater"
        else
            echo "$num3 is greater"
    fi
}
read -p "Enter num1 :" num1
read -p "Enter num2 :" num2
read -p "Enter num3 :" num3
greatest $num1 $num2 $num3
         
    