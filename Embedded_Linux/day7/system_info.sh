#!/bin/bash
# how to declare a variable
# variable_name=value (without space)

<<COMMENT

system_hostname=`uname -n`
system_kernel_version=`uname -v`
system_kernel_name=`uname -s`
system_all=`uname -a`
echo "Your System Name :"$system_hostname
echo "Your Kernel Version :"$system_kernel_version
echo "Your Kernel Name :"$system_kernel_name 
echo "Your All Info :"$system_all 

# this is another way to write comment
read -p "Enter your name : " name
read -p "Enter your age : " age 
echo "Hello !! Miss. $name Welcome to the world of IOT"
echo "Your age is $age , seems so young to learn shell scripting"

COMMENT

# this is another way to write comment
read -p "Enter the command : " command_user
echo "Hello !! Mr/Miss You have entered command <'$command_user'> and value returned by shell is <<`$command_user`>>"
