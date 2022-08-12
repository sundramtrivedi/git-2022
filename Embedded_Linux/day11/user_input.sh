#!/bin/bash
read -p "Enter the name of student :" name
read -p "Enter the prn of student :" prn
read -p "Enter the branch name of student :" branch_name
read -p "Enter the age of student :" age
read -p "Enter the salary of student :" salary

	if [ $name == "payal" ]
	then
		if [ $prn == 22 ]
		then
			if [ $branch_name == "iot" ]
			then
				echo "You are part of this Organization"
			fi
		fi
	else
		echo "You are not allowed to enter"
	fi

	if [ $age == 23 ]
	then
		if [ $salary == 100 ]
		then
			echo "You are no more student but employee"
		fi
	else
		echo "you are still student"
	fi



	if [[ $name == "payal" && $prn == 22 && $branch_name == "iot" ]]
	then
		echo "you are part of this Organization"
	else
		echo "you are not allowed to enter"
	fi
	if [[ $age == 23 && $salary == 100 ]]
	then
		echo "You are no more student but employee"
	else
		echo "You are still student"
	fi
