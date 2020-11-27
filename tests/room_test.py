import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
from src.bar import Bar


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.person_1 = Guest("Singy McSingface", 36, 50, "Never Gonna Give You Up", "Beer")
        self.person_2 = Guest("Dancy McDanceface", 30, 60, "Sandstorm", "Wine")
        self.song_1 = Song("Never Gonna Give You Up", "Rick Astley", "Pop")
        self.song_2 = Song("Sandstorm", "Darude", "Dance")
        self.room = Room("Room 1", 5, 10)
        drinks = {"Beer": 4, "Wine": 8, "Whiskey": 5, "Vodka": 2}
        self.bar = Bar("Karaoke Bar", 100, drinks)
        
        

    def test_room_capacity(self):
        self.assertEqual(5, self.room.capacity)
    
    def test_room_name(self):
        self.assertEqual("Room 1", self.room.room_name)

    def test_check_in_guest(self):
        self.room.check_in_guest(self.person_1)
        self.assertEqual("Singy McSingface", self.room.guests[0].name)

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
        self.assertEqual("Sorry, room is full", self.room.check_in_guest(self.person_1))

    def test_remove_cash_on_check_in(self):
        self.room.check_in_guest(self.person_1)
        self.assertEqual(40, self.person_1.cash)

    def test_play_song__title_and_artist(self):
        self.assertEqual("Next up we have Singy McSingface with Never Gonna Give You Up by Rick Astley", 
        self.room.play_song(self.song_1, self.person_1))

    def test_get_song_by_name(self):
        self.room.add_song(self.song_1)
        self.assertEqual(self.song_1, self.room.get_song_by_name("Never Gonna Give You Up"))
    
    def test_add_favourite_songs(self):
        self.room.add_song(self.song_1)
        self.room.add_song(self.song_2)
        self.room.check_in_guest(self.person_1)
        self.room.check_in_guest(self.person_2)
        self.room.add_fav_songs_to_playlist()
        self.assertEqual(2, len(self.room.playlist))

    def test_add_favourite_songs__song_not_found(self):
        self.room.add_song(self.song_2)
        self.room.check_in_guest(self.person_1)
        self.room.check_in_guest(self.person_2)
        self.room.add_fav_songs_to_playlist()
        self.assertEqual(1, len(self.room.playlist))
    
    
        


      





    







        

    


    

        
