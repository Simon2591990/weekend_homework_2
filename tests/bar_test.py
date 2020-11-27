import unittest
from src.bar import Bar

class TestBar(unittest.TestCase):
    def setUp(self):
        drinks = {"Beer": 4, "Wine": 8, "Whiskey": 5, "Vodka": 2}
        self.bar = Bar("Karaoke Bar", 100, drinks)

    def test_get_bar_name(self):
        self.assertEqual("Karaoke Bar", self.bar.name)
