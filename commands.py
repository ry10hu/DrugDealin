import drugtable, nametoid, os, platform, math
from colorama import Fore, Back, Style

def userInput():
    while True:
        drugtable.money = int(math.floor(float(drugtable.money)))
        user_input = input(Fore.BLUE + "\nWhat would you like to do? " + Fore.RED).lower()
        # print('\n')
        drugtable.money=int(drugtable.money)
        if user_input == "buy" or user_input == 'b':
            buying = input(Fore.BLUE + '\nWhat would you like to buy? (nvm to cancel) ' + Fore.RED)
            if buying == 'nvm':
                continue

            amount = input(Fore.BLUE + '\nHow much would you like to buy? (nvm to cancel) ' + Fore.RED)
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
                    print(Fore.GREEN + f'\nGrind harder, you broke idiot. (You need {req} more money)' + Fore.RED)
            except ValueError:
                print('\nEnter a numeric value or a shorthand (max). \n')
                continue

        if user_input == 'sell' or user_input == 's':
            selling = input(Fore.BLUE + '\nWhat would you like to sell? (nvm to cancel) ' + Fore.RED)
            if selling == 'nvm':
              continue
            
            amount = input(Fore.BLUE + '\nHow much would you like to sell? (nvm to cancel) ' + Fore.RED)
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
                    print(Fore.GREEN + '\nYou can\'t sell what you don\'t have, idiot.' + Fore.RED)
            except ValueError:
                print('\nEnter a numeric value or a shorthand (max). \n')
                continue

        if user_input == 'inventory' or user_input == 'i':
            
            for x in range(0, len(drugtable.table)):
                print(Fore.GREEN + f'\n{drugtable.table[x][3]} Owned:  {drugtable.table[x][2]}      Current Price: {drugtable.table[x][1]}' + Fore.RED)
            

        if user_input == 'balance' or user_input == 'bal':
            print(Fore.GREEN + f'\nYou have {drugtable.money} money.' + Style.RESET_ALL)
        if user_input == 'price':
            price = input(Fore.BLUE+ '\nPrice of what? ' + Fore.RED)
            print(Fore.GREEN + f'\nThe price of {price} is {drugtable.table[nametoid.toID(price)][1]} money.' + Style.RESET_ALL)
        if user_input == 'cls' or user_input == 'clear':
            if platform.system() == "Windows":
               os.system('cls')
            elif platform.system() in ["Linux", "Darwin"]:  
                os.system('clear')