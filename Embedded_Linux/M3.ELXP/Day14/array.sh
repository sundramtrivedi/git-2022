#!/bin/bash
index_array=(1 2 3 4 5)
#echo ${index_array[0]}
for i in ${index_array[@]}
do 
    echo $i
done
echo "length of the array is: ${#index_array[@]}"

#array element assigment at each index
name[0]="Sundar"
name[1]="Payal"
name[2]="Vishwa"
name[3]="Leekhil"
name[4]="Ganesh"
#access each elemet at index
echo "0th element of array : ${name[0]}"
#access all elements of array
echo "all array elements : ${name[@]}"
echo "all array elements: ${name[*]}"

