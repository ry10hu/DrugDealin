import drugtable, nametoid, os, platform, math, random, colours
import xml.etree.cElementTree as ET
from colorama import Fore, Back, Style

def userInput():
    while True:
        save = ET.Element('save')
        items = ET.SubElement(save, 'items')
        drugtable.money = int(math.floor(float(drugtable.money)))
        user_input = input(colours.questioncolour + "\nWhat would you like to do? " + colours.inputcolour).lower().split()
        # print('\n')
        if len(user_input) >= 1:
            if user_input[0] =='save':
                ### Saves the user's drug information
                ET.SubElement(items, 'meth', price=str(drugtable.savetable[0][1]), owned=str(drugtable.savetable[0][2]))
                ET.SubElement(items, 'cocaine', price=str(drugtable.savetable[1][1]), owned=str(drugtable.savetable[1][2]))
                ET.SubElement(items, 'heroin', price=str(drugtable.savetable[2][1]), owned=str(drugtable.savetable[2][2]))
                ET.SubElement(items, 'marijuana', price=str(drugtable.savetable[3][1]), owned=str(drugtable.savetable[3][2]))
                ET.SubElement(items, 'opium', price=str(drugtable.savetable[4][1]), owned=str(drugtable.savetable[4][2]))
                tree = ET.ElementTree(save)
                tree.write('saves/save.xml')         
                
            # if user_input[0] == 'load':
            #     print('\n' + colours.answercolour + 'Loading...' + '\n')
            #     drugtable.savetable = drugtable.loadtable
            #     print(colours.answercolour + 'Loaded!')
            if user_input[0] == 'changestock':
        
                for x in range(0, len(drugtable.savetable)):
                    number = random.randint(-20, 20)
        
                    if drugtable.savetable[x][1] + number > 0:
                        drugtable.savetable[x][1] += number    
            drugtable.money=int(drugtable.money)

            if user_input[0] == "buy" or user_input[0] == 'b':
                print(len(user_input))
        
                if len(user_input) == 3:
                    buying = user_input[1]
                    amount = user_input[2]
        
                else:
                    print(colours.answercolour + '\nERROR: WRONG SYNTAX. The Correct Syntax Is: buy {drug} {amount}' + colours.warningcolour)
                    continue
        
                try:
        
                    if amount == 'max':
                        amount = int(drugtable.money/drugtable.savetable[nametoid.toID(buying)][1])
        
                    else:
                        amount = int(amount)
        
                    if drugtable.money >= amount * drugtable.savetable[nametoid.toID(buying)][1]:
                        drugtable.money -= amount * drugtable.savetable[nametoid.toID(buying)][1]
                        drugtable.savetable[nametoid.toID(buying)][2] += amount
        
                    else:
                        req = amount * drugtable.savetable[nametoid.toID(buying)][1] - drugtable.money
                        print(colours.answercolour + f'\nGrind harder, you broke idiot. (You need {req} more money)' + colours.inputcolour)
        
                except ValueError:
                    print('\nEnter a numeric value or a shorthand (max). \n')
                    continue

            if user_input[0] == 'sell' or user_input[0] == 's':
        
                if len(user_input) == 3:
                    selling = user_input[1]
                    amount = user_input[2]
        
                else:
                    print(colours.answercolour + '\nERROR: WRONG SYNTAX. The Correct Syntax Is: sell {drug} {amount}' + colours.inputcolour)

                try:
        
                    if amount == 'max':
                        amount = drugtable.savetable[nametoid.toID(selling)][2]
        
                    else:
                        amount = int(amount)
        
                    if drugtable.savetable[nametoid.toID(selling)][2] >= amount:
                        drugtable.money += amount * drugtable.savetable[nametoid.toID(selling)][1]
                        drugtable.savetable[nametoid.toID(selling)][2]-= amount
        
                    else:
                        print(colours.answercolour + '\nYou can\'t sell what you don\'t have.' + colours.inputcolour)
        
                except ValueError:
                    print('\nEnter a numeric value or a shorthand (max). \n')
                    continue

            if user_input[0] == 'inventory' or user_input[0] == 'i':
                
                for x in range(0, len(drugtable.savetable)):
                    print(colours.answercolour + f'\n{drugtable.savetable[x][3]} Owned:  {drugtable.savetable[x][2]}      Current Price: {drugtable.savetable[x][1]}' + colours.inputcolour)
                

            if user_input[0] == 'balance' or user_input[0] == 'bal':
                print(colours.answercolour + f'\nYou have {drugtable.money} money.' + Style.RESET_ALL)
        
            if user_input[0] == 'price':
                price = user_input[1]
                print(colours.answercolour + f'\nThe price of {price} is {drugtable.savetable[nametoid.toID(price)][1]} money.' + Style.RESET_ALL)
        
            if user_input[0] == 'cls' or user_input[0] == 'clear':
        
                if platform.system() == "Windows":
                    os.system('cls')
        
                elif platform.system() in ["Linux", "Darwin"]:  
                    os.system('clear')