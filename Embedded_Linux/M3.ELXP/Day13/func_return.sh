#how to return a value from function
<<comment function sub
{
    let  num1=$1
    let  num2=$1
    let diff=num1-num2
    return $diff
}
sub 20 10
echo $?
comment

function sub
{
    #arguments are passed as below in shell and not with function name
    return $(($1-$2))
}
read -p "Enter num1 :" num1
read -p "Enter num2 :" num2
#function call with agr from user input
sub $num1 $num2
#$? will print the latest succesfully cmd
let ret_diff=$?
echo "retuned value from function:"$?
echo "returned value stored in x is :" $ret_diff

