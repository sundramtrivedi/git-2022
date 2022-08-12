#!/bin/bash
factorial()
{<<comment
    let fact=1
    for((i=1;i<=$num1;i++))
        (($fact*$i))
        echo $fact
comment
    let fact=1
    for((i=1;i<=$num1;i++))
    {
        fact=`expr $i \* $fact`
        #(( $fact*$i ))
    }
        echo "Factorial of $num1 is : " $fact

}
       
read -p "Enter num1 :" num1
factorial $num1 
#echo $?
