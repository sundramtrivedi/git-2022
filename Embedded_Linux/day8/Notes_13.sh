








--------------------------------------------------------------------------------------------
--> client side requirements
--> 1) for windows based system - putty is recommended (UI based)
--> 2) for linux/mac --> ssh utility / putty optional
--> server side :
--------------------------------------------------------------------------------------------
--> ssh server must be installed
--> port number 22 should be open to listen incoming requests.
--> No firewall / proxy shold block port number 22
--------------------------------------------------------------------------------------------
# install openssh server on ubuntu if not installed:
--> sudo apt-get install openssh-server 
# enable the ssh service
--> sudo systemctl enable ssh 
# start the service
--> sudo systemctl start ssh 
    OR 
--> sudo service ssh start 
# check the ssh service status
--> sudo service ssh status 
    OR 
--> sudo systemctl status ssh 
--------------------------------------------------------------------------------------------
# log in to remote machines
--> ssh userName@Your-server-name-IP
Step 1:
--> Get the username : whoami
--> get the ipaddress of the system you want to coonect :
    => ifconfig
    => ip addr
    => ip a 
--------------------------------------------------------------------------------------------
How to access the ssh log :
--> cat /var/log/auth.log 
# ssh for key based communication :
--> ssh -i <key> username@ip 
--> e.g 
        => ssh -i test.pem iot@3.7.10.22

--> scp - secure copy
--------------------------------------------------------------------------------------------
Password change :
--> passwd 
--------------------------------------------------------------------------------------------
# scp username and password based
--> scp <file> username@ip:<path_of_the_file==where_to_copy_on_server>
--> e.g 
        => scp test.txt jeet@192.168.1.101:/home/diot/
--> key based :
        => scp -i <key> test.txt jeet@192.168.1.101:/home/jeet/
--------------------------------------------------------------------------------------------
