class Guest:
    def __init__(self, name, age, cash, fav_song, fav_drink):
        self.name = name
        self.age = age
        self.cash = cash
        self.fav_song = fav_song
        self.fav_drink = fav_drink

    def remove_cash(self, amount):
        self. cash -= amount