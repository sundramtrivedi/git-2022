Notes
--> stdin
--> stdout
--> stderr

Re-direction operator (>)
-----------------------------------------------------------------------------------------------------
--> ~$ echo "This is my test file"
--> This is my test file
--> ~$ echo "This is my test file"> test_data.txt
--> ~$ ls
--> Desktop    Documents  Music     Public  Templates      Videos
--> DIOT_Lect  Downloads  Pictures  snap    test_data.txt

--> Note - > operator write the data from the begining of the line if no data is present 
else it will overwrite the existing data.
-----------------------------------------------------------------------------------------------------
--> How to append data?
-----------------------------------------------------------------------------------------------------
--> use >> append
--> ~$ echo "IOT is next gen tech" >> test_data.txt
--> ~$ cat test_data.txt
--> This is my test file
--> IOT is next gen tech
-----------------------------------------------------------------------------------------------------
# remove a directory that has no file
--> rmdir directory_name
--> ~$ mkdir test_dir && cd test_dir && touch 1.txt
--> ~$ tree
.
└── 1.txt

0 directories, 1 file
-----------------------------------------------------------------------------------------------------
--> How to delete a directory which contains file?
--> ~$ rmdir -v test_dir/
--> rmdir : removing directory,'test_dir/'
--> rmdir : failed to remove 'test_dir/' : Directory not empty
--> (rmdir will not work)
--> what next?
--> rm -rf test_dir/
--> r => recursive
--> f => force
-----------------------------------------------------------------------------------------------------
--> ~s echo "Hii Payal!" > ../embedded_linux/day3/test.txt
--> ~/DIOT_Lect/embedded_linux$ ls
--> day1  day2  day3
--> ~/DIOT_Lect/embedded_linux$ tree
.
├── day1
│   ├── hello.c
│   └── Notes_02.sh
├── day2
│   └── Notes_04.sh
└── day3
    ├── Notes_05.sh
    └── test.txt

3 directories, 5 files
--------------------------------------------------------------------------------------------------
Question :
--> create a directory test/1/2/3
--> navigate to 3
--> create a file 1.txt inside 1 dir and write "IOT is awesome" in this file without providing 
the absolute path.
--> ~/DIOT_Lect/embedded_linux/day3/question$ cd 1
--> ~/DIOT_Lect/embedded_linux/day3/question/1$ cd 2
--> ~/DIOT_Lect/embedded_linux/day3/question/1/2$ cd 3
--> ~/DIOT_Lect/embedded_linux/day3/question/1/2/3$ echo "IOt is awesome" > ../../1.txt 
--> ~/DIOT_Lect/embedded_linux/day3/question/1/2/3$ cd ..
--> ~/DIOT_Lect/embedded_linux/day3/question/1/2$ cd ..
--> ~/DIOT_Lect/embedded_linux/day3/question/1$ cd ..
--> ~/DIOT_Lect/embedded_linux/day3/question$ tree
.
└── 1
    ├── 1.txt
    └── 2
        └── 3

3 directories, 1 file
-------------------------------------------------------------------------------------------------
# use tab to view directories without cd command
--> ~/DIOT_Lect/embedded_linux/day3/question$ echo "IOT" >1/2/3/3.txt
--> ~/DIOT_Lect/embedded_linux/day3/question$ tree
.
└── 1
    ├── 1.txt
    └── 2
        └── 3
            └── 3.txt

3 directories, 2 files
--------------------------------------------------------------------------------------------------
# create a directory in 1 directory from 3rd directory
--> ~/DIOT_Lect/embedded_linux/day3/question$ cd 1/2/3
--> ~/DIOT_Lect/embedded_linux/day3/question/1/2/3$ mkdir ../../iot
--> ~/DIOT_Lect/embedded_linux/day3/question/1/2/3$ cd ..
--> ~/DIOT_Lect/embedded_linux/day3/question/1/2$ cd ..
--> ~/DIOT_Lect/embedded_linux/day3/question/1$ cd ..
--> ~/DIOT_Lect/embedded_linux/day3/question$ tree
.
└── 1
    ├── 1.txt
    ├── 2
    │   └── 3
    │       └── 3.txt
    └── iot

4 directories, 2 files
----------------------------------------------------------------------------------------------------
*What / Why / Where*
----------------------------------------------------------------------------------------------------
Listing of files/directory inside directory
--> ls
--> ls -l   #list files and directory
--> ls -a   #list files and directories including hidden one(.extension)
--> ls -lh  #shows sizes in human readable format
--> ls -r   #listing in reverse order
--> ls -R   #recursive list of sub directories
--> ls -lt  #sorting based on latest time #ls-itr(in reverse)
----------------------------------------------------------------------------------------------------
