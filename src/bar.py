class Bar:

    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
        
        

    def get_drink_by_name(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink
    
    