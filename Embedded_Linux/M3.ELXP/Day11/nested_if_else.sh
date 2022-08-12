#!/bin/bash
read -p "Enter name: " name
if [ $name == "Ganesh" ]
then
    echo "Your $name is in the list"
    read -p "Enter your PRN:" prn 
    if [ $prn -eq 123 ]
    then
        echo " Your prn $prn is verified can take exam in 15 min"
    fi
else
    echo "You cannot take exam"
fi


