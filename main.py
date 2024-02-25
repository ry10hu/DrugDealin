import threading
import timeloops
import commands

global table # ID, Price, Amount, Name
global money
money = 100





threadCommands = threading.Thread(target=commands.userInput)
threadTimeloop = threading.Thread(target=timeloops.timeloop)

threadCommands.start()
threadTimeloop.start()

threadCommands.join()

threadTimeloop.join()


