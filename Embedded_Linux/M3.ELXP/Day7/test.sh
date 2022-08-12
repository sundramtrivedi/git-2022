#!/bin/bash
#variable declaration for script
system_hostname=`uname -n`
system_kernel_version=`uname -v`
system_kernel_name=`uname -s`

#to print o/p on console
echo "Your hostname :-"$system_hostname
echo "Your Kernel version :-"$system_kernel_version
echo "Your Kernel name :-"$system_kernel_name