#!/bin/bash
read -p "Enter student name : " name
read -p "Enter branch name : " branch
read -p "Enter student age : " age
read -p "Enter salary : " salary
if [[ $name == "Sundar" && $branch == "iot" ]]
then
echo "You are part of orgz"
else
echo "You are not part of orgz"
fi
if [[ $salary = 123 && $age = 15 ]]
then
echo "You are no more student but employee"
else
echo "You are still student"
fi
