#!/bin/bash
read -p "Enter the num: " num1
if [[ $num1 -lt 0 ]]    
then
    echo "$num1 is -ve"
elif [ $num1 -gt 0 ]
then
    echo "$num1 is +ve"
else
    echo "Number is neither +ve nor -ve"
fi

#check if string is empty
string="abcd"
string1=''
if [[ -z $string ]]#-z will give if string is empty or not
then
    echo "string is empty"
else
    echo "string is not empty"
fi


