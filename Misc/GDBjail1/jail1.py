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
