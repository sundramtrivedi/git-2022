#!/bin/bash
read -p "Enter the name :" name
	if [ $name == payal ]
	then
		read -p "Enter the prn :" prn
		if [ $prn == 22 ]
		then
		echo "Embedded linux"
		fi
	fi

	if [ $name == me ]
	then
		read -p "Enter the prn :" prn
		if [ $prn == 06 ]
		then 
		echo "Python"
		fi
	fi

	if [ $name == you ]
	then
		read -p "Enter the prn :" prn
		if [ $prn == 13 ]
		then 
		echo "HTML and CSS"
		fi
	fi
