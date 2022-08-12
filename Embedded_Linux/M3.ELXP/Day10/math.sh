let x=20
let y=30
let sum=x+y
echo "sum of $x+$y :" $sum
#concatenation
read -p "enter 1st num : " num1
read -p "enter 2nd num : " num2
num3=$num1+$num2
echo $num3
echo "sum:" $((num1+num2))

num3=$((num1+$num2))
echo "num3": $num3