class Room:
    def __init__(self, room_name, capacity):
        self.guests = []
        self.songs = []
        self.capacity = capacity
        self.room_name = room_name

    def check_in_guest(self, person):
        self.guests.append(person)

    def check_out_guest(self, person):
        self.guests.remove(person)

    def add_song(self, song):
        self.songs.append(song)
