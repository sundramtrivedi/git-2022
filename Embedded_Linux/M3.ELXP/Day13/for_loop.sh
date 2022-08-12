#!/bin/bash
for i in 1 2 3 4 5
do
    echo "Loop runs $i times"
done
for i in {0..5}
do  
    echo "Loop runs for $i times"
    echo "after incerement"
    ((i++))
    echo "Loop runs for $i times"
done