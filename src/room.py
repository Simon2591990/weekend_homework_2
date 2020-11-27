class Room:
    def __init__(self, room_name, capacity, room_price):
        self.guests = []
        self.songs = []
        self.capacity = capacity
        self.room_name = room_name
        self.room_price = room_price

    def check_in_guest(self, person):
        if len(self.guests) < self.capacity:
            person.remove_cash(self.room_price)
            self.guests.append(person)
        else:
            return "Sorry, room is full"

    def check_out_guest(self, person):
        self.guests.remove(person)

    def add_song(self, song):
        self.songs.append(song)

    def play_song(self, song):
        return f"Next up we have {song.name}"

