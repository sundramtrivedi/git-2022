#!/bin/bash
multiplication()
{
	mulres=`expr $1 \* $2`
	echo $mulres
}
division()
{
	divres=`expr $1 \/ $2`
	echo $divres
}
read -p "Enter the first number : " number1
read -p "Enter the second number : " number2
result_mul=`multiplication $number1 $number2`
result_div=`division $number1 $number2`
echo "Multiplication : " $result_mul
echo "Division : " $result_div
