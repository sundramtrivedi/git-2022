#!/bin/bash
greatest()
{
	if [ $1 -gt $2 ] && [ $1 -gt $3 ]
	then
		echo $1
	elif [ $2 -gt $3 ]
	then
		echo $2
	else
		echo $3
	fi
}
read -p "Enter the number 1 : " num1
read -p "Enter the number 2 : " num2
read -p "Enter the number 3 : " num3
result_greatest=`greatest $num1 $num2 $num3`
echo "The greatest number : " $result_greatest
