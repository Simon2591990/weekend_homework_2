class Bar:

    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
    
    def customer_buys_drink_pay_at_bar(self, person):
        cost = self.drinks[person.fav_drink]
        person.remove_cash(cost)

    def customer_buys_drink_add_to_tab(self, room, person):
        amount = self.drinks[person.fav_drink]
        room.tab += amount



