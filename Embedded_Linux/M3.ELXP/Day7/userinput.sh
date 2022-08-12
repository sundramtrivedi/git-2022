#!/bin/bash
'system_hostname=`uname -n`
echo "$system_hostname your hostname $system_hostname:-"$system_hostname
'
system_hostname=`uname -n`
read -p "Enter command :" cmd
read -p "Enter your name : " name
echo "Hello $name you have entered $cmd as command and value returned by shell is $system_hostname"


read -p:"Enter the command:" command
echo $command
echo `$command`