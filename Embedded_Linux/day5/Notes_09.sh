Notes

--> pipe 
--> head
--> tail 
--> paging
--> sda , sdb , sdc 
--> JIRA
--> df -h => disk file usage

*************************************************************************************
=> What is inode in linux ?
*************************************************************************************

--> ls -lit or ls -li   => inode number

--> ls -li
--> total 4
--> 1047962 -rw-rw-r-- 1 pedha pedha 218 Apr  9 19:01 Notes_09.sh

--> ls -litr
--> total 4
--> 1047962 -rw-rw-r-- 1 pedha pedha 218 Apr  9 19:01 Notes_09.sh

--> tee command:
--> use case
--> prints stdout at the same time write to the file system :

--> df -hi | tee disk_file_usage.txt 

--> version 18.04 => bionic

--> LTS => Long Term Support

--> explicitly
--> emplicitly
--> static type language

--> static and dynamic programming
--> shebang command 


--> polyglot programmer


--> what is script?
        => In script first line should be shebang 
        => shebang is nothing but the interpreter path
        => it must be start with #! < followed by path >
        => e.g 
                => python3 --> #!/sur/bin/python3
                => bash --> #!/bin/bash
        => script can be run from the background and at the run time.
        => e.g 
                => ./filenameofscript
        => bash programming can be written as bash script too
        => python programming can be written as a script too 
        => for scripting language must be dynamically typed / interpreter based 
        => script must have executable permissions

--> sample script :
        write a bash script that creates a directory and creates a file and write the data "My first shell script"
            => #!/bin/bash
            => mkdir shell_p
            => echo "My first shell script" > program1.txt 