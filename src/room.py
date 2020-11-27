class Room:
    def __init__(self, room_name, capacity, room_price):
        self.guests = []
        self.songs = []
        self.capacity = capacity
        self.room_name = room_name
        self.room_price = room_price
        self.playlist = []

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

    def play_song(self, song, person):
        return f"Next up we have {person.name} with {song.name} by {song.artist}"

    def get_song_by_name(self, song_name):
        for song in self.songs:
            if song.name == song_name:
                return song

    def add_fav_songs_to_playlist(self):
        for guest in self.guests:
            song = self.get_song_by_name(guest.fav_song)
            if song != None:
                self.playlist.append(song)
        
        




