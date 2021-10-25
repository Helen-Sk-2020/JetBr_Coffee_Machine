def buy(x):
    print('What do you want to buy? 1 - espresso, 2 - latte, '
          '3 - cappuccino, back - to main menu:')
    chose = input()
    if chose == '1':
        return buy_espresso(x)
    elif chose == '2':
        return buy_latte(x)
    elif chose == '3':
        return buy_cappuccino(x)
    elif chose == 'back':
        return x
    
    
def buy_espresso(x):
    espresso = [250, 16, 1, 4]
    lack = ''
    for key, value in x.items():
        if key == 'water':
            if x['water'] <= espresso[0]:
                lack = 'water'
        if key == 'coffee':
            if x['coffee'] <= espresso[1]:
                lack = 'coffee'
        if key == 'cups':
            if x['cups'] <= espresso[2]:
                lack = 'cups'

    if lack == '':
        for key, value in x.items():
            if key == 'water':
                x['water'] = value - espresso[0]
            elif key == 'coffee':
                x['coffee'] = value - espresso[1]
            elif key == 'cups':
                x['cups'] = value - espresso[2]
            elif key == 'money':
                x['money'] = value + espresso[3]
        print('I have enough resources, making you a coffee!\n')
        return x
    else:
        print(f'Sorry, not enough {lack}!\n')
        

def buy_latte(x):
    latte = [350, 75, 20, 1, 7]
    lack = ''
    for key, value in x.items():
        if key == 'water':
            if x['water'] <= latte[0]:
                lack = 'water'
        elif key == 'milk':
            if x['milk'] <= latte[1]:
                lack = 'milk'
        elif key == 'coffee':
            if x['coffee'] <= latte[2]:
                lack = 'coffee'
        elif key == 'cups':
            if x['cups'] <= latte[3]:
                lack = 'cups'

    if lack == '':
        for key, value in x.items():
            if key == 'water':
                x['water'] = value - latte[0]
            elif key == 'milk':
                x['milk'] = value - latte[1]
            elif key == 'coffee':
                x['coffee'] = value - latte[2]
            elif key == 'cups':
                x['cups'] = value - latte[3]
            elif key == 'money':
                x['money'] = value + latte[4]
                
        print('I have enough resources, making you a coffee!\n')
    
    else:
        print(f'Sorry, not enough {lack}!\n')
    return x


def buy_cappuccino(x):
    cappuccino = [200, 100, 12, 1, 6]
    lack = ''
    for key, value in x.items():
        if key == 'water':
            if x['water'] <= cappuccino[0]:
                lack = 'water'
        elif key == 'milk':
            if x['milk'] <= cappuccino[1]:
                lack = 'milk'
        elif key == 'coffee':
            if x['coffee'] <= cappuccino[2]:
                lack = 'coffee'
        elif key == 'cups':
            if x['cups'] <= cappuccino[3]:
                lack = 'cups'

    if lack == '':
        for key, value in x.items():
            if key == 'water':
                x['water'] = value - cappuccino[0]
            elif key == 'milk':
                x['milk'] = value - cappuccino[1]
            elif key == 'coffee':
                x['coffee'] = value - cappuccino[2]
            elif key == 'cups':
                x['cups'] = value - cappuccino[3]
            elif key == 'money':
                x['money'] = value + cappuccino[4]
        print('I have enough resources, making you a coffee!\n')
    else:
        print(f'Sorry, not enough {lack}!\n')
    return x
    
    
def fill(x):
    questions = ['Write how many ml of water you want to add:',
                 'Write how many ml of milk you want to add:',
                 'Write how many grams of coffee beans you want to add:',
                 'Write how many disposable coffee cups you want to add:']
    count = 0
    how_much_add = []
    while count < 4:
        print(questions[count])
        how_much_add.append(int(input()))
        count += 1
    for key, value in x.items():
        if key == 'water':
            x['water'] = value + how_much_add[0]
        elif key == 'milk':
            x['milk'] = value + how_much_add[1]
        elif key == 'coffee':
            x['coffee'] = value + how_much_add[2]
        elif key == 'cups':
            x['cups'] = value + how_much_add[3]
    return x


def take(x):
    print(f"I gave you ${x['money']}\n")
    x['money'] = 0
    return x


def remaining(x):
    print(f'''The coffee machine has:
{x['water']} of water
{x['milk']} of milk
{x['coffee']} of coffee beans
{x['cups']} of disposable cups
{x['money']} of money\n''')
    return x


available = {'water': 400, 'milk': 540, 'coffee': 120, 'cups': 9, 'money': 550}
while True:
    print('Write action (buy, fill, take, remaining, exit):')
    action = input()
    if action == 'buy':
        available = buy(available)
    elif action == 'fill':
        available = fill(available)
    elif action == 'take':
        available = take(available)
    elif action == 'remaining':
        available = remaining(available)
    elif action == 'exit':
        break
