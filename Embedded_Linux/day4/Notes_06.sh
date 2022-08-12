Notes

--> Standard file descriptor :
    => stdin - takes input from the console / terminal
    => stdout - prints output from the console / terminal
    => stderr - prints error on console / terminal 

--> tty command
    => The tty command of terminal basically prints the file name of the terminal connected to standard input. 
tty is short of teletype, but popularly known as a terminal it allows you to interact with the system by passing 
on the data (you input) to the system, and displaying the output produced by the system.
    => 0 : stdin in terminal 
    => 1 : stdin is not in terminal 

--> terminal to terminal communication

--> First terminal
    => ~$ tty
    => /dev/pts/2
    => ~$ echo "Communication between /dev/pts/0"
    => Communication between /dev/pts/0
    => ~$ echo "Communication between /dev/pts/0" > /dev/pts/0

--> Second terminal
    => ~$ tty
    => /dev/pts/0
    => ~$ Communication between /dev/pts/0

--> cat command
    => ~/DIOT_Lect/embedded_linux/day4$ cat >> mylearning.txt
    => "hello world!"~/DIOT_Lect/embedded_linux/day4$
    => ~/DIOT_Lect/embedded_linux/day4$ cat mylearning.txt
    => "hello world!"~/DIOT_Lect/embedded_linux/day4$

--> head and tail commands
--> head command
    => head -n # n stands for numeric value # display n lines from starting of the file
    => head -n <file.txt>
    => ~/DIOT_Lect/embedded_linux/day4$ cat ajkagyaan.txt | head -10
    => 1  sudo apt-get update
    => 2  sudo apt-get upgrade
    => 3  cd $HOME
    => 4  ls
    => 5  cd DIOT_Lect
    => 6  ls
    => 7  cd python
    => 8  ls
    => 9  python simple_calculator.py
    => 10  python3
--> tail command
    => tail -n # n stands for numeric value # display n lines from the ending of the file
    => tail -n <file.txt>
    => ~/DIOT_Lect/embedded_linux/day4$ cat ajkagyaan.txt | tail -10
    => 265  cat >> quote.txt >> hardworking is key to success
    => 266  cat >> quotes.txt
    => 267  cat quote.txt
    => 268  cat quotes.txt
    => 269  cat >> quote.txt
    => 270  cat quote.txt
    => 271  cat < quote.txt
    => 272  cat < quote.txt > quote1.txt
    => 273  cat quote1.txt
    => 274  history > ajkagyaan.txt
--> Works well and practiced with pipe (|) operator 
    => ls -l | head -5
    => ls -l | tail -5
--> pipe : used for Inter process input 
    => it redirects the output of one process to the input of another process 
    => e.g ls -l | head -5
        here the ls -l output is eventually becoming the input of head -5 process 
--> cat command 
    => ~/DIOT_Lect/embedded_linux/day4$ echo "Hii" > 1.txt
    => ~/DIOT_Lect/embedded_linux/day4$ cat 1.txt > 9.txt
    => ~/DIOT_Lect/embedded_linux/day4$ cat 9.txt
    => Hii
    => ~/DIOT_Lect/embedded_linux/day4$ cat 1.txt
    => Hii
    => ~/DIOT_Lect/embedded_linux/day4$ cat 1.txt | cat
    => Hii
    => ~/DIOT_Lect/embedded_linux/day4$ cat 1.txt | cat > 9.txt
    => ~/DIOT_Lect/embedded_linux/day4$ cat 9.txt
    =>Hii
