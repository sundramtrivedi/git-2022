#!/bin/bash
read -p "Enter your name :" name
read -p "Enter your age :" age
read -sp "Enter your password :" password
echo "your name is $name and you are $age years"

<<com
What if no variable is supplied to read function
com
read -p "What is your current location :"
# read by default saves the value inside $REPLY variable if no variable name is supplied
echo "your current location found : $REPLY"
