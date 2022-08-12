Notes
--> echo $SHELL
    /bin/bash   ----- shell name
Environment variable
--> There values are already defined in the system you just need to use it.
--> more system related
--> there are always written in the capital letter
echo - commands is used to print the values like printf in c.
# print the home directory name
--> echo $HOME 
whoami     #utility to print user name
hostname    
package manager #aptis a package manager
-----------------------------------------------------------------------------
--> ubuntu is debian based OS.
--> default package manager is apt.
--> helps to install packages from the remote debian repos.
More - https://helps.ubuntu.com/community/Repositories/CommandLine
# any package to install on the system must be done by sudo/root users
e.g - xournal software/application
--> sudo apt install xournal
--> sudo apt install xournal -y #exlicit yes
# update the system packages
--> sudo apt update
# will upgrade to latest packages
--> sudo apt-get upgrade
# delete/remove an exiting package
--> sudo apt purge <packagename> // apt-purge use -y while on servers
# run multiple commands at once
update the system and then install net-tools 
--> sudo apt update -y && sudo apt install net-tools -y 
Assignment :
1. Remove the package net-tools and install the package net-tools in one line.
2. Write a basic C program and compile and run in one line.
# print ip address
--> ifconfig    // net-tools or ifconfig -a  print all available interface
--> ip address
--> ip -a 
--> ip addr 
lo --> loop back 
--> 127.0.0.1 - is known as loopback address 
--> used for debug and test internal serices
--> interface name -lo 
other interfaces wlp5s0 --> for wireless name may be changes w- wireless
                 emp4s0 --> for ethernet name may be change 
#navigation based commands
cd --> to change directory => Change Directory
pwd --> to know directory path => Present Working Directory
Assignment :
1. redirect to home directory using cd and environment variable.
--> cd $HOME 
--> cd ~
--> cd /home/<username>
