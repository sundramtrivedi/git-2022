file=/etc/passwd
while read -r line; do
	echo $line
done < "$file"

<<notes
Instead of controlling the while loop with a condition, we are using input
redirection (< "$file") to pass a file to the read command, which 
controls the loop. The while loop will run until the last line is read. 
When reading file line by line,always use read with the -r option to prevent 
backslash from acting as an escape character.
notes
<<notes2
When reading file line by line, always use read with the -r option to 
prevent backslash from acting as an escape character. By default, the read
command trims the leading/trailing whitespace characters (spaces and tabs). 
Use the IFS= option before read to prevent this behavior: 
notes2 
