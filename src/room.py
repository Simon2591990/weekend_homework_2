class Room:
    def __init__(self, room_name, capacity):
        self.guests = []
        self.songs = []
        self.capacity = capacity
        self.room_name = room_name

    def check_in_guest(self, person):
        if len(self.guests) < self.capacity:
            self.guests.append(person)
        else:
            return "Sorry, room is full"

    def check_out_guest(self, person):
        self.guests.remove(person)

    def add_song(self, song):
        self.songs.append(song)
