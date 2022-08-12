#!/bin/bash
helloworld()
{
	echo "hello $1"
	echo "Shell syntax is very difficult"
}
helloworld "DIOT2022"
read -p "Enter the name with whom you want to say hello : " hello
helloworld $hello
# passing argument in function
sum()
{
	let result=$1+$2
	res=$(($1+$2))
	expr $1 + $2
	echo $res
	echo $result
}
sum "10" "20"
