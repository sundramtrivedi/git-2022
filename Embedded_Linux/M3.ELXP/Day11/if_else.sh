#!/bin/bash
read -p "Enter name: " name
if[$name=="Ganesh"]
then
echo "Your name is in the list"
read "Enter your PRN:" prn 
if[$prn==123]
then
echo " Your prn is verified can take exam in 15 min"
else
echo "You cannot take exam"
fi
fi

