<<comment
There are two ways 
comment

helloworld ()
{
    echo "hello $1"
    echo "shell syntax is very difficult"
}
#call a function here it is called 3times and with arguments
helloworld `ls`
helloworld "diot" 
read -p "enter the name with whom you want to say to hello : " hello
helloworld $hello 


#sum function
function sum()
{
    let res=$1+$2
    echo $res
}
#function call with arguemnts
sum 10 20

#function definition
function quote
{
    echo "function can be created without bkts in function name"
}
#function call
quote
