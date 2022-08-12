#!/bin/bash
mod()
{
    modres=`expr $1 % $2`
    return $modres

}
#usetr input
read -p "Enter num1 :" num1
read -p "Enter num2 :" num2

#function call
mod $num1 $num2
echo $?