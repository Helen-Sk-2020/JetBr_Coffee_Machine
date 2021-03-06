class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars=None, cents=None):
        self.dollars = dollars
        self.cents = cents
        
    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.dollars += (self.cents + deposit_cents) // 100
        self.cents = (self.cents + deposit_cents) % 100
        
