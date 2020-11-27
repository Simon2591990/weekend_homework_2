import unittest
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        person_1 = Guest("Songy McSongface", 36)
        person_2 = Guest("Singy McSingface", 34)
        party = [person_1, person_2]
        self.room = Room(party, 5)

    def test_room_capacity(self):
        self.assertEqual(5, self.room.capacity)


    

        
