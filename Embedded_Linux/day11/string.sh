#!/bin/bash
read -p "Enter the string 1 :" str1
read -p "Enter the string 2 :" str2
str="aabbaa"
str_1=''
	if [[ -z $str ]]
	then
		echo "String is empty"
	else
		echo "String is not empty"
	fi

	if [[ -n $str_1 ]]
	then
		echo "String is not empty"
	else
		echo "String is empty"
	fi

	if [[ $str1 == $str2 ]]
	then
		echo "Strings are same"
	else
		echo "Strings are not same"
	fi
