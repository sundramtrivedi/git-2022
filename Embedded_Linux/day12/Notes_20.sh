--> Working with cut command :
-----------------------------------------------------
--> cut command is used to extract field wise data
--> Example a file having multiple fields and requirement is to get field 1 only
--> delimiter helps to get this done e.g. . or : or ""
--------------------------------------------------------------------------------------------------------------------
Assignment:
--> get all the username present in the /etc/passwd file.
--> get the username and associated bash shell names from /etc/passwd 
--> get username,UID and bash shell name 
--------------------------------------------------------------------------------------------------------------------
cut -d []
--------------------------------------------------------------------------------------------------------------------
--> How to write multiline commands :
----------------------------------------------------
--> use escape character :
ls \
-l 
--------------------------------------------------------------------------------------------------------------------
while IFS= read -r line; do 
    echo $line 
done < "$file"
--------------------------------------------------------------------------------------------------------------------
