# GDBjail1
## Description
Lets see how you escape hell , i mean gdb
## remote  connection
nc pwn.dh.securinets.tn 2016

And we're given a python code

```
import gdb 

## gdb -x jail.py main
gdb.execute("start")

while 1:
    
    try :
    
        command=input("> ")
        parts=command.split()  
    
        blacklist=["python","python-interactive"]
        ## validation 
        for blacklisted_word in blacklist:
            if parts[0] in blacklisted_word : 
                print("!!!! no pasaran !!!!")
                continue

        gdb.execute(command)
    except gdb.error as e:
        print(e)
    except : 
        pass        

```

AI helped me on this one , i asked it how to get a shell from a GDB environment and under those restrictions to get a flag and he gave me some commands from which this one worked !  


![GDB1](https://github.com/Rayene9052/darkest-hour-ctf-writeups/blob/0de1dab5a8d420fd7225bfc13e45c102954e7992/assets/gdb1.PNG)