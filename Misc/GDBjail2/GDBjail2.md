
# GDBjail2
## Description 
escape (2)
## Remote
nc pwn.dh.securinets.tn 2017

And we're given a python code

```
import gdb 

## gdb -x jail.py main
gdb.execute("start")

while 1:
    try :
        command=input("> ")
        parts=command.split()  
        whitelist=["set","x","continue","help","quit"]
        if parts[0] not in whitelist or (not command.isascii()): 
            print("!!!! ya met7ayel !!!!")
            continue

        gdb.execute(command)
    except gdb.error as e:
        print(e)
    except : 
        pass        

``` 

# Method 
Ai also helped me on this one  giving me that command 
![DGBjail2](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/1a27cacc215c4a23943379b94934ae06255fae2a/assets/gdbjail2.PNG)

This was not the way  that it's supposed to be done as the author told me , we were intended to write a shell code to manipulate some register values .
This worked because the script only checks if the first argument of the command exists in the whitelist but does not inspect the whole expression. With set $var = system("cat flag.txt"), GDB invokes the system() function, which executes a shell and performs cat flag.txt, printing the flag.
