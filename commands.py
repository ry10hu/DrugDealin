import drugtable
import nametoid
import os
def userInput():
    while True:
        user_input = input("What would you like to do? ")
        drugtable.money=int(drugtable.money)
        if user_input == "buy" or user_input == 'b':
            buying = input('What would you like to buy? (nvm to cancel) ')
            if buying == 'nvm':
                continue

            amount = input('How much would you like to buy? (nvm to cancel) ')
            try:
                if amount == 'nvm':
                    continue
                if amount == 'max':
                    amount = drugtable.money/drugtable.table[nametoid.toID(buying)][1]
                else:
                    amount = int(amount)
                if drugtable.money >= amount * drugtable.table[nametoid.toID(buying)][1]:
                    drugtable.money -= amount * drugtable.table[nametoid.toID(buying)][1]
                    drugtable.table[nametoid.toID(buying)][2] += amount
                else:
                    req = amount * drugtable.table[nametoid.toID(buying)][1] - drugtable.money
                    print(f'Grind harder, you broke idiot. (You need {req} more money)')
            except ValueError:
                print('Enter a numeric value. ')
                continue

        if user_input == 'sell' or user_input == 's':
            selling = input('What would you like to sell? (nvm to cancel) ')
            if selling == 'nvm':
              continue
            
            amount = input('How much would you like to sell? (nvm to cancel) ')
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
                    print('You can\'t sell what you don\'t have, idiot.')
            except ValueError:
                print('Enter a numeric value. ')
                continue

        if user_input == 'inventory' or user_input == 'i':
            # Add your inventory logic here
            pass

        if user_input == 'balance' or user_input == 'bal':
            print(f'You have {drugtable.money} money.')
        if user_input == 'price':
            price = input('Price of what? ')
            print(f'The price of {price} is {drugtable.table[nametoid.toID(price)][1]}')
        if user_input == 'cls' or user_input == 'clear':
            os.system('cls')
