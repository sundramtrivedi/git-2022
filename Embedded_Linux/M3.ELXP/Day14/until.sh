#!/bin/bash
i=0
until [ $i -gt 3 ]
do 
    echo "i : $i"
    ((i=i+1))
done
i=0
#till $i -eq 3 is acheived until will execute as soon as condition is true util will get out
until [ $i -eq 3 ]
do 
    echo "i : $i"
     ((i=i+1))
done