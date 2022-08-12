file=h1.txt
while IFS= read -r line; do 
    echo $line 
done < "$file"
