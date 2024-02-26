import drugtable
import nametoid
import os
import math
def userInput():
    while True:
        drugtable.money = int(math.floor(float(drugtable.money)))
        user_input = input("\nWhat would you like to do? ")
        drugtable.money=int(drugtable.money)
        if user_input == "buy" or user_input == 'b':
            buying = input('\nWhat would you like to buy? (nvm to cancel) ')
            if buying == 'nvm':
                continue

            amount = input('\nHow much would you like to buy? (nvm to cancel) ')
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
                    print(f'\nGrind harder, you broke idiot. (You need {req} more money)\n')
            except ValueError:
                print('\nEnter a numeric value or a shorthand (max). \n')
                continue

        if user_input == 'sell' or user_input == 's':
            selling = input('\nWhat would you like to sell? (nvm to cancel) ')
            if selling == 'nvm':
              continue
            
            amount = input('\nHow much would you like to sell? (nvm to cancel) ')
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
                    print('\nYou can\'t sell what you don\'t have, idiot.\n')
            except ValueError:
                print('\nEnter a numeric value or a shorthand (max). \n')
                continue

        if user_input == 'inventory' or user_input == 'i':
            print('\n')
            for x in range(0, len(drugtable.table)):
                print(f'{drugtable.table[x][3]} Owned:  {drugtable.table[x][2]}       Current Price: {drugtable.table[x][1]}')
            print('\n')

        if user_input == 'balance' or user_input == 'bal':
            print(f'\nYou have {drugtable.money} money.\n')
        if user_input == 'price':
            price = input('\nPrice of what? ')
            print(f'\nThe price of {price} is {drugtable.table[nametoid.toID(price)][1]}\n')
        if user_input == 'cls' or user_input == 'clear':
            if os.name() == 'posix':
                os.system('clear')
            if os.name() == 'nt':
                os.system('cls')
