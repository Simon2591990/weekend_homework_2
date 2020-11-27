class Room:
    def __init__(self, room_name, capacity):
        self.guests = []
        self.songs = []
        self.capacity = capacity
        self.room_name = room_name