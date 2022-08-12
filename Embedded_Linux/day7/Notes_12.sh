Notes 

--> uname
    => -a, --all
              print  all  information,  in the following order, except omit -p
              and -i if unknown:
    => -s, --kernel-name
              print the kernel name
    => -n, --nodename
              print the network node hostname
    => -r, --kernel-release
              print the kernel release
    => -v, --kernel-version
              print the kernel version

    => -m, --machine
              print the machine hardware name

    => -p, --processor
              print the processor type (non-portable)

    => -i, --hardware-platform
              print the hardware platform (non-portable)

    => -o, --operating-system
              print the operating system

    => --help display this help and exit

    => --version
              output version information and exit
---------------------------------------------------------------------------------------------------------------------------
System Information 

--> #!/bin/bash
--> # how to declare a variable
--> # variable_name=value (without space)
--> system_hostname=$('uname -n')
--> system_kernel_version=$('uname -v')
--> system_kernel_name=$('uname -s')
--> echo"Your System Name :"$system_hostname
--> echo"Your Kernel Version :"$system_kernel_version
--> echp"Yout Kernel Name :"$system_kernel_name 
----------------------------------------------------------------------------------------------------------------------------
Word Count 

--> wc => word count 
--> wc -c <filename>    # number of bytes
--> wc -m <filename>    # character count
--> wc -l <filename>    # new line count
--> wc -w <filename>    # number of words
--> wc -L <filename>    # length or width of longest line
--> wc filename       # lines words characters count from a file
-----------------------------------------------------------------------------------------------------------------------------
bc      # arbitary precision calculator language
# combining commands
wc <filename> ; ls -l <filename>
man     # manual pages
whatis  # display