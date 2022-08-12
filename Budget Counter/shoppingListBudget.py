# program counts the budget of the user depending to his shopping list cost
def budgetCounter():
    item_list_name = []
    item_list_price = []
    print("Hello welcome to shopping budget counter Ready to count your budget let's start !")
    numberOfitems = int(input('Enter the numbers of items of you shopping list: '))
    budget = int(input('Enter your budget in RS : '))
    for i in range(numberOfitems):
        nameOfItem = input('Enter the name of item ' + str(i+1)+' of your shopping list : ')
        item_list_name.append(nameOfItem)
        try:
            itemPrice = int(input('Enter the price of ' + nameOfItem+' in RS'+' of your shopping list : '))
        except:
            print('Enter a valid input Try again')
            budgetCounter()
        item_list_price.append(itemPrice)
    print('Your list shopping is ' , item_list_name ,' and your budget is ',budget)
    is_it_enough(shopping_list_total(item_list_price),budget)


def shopping_list_total(listName):
    print(listName)
    total = 0
    for i in range(len(listName)):
        total = total + listName[i]
    return total


def is_it_enough(total, budget):
    print(total)
    print(budget)
    if total > budget:
        print('Your budget is not enough you need', total - budget,'RS so you can afford your shopping list')
    elif budget > total and budget - total != 0:
        print('Your budget is enough and what will left from your budget is', budget - total,' RS')
    else:
        print('Your budget is enough to your shopping list and what will left from your budget is nothing ')

budgetCounter()
