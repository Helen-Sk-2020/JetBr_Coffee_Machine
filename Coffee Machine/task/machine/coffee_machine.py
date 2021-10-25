class CoffeeMachine:
    
    def __init__(self, water, milk, coffee, cups, cash):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.cash = cash
    
    def buy_espresso(self):
        if self.water < 250:
            print('Sorry, not enough water!\n')
        else:
            if self.coffee < 16:
                print('Sorry, not enough coffee!\n')
            else:
                if self.cups < 1:
                    print('Sorry, not enough cups!\n')
                else:
                    self.water -= 250
                    self.coffee -= 16
                    self.cups -= 1
                    self.cash += 4
                    print('I have enough resources, making you a coffee!\n')
    
    def buy_latte(self):
        if self.water < 350:
            print('Sorry, not enough water!\n')
        else:
            if self.milk < 75:
                print('Sorry, not enough milk!\n')
            else:
                if self.coffee < 20:
                    print('Sorry, not enough coffee!\n')
                else:
                    if self.cups < 1:
                        print('Sorry, not enough cups!\n')
                    else:
                        self.water -= 350
                        self.milk -= 75
                        self.coffee -= 20
                        self.cups -= 1
                        self.cash += 7
                        print('I have enough resources, making you a coffee!\n')
    
    def buy_cappuccino(self):
        if self.water < 200:
            print('Sorry, not enough water\n')
        else:
            if self.milk < 100:
                print('Sorry, not enough milk!\n')
            else:
                if self.coffee < 12:
                    print('Sorry, not enough coffee!\n')
                else:
                    if self.cups < 1:
                        print('Sorry, not enough cups!\n')
                    else:
                        self.water -= 200
                        self.milk -= 100
                        self.coffee -= 12
                        self.cups -= 1
                        self.cash += 6
                        print('I have enough resources, making you a coffee!\n')
    
    def take(self):
        print(f"I gave you ${self.cash}\n")
        self.cash = 0
    
    def remaining(self):
        print(f'''The coffee machine has:
    {self.water} of water
    {self.milk} of milk
    {self.coffee} of coffee beans
    {self.cups} of disposable cups
    ${self.cash} of money\n''')
    
    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, '
              '3 - cappuccino, back - to main menu:')
        chose = input()
        if chose == '1':
            self.buy_espresso()
        elif chose == '2':
            self.buy_latte()
        elif chose == '3':
            self.buy_cappuccino()
        elif chose == 'back':
            pass
    
    def fill(self):
        print('Write how many ml of water you want to add:')
        self.water += int(input())
        print('Write how many ml of milk you want to add:')
        self.milk += int(input())
        print('Write how many grams of coffee beans you want to add:')
        self.coffee += int(input())
        print('Write how many disposable coffee cups you want to add:')
        self.cups += int(input())
    
    def action(self):
        while True:
            print('Write action (buy, fill, take, remaining, exit):')
            action = input()
            if action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                self.remaining()
            elif action == 'exit':
                break


machine = CoffeeMachine(400, 540, 120, 9, 550)
machine.action()
