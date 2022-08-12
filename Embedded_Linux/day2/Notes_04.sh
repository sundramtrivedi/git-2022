Notes
--> sudo is a substitute user
--> sudo su => root user => privileged
--> login => normal user 
---------------------------------------------------------------
login as a root user
--> iot$ sudo su
--> root@iot:/etc/apt# whoami
--> root
--> root@iot:/etc/apt#
Note: 
1. root user has all the privileged
2. whenever we run command with sudo our normal user get all 
 the privileges that root posses
--> NSSR => Non Standard software Review
# to check where is a utility/command is located
--> whereis <nameofutility>
--> iot$ where is python3
--> python3 > /user/bin/python3.6/user/.....
---------------------------------------------------------------
# to create a directory :
--> mkdir <dirname>
--> example :
--> mkdir linux #linux directory will be created
--> mkdir -v linux1 # will print background process too(-v => verbose)
Assignment
1. Navigate to linux and create a directory practice in one statement
Note :
--> Move into home directory from anywhere just type : cd
--> go one directory back : use ..
--> e.g =>
--> iot$ cd ~/linux/day
--> iot$ cd..
--> iot$ pwd :
--> iot$ /home/embeded_linux/linux
Assignment
--> How to create directory inside directory in one command 
--> e.g create 1/2/3/4 inside embeded_linux
--> iot$ mkdir -p 1/2/3/4
# to check directory hierarchy use tree command
#install tree
--> iot$ sudo apt install tree
--> iot$ tree
.
├── 1
│   └── 2
│       └── 3
│           └── 4
├── hello.c
├── hello.out
├── linux
├── Notes_02.sh
└── Notes_04.sh

5 directories, 4 files
# create a blank file using touch file command
--> iot$ touch <nameoffile>
--> iot$ touch 1.txt
--> iot$ ls 
--> 1 1.txt 
# display the content of a file use cat command
--> iot$ cat 1.txt 
# write some data inside a file with echo and redirection operator
--> iot$ echo " Hello this is my first file " > 1.txt