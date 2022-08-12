#!/bin/bash
<<notes
return can be used with the function but limitation with return is.
1. It can only return unsigned number
2. Number between 0 to 255.
The best practice and alternative to return is demonstrated in the
---> multiplication function 
--> the demo for the return function is kept in the division function. (max output can be retured is 255)
--> function takes argument in form of $1 as first argument , $2 as second argument.
notes
#multiplication function definition and declaration
multiplcation()
{
    mulres=`expr $1 \* $2`
    echo $mulres                
}

#division function declaration and definition
division()
{
    divres=`expr $1 \/ $2`
    return $divres
}
# take input from the user
read -p "Enter first number : "  number1
read -p "Enter second number : " number2

#call the function 1 and store the value in variable retval
retval=`multiplcation $number1 $number2`
echo $retval

#call the division function
division $number1 $number2         
result=$?    #the return value is stored in $? -- get it and store it in result variable
echo "$number1 / $number2 = $result"   #print the result