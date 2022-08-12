#!/bin/bash
read -p "Enter the number :" number
if [ $number -lt 0 ];
then
	echo "Number is negative"
elif [ $number -gt 0 ];
then
	echo "Number is positive"
else
	echo "Number is neither positive nor negative"
fi
