Notes

--> s => stands for socket file 

--> file permission shortforms 
    => r --> read 
    => w --> write 
    => x --> execute 
    => u --> user 
    => g --> group 
    => o --> other 
    => a --> all 
    => + --> add
    => - --> remove
    => = --> assign 
----------------------------------------------------------------------------------------------
chmod u+rwx a.txt   # user have read write and execute (+ to add)
chmod u-rwx a.txt   # user does not read , write and execute (- to remove)
---------------------------------------------------------------------------------------------
--> file permissions commands 
    => 0 --> No rights
    => 1 --> executable right 
    => 2 --> write right 
    => 4 --> read right 
    => 4 + 1 --> read and executable right 
    => 4 + 2 --> read and write right 
    => 4 + 1 + 2 --> read , write and executable right 

--> how to turn a perticular program inti script 
--> chmod
--> numerical representation of file permission (octal representation)
-----------------------------------------------------------------------------------------------
--> Assignment
-----------------------------------------------------------------------------------------------
--> 1) create a python program say helloworldsc.py 
--> and print hello world
--> helloworldsc.py should be run as a script 
--> file should have read, write and execute(rwx) permission for owner
--> r,w too group members and no permission to the others

=>  answer 1 :-    
            => $ nano hello_world.py
            => $ chmod 760 hello_world.py
            => $ ls -l
            total 32
            -rwxrw---- 1 pedha pedha   35 Apr 11 08:18 hello_world.py

    answer 2 :-
            => $ nano hello_world.py
            => $ chmod u+rwx,g+rw,o-rwx hello_world.py
            => $ ls -l
            total 32
            -rwxrw---- 1 pedha pedha   35 Apr 11 08:18 hello_world.py
-----------------------------------------------------------------------------------------------
--> to run a python program as a script first line :
        => #!/usr/bin/python3
-----------------------------------------------------------------------------------------------
--> 2) create a file file2.txt and provide user to read and write (rw) permission and no permission to group and others 
=>  answer 1 :-
            => $ nano file2.txt
            => $ chmod 600 file2.txt
            => $ ls -l
            total 32
            -rw------- 1 pedha pedha   26 Apr 11 08:38 file2.txt

    answer 2 :-
            => $ nano file2.txt
            => $ chmod u+rw,u-x,g-rwx,o-rwx file2.txt
            => $ ls -l
            total 32
            -rw------- 1 pedha pedha   26 Apr 11 08:38 file2.txt
--------------------------------------------------------------------------------------------------------------------------
--> 3) create a file file3.txt and provide user to read and write (rw) permission and read permission to group and rw to others
=>  answer 1 :-
            => nano file2.txt
            => $ chmod 646 file3.txt
            => $ ls -l
            total 36
            -rw-r--rw- 1 pedha pedha   45 Apr 11 08:40 file3.txt
    answer 2 :-
            => $ nano file3.txt
            => $ chmod u+rw,u-x,g+r,g-wx,o+rw,o-x file3.txt
            => $ ls -l
            total 36
            -rw-r--rw- 1 pedha pedha   45 Apr 11 08:40 file3.txt
--------------------------------------------------------------------------------------------------------------------------
--> 4) create a file file4.txt and provide user to write (w) permission group to read and others to execute permissions
=>  answer 1 :-
            => nano file4.txt
            => $ chmod 241 file4.txt
            => $ ls -l
            total 40
            --w-r----x 1 pedha pedha   26 Apr 11 08:43 file4.txt
    answer 2 :-
            => $ nano file4.txt
            => $ chmod u+rw,u-x,g+r,g-wx,o+rw,o-x file4.txt
            => $ ls -l
            total 40
            --w-r----x 1 pedha pedha   26 Apr 11 08:43 file4.txt
--------------------------------------------------------------------------------------------------------------------------

************************************************************************************************************************
--> COPY a file 

cp <source_file_path> <destination_file_path>

--> move file 

mv <source_file_path> <destination_file_path>
************************************************************************************************************************

--------------------------------------------------------------------------------------------------------------------------
