#!/bin/bash
function substract
{
	return $(($1-$2))
}
function multiplication
{
	let mult=`expr $1 \* $2`
	return $mult
}
read -p "Enter the First number : " number1
read -p "Enter the Second number : " number2
substract $number1 $number2
echo $?
multiplication $number1 $number2
result=$?
echo "$number1 * $number2 = $result"
