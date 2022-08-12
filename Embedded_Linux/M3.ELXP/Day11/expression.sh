#!/bin/bash
read -p "Enter num1 :" num1
read -p "Enter num1 :" num2
sum=`expr $num1 + $num2` #expr work as a mathmatic expression
echo "sum of $num1 + $num2 is : $sum"