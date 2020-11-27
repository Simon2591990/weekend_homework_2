class Bar:

    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
    
    def customer_buys_drink(self, person):
            cost = self.drinks[person.fav_drink]
            person.cash -= cost
