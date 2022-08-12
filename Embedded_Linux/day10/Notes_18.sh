#!/bin/bash
# -p --> prompt
# -s --> Do not echo keystrokes when read is taking input from the terminal
read -p "username :" uservar
read -sp "password :" userpass
echo  
echo "your username and password are "
echo "username :" $uservar
echo "password :" $userpass
-------------------------------------------------------------------------------------------------------------------------
#!/bin/sh
# echo will display the same msg. on monitor/console that is written inside the double quote
echo "List of the files/directory"
# listing of files/directory
ls -l 
-------------------------------------------------------------------------------------------------------------------------
#!/bin/bash
# Demo to install any package
echo "Installing net-tools"
# net-tools is a package that provides ifconfig utility
sudo apt install net-tools 
------------------------------------------------------------------------------------------------------------------------
#!/bin/bash
read -p "Name the package to install :" toInstall
echo "Removing the previously install package!"
sudo apt autoremove $toInstall
echo "No re-installing the entered file"
sudo apt-get install $toIntstall
-----------------------------------------------------------------------------------------------------------------------
#!/bin/bash
echo "Enter some value"
read value
echo "you have entered :" $value 
read -p "Enter your name :" name 
echo "Hi $name !! Good Day !! you have entered the value $value"
-----------------------------------------------------------------------------------------------------------------------
#!/bin/bash
read -p "Enter the First number :" number1
read -p "Enter the Second number :" number2
echo $((number1 + number2))
-----------------------------------------------------------------------------------------------------------------------
#!/bin/bash
read -p "Enter the First number :" number1
read -p "Enter the Second number :" number2
number3=$((number1+number2))
echo $number3
read -p "Enter the First number :" number1
read -p "Enter the Second number :" number2
echo $((number1 + number2))
read -p "Enter the First number :" number1
read -p "Enter the Second number :" number2
let number1=$number1
let number2=$number2
let number3=number1+number2
echo $number3
------------------------------------------------------------------------------------------------------------------------
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
-------------------------------------------------------------------------------------------------------------------------
#!/bin/bash
# infinite loop
while :
do 
echo "I am inside while loop"
sleep 10
echo "I have just wakeup after 10 seconds"
done
-------------------------------------------------------------------------------------------------------------------------
#!/bin/bash
let num1=100
let num2=20
if [ $num1 -gt $num2 ]
then
echo "$num1 is greater than $num2"
fi 
-------------------------------------------------------------------------------------------------------------------------
