trap "echo once signal is send I will be terminated" EXIT
i=1
while true
do
echo "the value of i is $i"
((i++))
done
