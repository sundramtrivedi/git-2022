--> if then condition

#!/bin/bash
read -p "Enter the name : " name
if [ $name == payal ]
then
echo "Welcome Payal"
read -p "Enter your percentage : " marks
if [ $marks == 80 ]
then
echo "Congratulations you got $marks %"
fi
fi
----------------------------------------------------------------------------------------------------------------------
--> nested if else condition

#!/bin/bash
read -p "Enter the name :" name
if [ $name == payal ]
then
echo "Welcome user payal"
else if [ $name == me ]
then
echo "Welcome user me"
else if [ $name == you ]
then
echo "Invalid user you"
fi
fi
fi
---------------------------------------------------------------------------------------------------------------------
--> nested if then condition

#!/bin/bash
read -p "Enter the name :" name
        if [ $name == payal ]
        then
                read -p "Enter the prn :" prn
                if [ $prn == 22 ]
                then
                echo "Embedded linux"
                fi
        fi

        if [ $name == me ]
        then
                read -p "Enter the prn :" prn
                if [ $prn == 06 ]
                then 
                echo "Python"
                fi
        fi

        if [ $name == you ]
        then
                read -p "Enter the prn :" prn
                if [ $prn == 13 ]
                then 
                echo "HTML and CSS"
                fi
        fi
---------------------------------------------------------------------------------------------------------------------
--> nested if else user input 

#!/bin/bash
read -p "Enter the name of student :" name
read -p "Enter the prn of student :" prn
read -p "Enter the branch name of student :" branch_name
read -p "Enter the age of student :" age
read -p "Enter the salary of student :" salary

        if [ $name == "payal" ]
        then
                if [ $prn == 22 ]
                then
                      if [ $branch_name == "iot" ]
                        then
                                echo "You are part of this Organization"
                        fi
                fi
        else
                echo "You are not allowed to enter"
        fi

        if [ $age == 23 ]
        then
                if [ $salary == 100 ]
                then
                        echo "You are no more student but employee"
                fi
        else
                echo "you are still student"
        fi



        if [[ $name == "payal" && $prn == 22 && $branch_name == "iot" ]]
        then
                echo "you are part of this Organization"
        else
                echo "you are not allowed to enter"
        fi
        if [[ $age == 23 && $salary == 100 ]]
        then
                echo "You are no more student but employee"
        else
                echo "You are still student"
        fi
---------------------------------------------------------------------------------------------------------------------
--> sum of 2 numbers user input 

#!/bin/bash
read -p "Enter the number 1 :" num1
read -p "Enter the number 2 :" num2
sum=`expr $num1 + $num2`
echo "$num1 + $num2 = $sum"
---------------------------------------------------------------------------------------------------------------------
--> positive , negative and zero using if elif else 

#!/bin/bash
read -p "Enter the number :" number
if [ $number -lt 0 ];
then
        echo "Number is negative"
elif [ $number -gt 0 ];
then
        echo "Number is positive"
else
        echo "Number is neither positive nor negative"
fi
-------------------------------------------------------------------------------------------------------------------
--> check if string is empty and strings are equal or not 

#!/bin/bash
read -p "Enter the string 1 :" str1
read -p "Enter the string 2 :" str2
str="aabbaa"
str_1=''
        if [[ -z $str ]]
        then
                echo "String is empty"
        else
                echo "String is not empty"
        fi

        if [[ -n $str_1 ]]
        then
                echo "String is not empty"
        else
                echo "String is empty"
        fi

        if [[ $str1 == $str2 ]]
        then
                echo "Strings are same"
        else
                echo "Strings are not same"
        fi
------------------------------------------------------------------------------------------------------------------
--> case expression in 
        pattern1)
        statements
        ;;
        pattern2)
        statements
        ;;
        pattern3)
        ;;
        patternn)
        ;;
        *)
            statements
            ;;
        esac
    notes