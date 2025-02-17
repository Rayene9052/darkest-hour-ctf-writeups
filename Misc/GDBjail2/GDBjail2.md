
# GDBjail2
## Description 
escape (2)
## Remote
nc pwn.dh.securinets.tn 2017

# Method 

This is not the way  that it's supposed to be done as the author told me , we were intended to write a shell code to manipulate some register values .
![DGBjail2]
This worked because the script only checks if the first argument of the command exists in the whitelist but does not inspect the whole expression. With set $var = system("cat flag.txt"), GDB invokes the system() function, which executes a shell and performs cat flag.txt, printing the flag.