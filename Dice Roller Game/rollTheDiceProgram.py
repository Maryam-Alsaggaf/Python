import random 
def rolling_the_dice(dices):
    if dices==1:
            print('Rolling the Dice.....')
            print('Dice number is',random.randint(1,6))
            keepRolling=input('Do you want to keep rolling dice y/n: ')
            if keepRolling.upper()=='Y':
                rolling_the_dice(dices)
            elif keepRolling.upper()=='N':
                print('Rolling dice stopped.')
            else:
                print(' You should have enter a valid input try again ')
    if dices==2:
            print('Rolling the Dice.....')
            print('First dice number is',random.randint(1,6))
            print('Second dice number is',random.randint(1,6))
            keepRolling=input('Do you want to keep rolling dice y/n: ')
            if keepRolling.upper()=='Y':
                rolling_the_dice(dices)
            elif keepRolling.upper()=='N':
                print('Rolling dice stopped.')
            else:
                print(' You should have enter a valid input try again ')
    
def usedDices(numberOfDice):
    if numberOfDice=='2' or numberOfDice =='1':
        rolling_the_dice(int(numberOfDice))
    else:
        print('Enter a valid input ')
        secondTry= input('How many dice do you want to play with 1 or 2 : ')
        usedDices(secondTry)
        
def startPlaying():
    print('Hello at Roll Dice roller')
    numberOfDice =input('How many dice do you want to play with 1 or 2 : ')
    usedDices(numberOfDice)

startPlaying()
    

         
            
            
        
        
