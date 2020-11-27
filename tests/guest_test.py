import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Singy McSingface", 36)

    def test_guest_has_name(self):
        self.assertEqual("Singy McSingface", self.guest.name)

    
