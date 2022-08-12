#!/bin/bash
read -p "Enter the number 1 :" num1
read -p "Enter the number 2 :" num2
sum=`expr $num1 + $num2`
echo "$num1 + $num2 = $sum"
