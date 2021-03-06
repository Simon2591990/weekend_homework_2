import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.never_gonna_give_you_up = Song("Never Gonna Give You Up", "Rick Astley", "Pop" )

    def test_song_has_name(self):
        self.assertEqual("Never Gonna Give You Up", self.never_gonna_give_you_up.name)

    def test_song_has_artist(self):
        self.assertEqual("Rick Astley", self.never_gonna_give_you_up.artist)

    def test_song_has_genre(self):
        self.assertEqual("Pop", self.never_gonna_give_you_up.genre)

