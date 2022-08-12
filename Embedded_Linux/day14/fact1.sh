#!/bin/bash
factorial()
{
	let fact=1
	let num=$1
	while [ $num -gt 0 ]
	do
		fact=`expr $num \* $fact`
		((num--))
	done
	echo $fact
}
read -p "Enter the number : " num1
result_fact=`factorial $num1`
echo "Factorial : " $result_fact
