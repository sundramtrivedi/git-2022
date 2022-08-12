#!/bin/bash
for i in 1 2 3 4  5
do
	echo "Loop runs $i times"
done
echo " "
for i in {0..4}	# bash 3.0 support (start and end with +1 iteration)
do
	echo "Loop runs $i times"
done
echo " "
# bash 4.0 supports
# start End increment
for i in {0..10..2}
do
	echo "Value of i is : $i"
done
