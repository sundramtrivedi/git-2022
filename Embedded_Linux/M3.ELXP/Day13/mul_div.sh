function mul
{
    #\ is used for parsing here as * w/o slash is considered as select all 
    #\ in case division will be cosidered as go to next directory so here aslo we need to use parsing
    let mulres=`expr $1 \* $2`
    return $mulres
}
read -p "Enter a:" a
read -p "enter b:" b
mul $a $b
res=$?
echo "$a * $b:"$res
function division
{
    let divres=`expr $1\/$2`
    return $divres
}
division $a $b
dres=$?
echo "$a / $b:" $dres