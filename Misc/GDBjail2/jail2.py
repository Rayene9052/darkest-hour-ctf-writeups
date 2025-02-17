import gdb 

## gdb -x jail.py main
gdb.execute("start")
set *(long)0x11223344=7
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
