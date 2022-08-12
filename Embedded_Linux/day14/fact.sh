#!/bin/bash
factorial()
{
	let fact=1
	let num=$1
	for (( count=1;count<=$num;count++ ))
	{
		fact=$(( $count * $fact))
	}
	echo $fact
}
read -p "Enter the number : " num1
result_fact=`factorial $num1`
echo "Factorial : " $result_fact
