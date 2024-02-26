import threading
import timeloops
import commands
import os
import platform
if platform.system() == "Windows":
        os.system('cls')
elif platform.system() in ["Linux", "Darwin"]:  
    os.system('clear')
global table # ID, Price, Amount, Name
global money
money = 100



threadCommands = threading.Thread(target=commands.userInput)
threadTimeloop = threading.Thread(target=timeloops.timeloop)

threadCommands.start()
threadTimeloop.start()

threadCommands.join()

threadTimeloop.join()