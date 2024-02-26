import drugtable, nametoid, os, platform, math, random, colours
from colorama import Fore, Back, Style

def userInput():
    while True:
        drugtable.money = int(math.floor(float(drugtable.money)))
        user_input = input(colours.questioncolour + "\nWhat would you like to do? " + colours.inputcolour).lower()
        # print('\n')
        if user_input == 'change stock':
            for x in range(0, len(drugtable.table)):
                number = random.randint(-20, 20)
                if drugtable.table[x][1] + number > 0:
                    drugtable.table[x][1] += number    
        drugtable.money=int(drugtable.money)
        if user_input == "buy" or user_input == 'b':
            buying = input(colours.questioncolour + '\nWhat would you like to buy? (nvm to cancel) ' + colours.inputcolour)
            if buying == 'nvm':
                continue

            amount = input(colours.questioncolour + '\nHow much would you like to buy? (nvm to cancel) ' + colours.inputcolour)
            try:
                if amount == 'nvm':
                    continue
                if amount == 'max':
                    amount = int(drugtable.money/drugtable.table[nametoid.toID(buying)][1])
                else:
                    amount = int(amount)
                if drugtable.money >= amount * drugtable.table[nametoid.toID(buying)][1]:
                    drugtable.money -= amount * drugtable.table[nametoid.toID(buying)][1]
                    drugtable.table[nametoid.toID(buying)][2] += amount
                else:
                    req = amount * drugtable.table[nametoid.toID(buying)][1] - drugtable.money
                    print(colours.answercolour + f'\nGrind harder, you broke idiot. (You need {req} more money)' + colours.inputcolour)
            except ValueError:
                print('\nEnter a numeric value or a shorthand (max). \n')
                continue

        if user_input == 'sell' or user_input == 's':
            selling = input(colours.questioncolour + '\nWhat would you like to sell? (nvm to cancel) ' + colours.inputcolour)
            if selling == 'nvm':
              continue
            
            amount = input(colours.questioncolour + '\nHow much would you like to sell? (nvm to cancel) ' + colours.inputcolour)
            try:
                if amount == 'nvm':
                    continue
                if amount == 'max':
                    amount = drugtable.table[nametoid.toID(selling)][2]
                else:
                    amount = int(amount)
                if drugtable.table[nametoid.toID(selling)][2] >= amount:
                    drugtable.money += amount * drugtable.table[nametoid.toID(selling)][1]
                    drugtable.table[nametoid.toID(selling)][2]-= amount
                else:
                    print(colours.answercolour + '\nYou can\'t sell what you don\'t have, idiot.' + colours.inputcolour)
            except ValueError:
                print('\nEnter a numeric value or a shorthand (max). \n')
                continue

        if user_input == 'inventory' or user_input == 'i':
            
            for x in range(0, len(drugtable.table)):
                print(colours.answercolour + f'\n{drugtable.table[x][3]} Owned:  {drugtable.table[x][2]}      Current Price: {drugtable.table[x][1]}' + colours.inputcolour)
            

        if user_input == 'balance' or user_input == 'bal':
            print(colours.answercolour + f'\nYou have {drugtable.money} money.' + Style.RESET_ALL)
        if user_input == 'price':
            price = input(colours.questioncolour+ '\nPrice of what? ' + colours.inputcolour)
            print(colours.answercolour + f'\nThe price of {price} is {drugtable.table[nametoid.toID(price)][1]} money.' + Style.RESET_ALL)
        if user_input == 'cls' or user_input == 'clear':
            if platform.system() == "Windows":
               os.system('cls')
            elif platform.system() in ["Linux", "Darwin"]:  
                os.system('clear')