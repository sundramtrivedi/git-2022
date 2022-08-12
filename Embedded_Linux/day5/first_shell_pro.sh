#!/bin/bash
mkdir shell_p && cd shell_p
echo "My first shell script" > program1.txt | cat program1.txt |tee program2.txt  
echo "The data is written in file"