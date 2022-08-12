#!/bin/bash
time="2" 
echo process is $$
while (( count < 10 ))
do 
    sleep ${time}
    echo $count
     
    (( count++ ))
done
     