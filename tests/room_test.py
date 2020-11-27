import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.person_1 = Guest("Songy McSongface", 36, 50)
        self.person_2 = Guest("Singy McSingface", 34, 45)
        self.song_1 = Song("Never Gonna Give You Up", "Rick Astley", "Pop")
        self.room = Room("Room 1", 5)

    def test_room_capacity(self):
        self.assertEqual(5, self.room.capacity)
    
    def test_room_name(self):
        self.assertEqual("Room 1", self.room.room_name)

    def test_check_in_guest(self):
        self.room.check_in_guest(self.person_1)
        self.assertEqual("Songy McSongface", self.room.guests[0].name)

    def test_check_out_guest(self):
        self.room.check_in_guest(self.person_1)
        self.room.check_out_guest(self.person_1)
        self.assertEqual([], self.room.guests)
    
    def test_add_song(self):
        self.room.add_song(self.song_1)
        self.assertEqual("Never Gonna Give You Up", self.room.songs[0].name)

    def test_check_in_guest__reached_capacity(self):
        self.room.check_in_guest(self.person_1)
        self.room.check_in_guest(self.person_1)
        self.room.check_in_guest(self.person_1)
        self.room.check_in_guest(self.person_1)
        self.room.check_in_guest(self.person_1)
        self.room.check_in_guest(self.person_1)
        self.assertEqual(5, len(self.room.guests))

    def test_check_in_guest__returns_string(self):
        self.room.check_in_guest(self.person_1)
        self.room.check_in_guest(self.person_1)
        self.room.check_in_guest(self.person_1)
        self.room.check_in_guest(self.person_1)
        self.room.check_in_guest(self.person_1)
        self.room.check_in_guest(self.person_1)
        self.assertEqual("Sorry, room is full", self.room.check_in_guest(self.person_1) )



        

    


    

        
