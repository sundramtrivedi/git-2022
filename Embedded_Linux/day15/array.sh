#!/bin/bash
index_array={1 2 3 4 5 6}
echo ${index_array[0]}
for i in ${index_array[@]}
do
	echo $i
done
echo "length of the array is : " ${#index_array[@]}
name[0]="Payal"
name[1]="Ganesh"
name[2]="Vishwajit"
name[3]="Sundram"
name[4]="Likhil"
echo "First Index value : " ${name[0]}
echo "All members of array : " ${name[*]}
echo "All members of array : " ${name[@]}
